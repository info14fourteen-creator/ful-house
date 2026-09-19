import os
import pdfplumber
from datetime import datetime
from decimal import Decimal
from .models import BankOperation, BankStatement
from .classifier import classify_operation, validate_operation_date


class BankStatementProcessor:
    def __init__(self):
        self.supported_banks = ['Сбер', 'Т-Банк', 'Альфа-Банк']
        self.current_bank = None
        
    def set_bank(self, bank_name):
        if bank_name not in self.supported_banks:
            raise ValueError(f'Unsupported bank: {bank_name}')
        self.current_bank = bank_name
        
    def process_alfa_statement(self, file_path):
        """
        Process Alfa-Bank PDF statement
        Returns list of BankOperation objects
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'Statement file not found: {file_path}')
            
        operations = []
        
        with pdfplumber.open(file_path) as pdf:
            # Process first page to get statement info
            first_page = pdf.pages[0]
            text = first_page.extract_text()
            
            # Extract period information
            period_start, period_end = self._extract_period(text)
            
            # Extract account number
            account_number = self._extract_account_number(text)
            
            # Extract balances
            opening_balance, closing_balance = self._extract_balances(text)
            
            # Process all pages for operations
            for page in pdf.pages:
                page_text = page.extract_text()
                page_operations = self._parse_operations(page_text, period_start, account_number)
                operations.extend(page_operations)
                
        return operations
    
    def _extract_period(self, text):
        """
        Extract period from statement text
        Returns (start_date, end_date) as datetime objects
        """
        import re
        
        # Look for date patterns like "с 01.01.2023 по 31.01.2023"
        period_pattern = r'с\s+(\d{2}\.\d{2}\.\d{4})\s+по\s+(\d{2}\.\d{2}\.\d{4})'
        match = re.search(period_pattern, text)
        
        if match:
            start_str = match.group(1)
            end_str = match.group(2)
            
            try:
                start_date = datetime.strptime(start_str, '%d.%m.%Y')
                end_date = datetime.strptime(end_str, '%d.%m.%Y')
                return start_date, end_date
            except ValueError:
                pass
        
        # Default to None if not found
        return None, None
    
    def _extract_account_number(self, text):
        """
        Extract account number from statement text
        """
        import re
        
        # Look for account pattern like "Номер счёта: 40817810100000000000"
        account_pattern = r'Номер\s+счёта:\s+(\d{20})'
        match = re.search(account_pattern, text)
        
        if match:
            return match.group(1)
        
        return None
    
    def _extract_balances(self, text):
        """
        Extract opening and closing balances from statement text
        Returns (opening_balance, closing_balance) as Decimal
        """
        import re
        
        # Look for balance patterns
        opening_pattern = r'Остаток\s+на\s+начало\s+периода:\s+([\d\s]+)'
        closing_pattern = r'Остаток\s+на\s+конец\s+периода:\s+([\d\s]+)'
        
        opening_match = re.search(opening_pattern, text)
        closing_match = re.search(closing_pattern, text)
        
        opening_balance = None
        closing_balance = None
        
        if opening_match:
            balance_str = opening_match.group(1).replace(' ', '')
            try:
                opening_balance = Decimal(balance_str)
            except ValueError:
                pass
                
        if closing_match:
            balance_str = closing_match.group(1).replace(' ', '')
            try:
                closing_balance = Decimal(balance_str)
            except ValueError:
                pass
                
        return opening_balance, closing_balance
    
    def _parse_operations(self, text, period_start, account_number):
        """
        Parse operations from page text
        Returns list of BankOperation objects
        """
        import re
        
        # Pattern to match operation lines
        # Expected format: date | code | description | amount | direction | opening_balance | closing_balance
        operation_pattern = r'(\d{2}\.\d{2}\.\d{4})\s+(\w+)\s+(.*?)\s+([\d\s]+)\s+(\w+)\s+([\d\s]+)\s+([\d\s]+)'
        
        operations = []
        
        # Find all operation lines
        matches = re.findall(operation_pattern, text, re.DOTALL)
        
        for match in matches:
            try:
                # Extract data from match
                date_str = match[0]
                code = match[1]
                description = match[2].strip()
                amount_str = match[3].replace(' ', '')
                direction = match[4]  # Will be processed later
                opening_balance_str = match[5].replace(' ', '')
                closing_balance_str = match[6].replace(' ', '')
                
                # Parse date
                operation_date = datetime.strptime(date_str, '%d.%m.%Y')
                
                # Parse amounts
                amount = Decimal(amount_str)
                opening_balance = Decimal(opening_balance_str)
                closing_balance = Decimal(closing_balance_str)
                
                # Classify operation
                category, classified_description, op_direction = classify_operation(code, operation_date, amount, description)
                
                # Validate date consistency
                date_valid = validate_operation_date(operation_date, code)
                
                # Create BankOperation object
                bank_op = BankOperation(
                    operation_date=operation_date,
                    operation_code=code,
                    description=classified_description,
                    amount=amount,
                    direction=op_direction,
                    opening_balance=opening_balance,
                    closing_balance=closing_balance,
                    account_number=account_number
                )
                
                operations.append(bank_op)
                
            except Exception as e:
                # Log error but continue processing
                print(f'Error parsing operation: {e}')
                continue
                
        return operations
    
    def generate_internal_report(self, statement_id, operations):
        """
        Generate internal PDF report based on statement and operations
        Returns file path of generated PDF
        """
        from .report import InternalReportGenerator
        
        generator = InternalReportGenerator()
        return generator.generate_report(statement_id, operations)