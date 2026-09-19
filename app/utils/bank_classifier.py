import re
from datetime import datetime

class AlphaBankClassifier:
    """
    Classifies bank operations based on Alpha-Bank operation codes.
    
    For detailed code information see:
    - B01DDMMYYNNNNNNN: Internal transfers between own accounts
    - C16DDMMYYNNNNNNN: Outgoing transfer via SBP to phone number
    - C42DDMMYYNNNNNNN: Outgoing transfer via SBP to phone number
    - C46DDMMYYNNNNNNN: Outgoing transfer via SBP to phone number
    - C17DDMMYYNNNNNNN: Incoming transfer via SBP from phone number
    - C19DDMMYYNNNNNNN: Incoming transfer from Sberbank
    - C07DDMMYYNNNNNNN: Transfer of funds, mostly expense
    - C21DDMMYYNNNNNNN: Payment to merchant via SBP
    - C51DDMMYYNNNNNNN: QR payment through Sberbank
    - C52DDMMYYNNNNNNN: QR payment refund
    - C78DDMMYYNNNNNNN: Fine payment via SBP
    - A01DDMMYYNNNNNNN: Mobile communication, state fee, fine or other service payment
    - CRD_XXXXXX: Card operation: purchase, cash withdrawal, service payment
    - CHS-2A-MMDDNNNNN: Cash withdrawal from account; expense
    - CASHIN<terminal_id>: Cash deposit via Recycling device; income
    - MPL1_<id>: Cashback accrual; income
    - PML<id>: Interest payment on balance; income
    - TKS1_<id>: Subscription fee for "Alpha-Smart"
    - MOCOD<id> and MAKTD<id>: Insurance payments
    - OP1E<subtype><YY><M><D36><id>: Internal operations between own accounts or internal operations; direction determined by sign of amount and description
    """
    
    # Pattern for date extraction from codes
    DATE_PATTERN = re.compile(r'(\d{6})')
    
    # Classification patterns for Alpha-Bank codes
    CODE_PATTERNS = {
        'B01': 'Internal transfer between own accounts',
        'C16': 'Outgoing transfer via SBP to phone number',
        'C42': 'Outgoing transfer via SBP to phone number',
        'C46': 'Outgoing transfer via SBP to phone number',
        'C17': 'Incoming transfer via SBP from phone number',
        'C19': 'Incoming transfer from Sberbank',
        'C07': 'Transfer of funds, mostly expense',
        'C21': 'Payment to merchant via SBP',
        'C51': 'QR payment through Sberbank',
        'C52': 'QR payment refund',
        'C78': 'Fine payment via SBP',
        'A01': 'Mobile communication, state fee, fine or other service payment',
        'CRD_': 'Card operation: purchase, cash withdrawal, service payment',
        'CHS-2A': 'Cash withdrawal from account; expense',
        'CASHIN': 'Cash deposit via Recycling device; income',
        'MPL1_': 'Cashback accrual; income',
        'PML': 'Interest payment on balance; income',
        'TKS1_': 'Subscription fee for "Alpha-Smart"',
        'MOCOD': 'Insurance payment',
        'MAKTD': 'Insurance payment',
        'OP1E': 'Internal operations between own accounts or internal operations'
    }
    
    @staticmethod
    def extract_date_from_code(code: str, operation_date: datetime) -> datetime:
        """
        Extract date from code if it matches DDMMYY pattern.
        Compare with actual operation date.
        """
        # Find all 6-digit sequences in the code
        matches = AlphaBankClassifier.DATE_PATTERN.findall(code)
        
        # Try to extract a date from the last match (or first if there's only one)
        if matches:
            date_str = matches[-1]  # Use the last 6-digit sequence
            try:
                # Parse DDMMYY format
                day = int(date_str[:2])
                month = int(date_str[2:4])
                year = int(date_str[4:])
                
                # Convert 2-digit year to 4-digit (assuming 20xx)
                if year < 100:
                    year += 2000
                
                return datetime(year, month, day)
            except ValueError:
                # If date parsing fails, return original operation date
                return operation_date
        
        return operation_date
    
    @staticmethod
    def classify_operation(code: str, amount: float, description: str) -> tuple:
        """
        Classify bank operation based on code.
        Returns (direction, category_description)
        """
        direction = 'income' if amount > 0 else 'expense'
        
        # Handle special cases
        if code.startswith('CHS-2A'):
            # For CHS-2A codes, description should be formatted as:
            # Выдача наличных рублей со счета {номер_счёта} {Фамилия И.О.}
            return 'expense', 'Cash withdrawal from account'
        
        elif code.startswith('CASHIN'):
            return 'income', 'Cash deposit via Recycling device'
        
        elif code.startswith('MPL1_'):
            return 'income', 'Cashback accrual'
        
        elif code.startswith('PML'):
            return 'income', 'Interest payment on balance'
        
        elif code.startswith('TKS1_'):
            return 'expense', 'Subscription fee for "Alpha-Smart"'
        
        elif code.startswith('MOCOD') or code.startswith('MAKTD'):
            return 'expense', 'Insurance payment'
        
        elif code.startswith('B01'):
            # Internal transfer between own accounts
            return direction, 'Internal transfer between own accounts'
        
        elif code.startswith('C16') or code.startswith('C42') or code.startswith('C46'):
            # Outgoing transfers via SBP
            return 'expense', 'Outgoing transfer via SBP to phone number'
        
        elif code.startswith('C17'):
            # Incoming transfer via SBP from phone number
            return 'income', 'Incoming transfer via SBP from phone number'
        
        elif code.startswith('C19'):
            # Incoming transfer from Sberbank
            return 'income', 'Incoming transfer from Sberbank'
        
        elif code.startswith('C07'):
            # Transfer of funds, mostly expense
            return 'expense', 'Transfer of funds, mostly expense'
        
        elif code.startswith('C21'):
            # Payment to merchant via SBP
            return 'expense', 'Payment to merchant via SBP'
        
        elif code.startswith('C51'):
            # QR payment through Sberbank
            return 'expense', 'QR payment through Sberbank'
        
        elif code.startswith('C52'):
            # QR payment refund
            return 'income', 'QR payment refund'
        
        elif code.startswith('C78'):
            # Fine payment via SBP
            return 'expense', 'Fine payment via SBP'
        
        elif code.startswith('A01'):
            # Mobile communication, state fee, fine or other service payment
            return 'expense', 'Mobile communication, state fee, fine or other service payment'
        
        elif code.startswith('CRD_'):
            # Card operation: purchase, cash withdrawal, service payment
            return direction, 'Card operation: purchase, cash withdrawal, service payment'
        
        elif code.startswith('OP1E'):
            # Internal operations between own accounts or internal operations
            return direction, 'Internal operations between own accounts or internal operations'
        
        else:
            # Default classification
            return direction, 'Unknown operation type'