import pdfplumber
from datetime import datetime
from dateutil.parser import parse
from typing import List, Dict, Any
import re


class AlphaBankStatementParser:
    """
    Parser for Alpha-Bank PDF statements.
    
    Extracts:
    - Operation date
    - Operation code
    - Description
    - Amount
    - Direction (income/expense)
    - Opening and closing balance
    - Account requisites
    - Statement period
    """
    
    def __init__(self):
        # Pattern to extract date from operation codes
        self.date_pattern = re.compile(r'(\d{6})')
        
    def parse_statement(self, pdf_path: str) -> Dict[str, Any]:
        """
        Parse entire bank statement PDF.
        Returns structured data about the statement and its operations.
        """
        try:
            with pdfplumber.open(pdf_path) as pdf:
                # Extract basic statement info
                statement_info = self._extract_statement_info(pdf)
                
                # Extract operations
                operations = self._extract_operations(pdf)
                
                return {
                    'statement_info': statement_info,
                    'operations': operations
                }
        except Exception as e:
            raise ValueError(f"Error parsing PDF: {str(e)}")
    
    def _extract_statement_info(self, pdf) -> Dict[str, Any]:
        """
        Extract general statement information.
        """
        # Get first page
        if len(pdf.pages) == 0:
            raise ValueError("PDF has no pages")
            
        page = pdf.pages[0]
        text = page.extract_text()
        
        # Extract account number
        account_match = re.search(r'Номер счета:\s*(\d+)', text)
        account_number = account_match.group(1) if account_match else "Unknown"
        
        # Extract period
        period_match = re.search(r'(\d{2}\.\d{2}\.\d{4})\s*-\s*(\d{2}\.\d{2}\.\d{4})', text)
        if period_match:
            start_date = parse(period_match.group(1))
            end_date = parse(period_match.group(2))
        else:
            start_date = datetime.now()
            end_date = datetime.now()
            
        # Extract balances
        opening_balance_match = re.search(r'Остаток на начало периода:\s*([\d,\.]+)', text)
        opening_balance = float(opening_balance_match.group(1).replace(',', '.')) if opening_balance_match else 0.0
        
        closing_balance_match = re.search(r'Остаток на конец периода:\s*([\d,\.]+)', text)
        closing_balance = float(closing_balance_match.group(1).replace(',', '.')) if closing_balance_match else 0.0
        
        return {
            'account_number': account_number,
            'period_start': start_date,
            'period_end': end_date,
            'opening_balance': opening_balance,
            'closing_balance': closing_balance
        }
    
    def _extract_operations(self, pdf) -> List[Dict[str, Any]]:
        """
        Extract individual operations from the statement.
        """
        operations = []
        
        # Look for content in all pages (usually operations are on second page)
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            
            # Skip header and footers
            if 'Остаток на начало периода' in text or 'Остаток на конец периода' in text:
                continue
                
            # Parse operations table (simplified approach)
            lines = text.split('\n')
            for line in lines:
                if self._is_operation_line(line):
                    operation = self._parse_operation_line(line)
                    if operation:
                        operations.append(operation)
        
        return operations
    
    def _is_operation_line(self, line: str) -> bool:
        """
        Check if a line contains operation data.
        """
        # Simple check - lines with dates and amounts
        date_pattern = re.compile(r'\d{2}\.\d{2}\.\d{4}')
        amount_pattern = re.compile(r'[\d,\.]+')
        
        return bool(date_pattern.search(line) and amount_pattern.search(line))
    
    def _parse_operation_line(self, line: str) -> Dict[str, Any]:
        """
        Parse a single operation line.
        Returns operation data or None if parsing fails.
        """
        try:
            # Split by whitespace and clean
            parts = [part.strip() for part in line.split() if part.strip()]
            
            if len(parts) < 4:
                return None
            
            # Extract date (first part)
            date_str = parts[0]
            operation_date = parse(date_str)
            
            # Extract operation code (second part)
            operation_code = parts[1] if len(parts) > 1 else ""
            
            # Extract amount (last part)
            amount_str = parts[-1]
            # Handle comma as decimal separator
            amount_str = amount_str.replace(',', '.')
            amount = float(amount_str)
            
            # Extract description (middle parts)
            description_parts = parts[2:-1]  # All parts except date and amount
            description = ' '.join(description_parts)
            
            return {
                'operation_date': operation_date,
                'operation_code': operation_code,
                'description': description,
                'amount': amount,
                'direction': 'income' if amount > 0 else 'expense'
            }
        except (ValueError, IndexError) as e:
            # If parsing fails, return None
            return None