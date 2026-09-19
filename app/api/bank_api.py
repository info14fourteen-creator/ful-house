from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
import os
import shutil

from app.database import get_db
from app.models.bank_statement import BankStatement, BankOperation
from app.parser.alpha_bank_parser import AlphaBankStatementParser
from app.utils.bank_classifier import AlphaBankClassifier
from app.utils.pdf_generator import InternalReportGenerator

router = APIRouter(prefix="/bank", tags=["Bank Statements"])

@router.get("/statements", response_model=List[BankStatement])
async def get_bank_statements(db: Session = Depends(get_db)):
    statements = db.query(BankStatement).all()
    return statements

@router.get("/statements/{statement_id}", response_model=BankStatement)
async def get_bank_statement(statement_id: int, db: Session = Depends(get_db)):
    statement = db.query(BankStatement).filter(BankStatement.id == statement_id).first()
    if not statement:
        raise HTTPException(status_code=404, detail="Bank statement not found")
    return statement

@router.get("/operations", response_model=List[BankOperation])
async def get_bank_operations(db: Session = Depends(get_db)):
    operations = db.query(BankOperation).all()
    return operations

@router.get("/operations/{operation_id}", response_model=BankOperation)
async def get_bank_operation(operation_id: int, db: Session = Depends(get_db)):
    operation = db.query(BankOperation).filter(BankOperation.id == operation_id).first()
    if not operation:
        raise HTTPException(status_code=404, detail="Bank operation not found")
    return operation

@router.post("/statements", response_model=BankStatement)
async def create_bank_statement(statement: BankStatement, db: Session = Depends(get_db)):
    db.add(statement)
    db.commit()
    db.refresh(statement)
    return statement

@router.post("/statements/import", response_model=dict)
async def import_bank_statement(
    bank_name: str,
    account_number: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    
    # Validate bank name
    if bank_name not in ['Alfa-Bank', 'Sber', 'T-Bank']:
        raise HTTPException(status_code=400, detail="Unsupported bank")
    
    # For now, only process Alfa-Bank statements
    if bank_name != 'Alfa-Bank':
        raise HTTPException(status_code=400, detail="Only Alfa-Bank statements are supported at this time")
    
    # Save uploaded file
    file_location = f"/tmp/{file.filename}"
    with open(file_location, "wb+") as buffer:
        shutil.write(buffer)
    
    try:
        # Parse the statement
        parser = AlphaBankStatementParser()
        parsed_data = parser.parse_statement(file_location)
        
        # Create bank statement record
        statement = BankStatement(
            bank_name=bank_name,
            account_number=account_number,
            statement_period_start=parsed_data['statement_info']['period_start'],
            statement_period_end=parsed_data['statement_info']['period_end'],
            opening_balance=parsed_data['statement_info']['opening_balance'],
            closing_balance=parsed_data['statement_info']['closing_balance'],
            file_path=file_location,
            is_processed=False
        )
        
        db.add(statement)
        db.commit()
        db.refresh(statement)
        
        # Process operations
        operations = []
        for op_data in parsed_data['operations']:
            # Classify operation
            direction, category = AlphaBankClassifier.classify_operation(
                op_data['operation_code'],
                op_data['amount'],
                op_data['description']
            )
            
            # Extract date from code if applicable
            try:
                extracted_date = AlphaBankClassifier.extract_date_from_code(
                    op_data['operation_code'],
                    op_data['operation_date']
                )
                # If dates don't match, use extracted date
                if extracted_date != op_data['operation_date']:
                    op_data['operation_date'] = extracted_date
            except Exception:
                pass  # Keep original date if extraction fails
            
            operation = BankOperation(
                statement_id=statement.id,
                operation_date=op_data['operation_date'],
                operation_code=op_data['operation_code'],
                description=op_data['description'],
                amount=op_data['amount'],
                direction=direction,
                account_requisites=account_number,
                # We'll set opening and closing balances later when processing all operations
            )
            
            operations.append(operation)
            
        # Add all operations to database
        db.add_all(operations)
        db.commit()
        
        # Update statement with processed flag
        statement.is_processed = True
        db.commit()
        
        return {
            "message": "Statement imported successfully",
            "statement_id": statement.id,
            "operation_count": len(operations)
        }
        
    except Exception as e:
        # Clean up temporary file
        if os.path.exists(file_location):
            os.remove(file_location)
        
        raise HTTPException(status_code=500, detail=f"Error importing statement: {str(e)}")

@router.get("/statements/{statement_id}/report", response_model=dict)
async def generate_statement_report(statement_id: int, db: Session = Depends(get_db)):
    # Get statement and operations
    statement = db.query(BankStatement).filter(BankStatement.id == statement_id).first()
    if not statement:
        raise HTTPException(status_code=404, detail="Bank statement not found")
    
    operations = db.query(BankOperation).filter(BankOperation.statement_id == statement_id).all()
    
    # Calculate totals
    total_income = sum(op.amount for op in operations if op.amount > 0)
    total_expenses = sum(op.amount for op in operations if op.amount < 0)
    
    # Prepare report data
    report_data = {
        "period_start": statement.statement_period_start.strftime('%d.%m.%Y'),
        "period_end": statement.statement_period_end.strftime('%d.%m.%Y'),
        "opening_balance": float(statement.opening_balance),
        "closing_balance": float(statement.closing_balance),
        "total_income": float(total_income),
        "total_expenses": float(abs(total_expenses)),  # Show as positive value
        "operations": [
            {
                "operation_date": op.operation_date,
                "operation_code": op.operation_code,
                "description": op.description,
                "amount": float(op.amount)
            }
            for op in operations
        ]
    }
    
    # Generate PDF report
    pdf_generator = InternalReportGenerator()
    report_path = f"/tmp/statement_{statement_id}.pdf"
    pdf_generator.generate_report(report_data, report_path)
    
    return {
        "message": "Report generated successfully",
        "report_path": report_path,
        "statement_id": statement.id
    }

@router.post("/statements/{statement_id}/link-operation")
async def link_operation_to_ipds(
    statement_id: int, 
    operation_id: int, 
    ipds_operation_id: int,
    db: Session = Depends(get_db)
):
    # Find the bank operation
    bank_operation = db.query(BankOperation).filter(
        BankOperation.id == operation_id,
        BankOperation.statement_id == statement_id
    ).first()
    
    if not bank_operation:
        raise HTTPException(status_code=404, detail="Bank operation not found")
    
    # Update the link
    bank_operation.ipds_operation_id = ipds_operation_id
    bank_operation.is_linked = True
    bank_operation.link_status = 'linked'
    
    db.commit()
    
    return {
        "message": "Operation linked to IPDS successfully",
        "operation_id": operation_id,
        "ipds_operation_id": ipds_operation_id
    }