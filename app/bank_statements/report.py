import os
from datetime import datetime
from decimal import Decimal
from fpdf import FPDF


class InternalReportGenerator:
    def __init__(self):
        self.template_path = 'app/bank_statements/templates'
        
    def generate_report(self, statement_id, operations):
        """
        Generate internal PDF report based on statement and operations
        Returns file path of generated PDF
        """
        # Calculate totals
        total_income = Decimal('0')
        total_expense = Decimal('0')
        
        for op in operations:
            if op.direction == 'income':
                total_income += op.amount
            elif op.direction == 'expense':
                total_expense += op.amount
        
        # Create PDF
        pdf = FPDF()
        pdf.add_page()
        
        # Set font for title
        pdf.set_font('Arial', 'B', 16)
        
        # Add title
        pdf.cell(0, 10, 'Внутренний отчёт IPDS. Не является банковской выпиской', ln=True, align='C')
        pdf.ln(10)
        
        # Add report details
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, f'Номер отчета: {statement_id}', ln=True)
        pdf.ln(5)
        
        # Add summary table
        self._add_summary_table(pdf, operations, total_income, total_expense)
        
        # Add operations table
        self._add_operations_table(pdf, operations)
        
        # Save file
        filename = f'internal_report_{statement_id}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
        filepath = os.path.join('temp', filename)
        
        # Create temp directory if it doesn't exist
        os.makedirs('temp', exist_ok=True)
        
        pdf.output(filepath)
        
        return filepath
    
    def _add_summary_table(self, pdf, operations, total_income, total_expense):
        """
        Add summary table to PDF
        """
        if not operations:
            return
        
        # Get period from first operation
        start_date = operations[0].operation_date
        end_date = operations[-1].operation_date
        
        pdf.cell(0, 10, f'Период: {start_date.strftime("%d.%m.%Y")} - {end_date.strftime("%d.%m.%Y")}', ln=True)
        pdf.ln(5)
        
        # Summary table
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(40, 10, 'Входящий остаток', border=1)
        pdf.cell(40, 10, 'Сумма поступлений', border=1)
        pdf.cell(40, 10, 'Сумма расходов', border=1)
        pdf.cell(40, 10, 'Исходящий остаток', border=1)
        pdf.ln()
        
        # Data
        pdf.set_font('Arial', '', 10)
        # For simplicity, we'll use first and last operation balances
        opening_balance = operations[0].opening_balance if operations else Decimal('0')
        closing_balance = operations[-1].closing_balance if operations else Decimal('0')
        
        pdf.cell(40, 10, f'{opening_balance}', border=1)
        pdf.cell(40, 10, f'{total_income}', border=1)
        pdf.cell(40, 10, f'{total_expense}', border=1)
        pdf.cell(40, 10, f'{closing_balance}', border=1)
        pdf.ln(10)
    
    def _add_operations_table(self, pdf, operations):
        """
        Add operations table to PDF
        """
        if not operations:
            return
        
        # Table header
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(30, 10, 'Дата проводки', border=1)
        pdf.cell(25, 10, 'Код операции', border=1)
        pdf.cell(80, 10, 'Описание', border=1)
        pdf.cell(40, 10, 'Сумма', border=1)
        pdf.ln()
        
        # Table data
        pdf.set_font('Arial', '', 10)
        for op in operations:
            pdf.cell(30, 10, op.operation_date.strftime('%d.%m.%Y'), border=1)
            pdf.cell(25, 10, op.operation_code, border=1)
            pdf.cell(80, 10, op.description[:30] + '...' if len(op.description) > 30 else op.description, border=1)
            pdf.cell(40, 10, f'{op.amount}', border=1)
            pdf.ln()
        
        pdf.ln(5)