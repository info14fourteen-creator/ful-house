from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from ..processor import BankStatementProcessor
from ..models import BankAccount, BankStatement
import os

router = APIRouter(prefix='/bank-statements', tags=['Bank Statements'])

# Initialize processor
processor = BankStatementProcessor()

@router.get('/banks')
async def get_supported_banks():
    """
    Get list of supported banks
    """
    return {
        'banks': [
            {'name': 'Альфа-Банк', 'status': 'available'},
            {'name': 'Сбер', 'status': 'soon'},
            {'name': 'Т-Банк', 'status': 'soon'}
        ]
    }

@router.post('/import')
async def import_statement(
    bank_name: str,
    file: UploadFile = File(...)
):
    """
    Import bank statement from PDF
    """
    # Validate bank
    if bank_name not in ['Сбер', 'Т-Банк', 'Альфа-Банк']:
        raise HTTPException(400, 'Unsupported bank')
    
    # Only process Alfa-Bank for now
    if bank_name != 'Альфа-Банк':
        raise HTTPException(400, 'Only Alfa-Bank statements are supported at this time')
    
    # Save uploaded file
    file_path = f'temp/{file.filename}'
    os.makedirs('temp', exist_ok=True)
    
    with open(file_path, 'wb') as buffer:
        content = await file.read()
        buffer.write(content)
    
    try:
        # Process statement
        operations = processor.process_alfa_statement(file_path)
        
        # Return result
        return {
            'status': 'success',
            'bank': bank_name,
            'file': file.filename,
            'operation_count': len(operations),
            'operations': [
                {
                    'date': op.operation_date.isoformat(),
                    'code': op.operation_code,
                    'description': op.description,
                    'amount': float(op.amount),
                    'direction': op.direction
                }
                for op in operations
            ]
        }
    except Exception as e:
        raise HTTPException(500, f'Error processing statement: {str(e)}')
    finally:
        # Clean up temporary file
        if os.path.exists(file_path):
            os.remove(file_path)

@router.post('/generate-report')
async def generate_internal_report(statement_id: int):
    """
    Generate internal PDF report
    """
    # In a real implementation, this would fetch operations from database
    # For now, we'll return a placeholder
    try:
        # This would normally fetch operations and call processor.generate_internal_report()
        report_path = f'temp/internal_report_{statement_id}_test.pdf'
        
        # Create a simple PDF for demonstration
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'Внутренний отчёт IPDS. Не является банковской выпиской', ln=True, align='C')
        pdf.ln(10)
        pdf.cell(0, 10, f'Отчет по операциям: {statement_id}', ln=True)
        
        # Save file
        os.makedirs('temp', exist_ok=True)
        pdf.output(report_path)
        
        return {
            'status': 'success',
            'report_path': report_path,
            'message': 'Internal report generated successfully'
        }
    except Exception as e:
        raise HTTPException(500, f'Error generating report: {str(e)}')