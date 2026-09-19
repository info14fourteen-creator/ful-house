from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.database import get_db
from app.models.bank_statement import BankStatement, BankOperation

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