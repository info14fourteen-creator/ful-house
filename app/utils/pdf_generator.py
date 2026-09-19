from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
from typing import List, Dict, Any


class InternalReportGenerator:
    """
    Generates internal PDF reports for IPDS without bank logos, stamps or signatures.
    
    PDF contains:
    - Period
    - Report number
    - Opening balance
    - Total income
    - Total expenses
    - Closing balance
    - Table with operation details (date, code, description, amount)
    """
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
        # Create a custom style for the header
        self.header_style = ParagraphStyle(
            'CustomHeader',
            parent=self.styles['Heading1'],
            fontSize=14,
            spaceAfter=12,
            alignment=1  # Centered
        )
        
    def generate_report(self, report_data: Dict[str, Any], output_path: str) -> None:
        """
        Generate internal PDF report.
        
        Args:
            report_data: Dictionary containing all report information
            output_path: Path where the PDF should be saved
        """
        doc = SimpleDocTemplate(output_path, pagesize=letter)
        elements = []
        
        # Add header with prominent notice
        header_text = 'Внутренний отчёт IPDS. Не является банковской выпиской'
        header = Paragraph(header_text, self.header_style)
        elements.append(header)
        
        # Add spacing
        elements.append(Spacer(1, 20))
        
        # Add main report information
        info_data = [
            ['Период:', f'{report_data["period_start"]} - {report_data["period_end"]}'],
            ['Номер внутреннего отчёта:', report_data.get('report_number', 'N/A')],
            ['Входящий остаток:', f'{report_data["opening_balance"]:.2f}'],
            ['Сумма поступлений:', f'{report_data["total_income"]:.2f}'],
            ['Сумма расходов:', f'{report_data["total_expenses"]:.2f}'],
            ['Исходящий остаток:', f'{report_data["closing_balance"]:.2f}']
        ]
        
        # Create table for information
        info_table = Table(info_data)
        info_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        elements.append(info_table)
        
        # Add spacing
        elements.append(Spacer(1, 20))
        
        # Add operations table
        if 'operations' in report_data and report_data['operations']:
            elements.append(Paragraph('Операции:', self.styles['Heading2']))
            
            # Prepare operation data for table
            operations_data = [['Дата', 'Код операции', 'Описание', 'Сумма']]
            for op in report_data['operations']:
                operations_data.append([
                    op['operation_date'].strftime('%d.%m.%Y'),
                    op['operation_code'],
                    op['description'],
                    f'{op["amount"]:.2f}'
                ])
            
            # Create table
            operations_table = Table(operations_data)
            operations_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            
            elements.append(operations_table)
        else:
            elements.append(Paragraph('Операции отсутствуют', self.styles['Normal']))
        
        # Build PDF
        doc.build(elements)
        print(f"PDF report generated at {output_path}")