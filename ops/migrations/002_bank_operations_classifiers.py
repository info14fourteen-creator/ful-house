import re
from datetime import datetime, timedelta

# Bank operation classifiers for Alfa-Bank
OPERATION_CLASSIFIERS = {
    # Inside bank transfers between own accounts
    'B01': lambda code, date: 'inside_transfer',
    
    # Outgoing transfers via SBP
    'C16': lambda code, date: 'outgoing_sbp_transfer',
    'C42': lambda code, date: 'outgoing_sbp_transfer',
    'C46': lambda code, date: 'outgoing_sbp_transfer',
    
    # Incoming transfers via SBP
    'C17': lambda code, date: 'incoming_sbp_transfer',
    
    # Incoming from Sberbank
    'C19': lambda code, date: 'incoming_sberbank_transfer',
    
    # General fund transfers
    'C07': lambda code, date: 'fund_transfer',
    
    # Payments via SBP
    'C21': lambda code, date: 'sbp_payment',
    
    # QR payments through Sberbank
    'C51': lambda code, date: 'qr_payment',
    'C52': lambda code, date: 'qr_refund',
    
    # Fine payments via SBP
    'C78': lambda code, date: 'fine_payment',
    
    # Mobile communication, fees, etc.
    'A01': lambda code, date: 'service_payment',
    
    # Card operations
    'CRD_': lambda code, date: 'card_operation',
    
    # Cash withdrawal
    'CHS-2A': lambda code, date: 'cash_withdrawal',
    
    # Cash deposit
    'CASHIN': lambda code, date: 'cash_deposit',
    
    # Cashback
    'MPL1_': lambda code, date: 'cashback',
    
    # Interest payments
    'PML': lambda code, date: 'interest_payment',
    
    # Subscription fees
    'TKS1_': lambda code, date: 'subscription_fee',
    
    # Insurance payments
    'MOCOD': lambda code, date: 'insurance_payment',
    'MAKTD': lambda code, date: 'insurance_payment',
    
    # Internal operations between own accounts
    'OP1E': lambda code, date: 'internal_operation',
}

# Function to extract date from operation code (DDMMYY format)
def extract_date_from_code(code):
    if len(code) >= 6:
        try:
            day = int(code[2:4])
            month = int(code[4:6])
            year = int(code[6:8])
            # Assume years in range 2020-2029
            if year >= 20:
                year += 1900
            else:
                year += 2000
            return datetime(year, month, day)
        except ValueError:
            return None
    return None

# Function to classify operation based on code and date
# Returns tuple of (category, description, direction)
def classify_operation(code, date, amount, description):
    # Check for specific patterns
    for pattern, classifier in OPERATION_CLASSIFIERS.items():
        if code.startswith(pattern):
            category = classifier(code, date)
            
            # Special handling for CHS-2A codes
            if pattern == 'CHS-2A':
                direction = 'expense'
                description = f'Выдача наличных рублей со счета {description}'
                return (category, description, direction)
            
            # Determine direction based on amount sign and category
            if amount > 0:
                direction = 'income'
            elif amount < 0:
                direction = 'expense'
            else:
                direction = 'unknown'
                
            return (category, description, direction)
    
    # Default case - classify by amount sign
    if amount > 0:
        direction = 'income'
    elif amount < 0:
        direction = 'expense'
    else:
        direction = 'unknown'
    
    return ('general', description, direction)

# Function to validate operation date against code date
# Returns True if dates match or if date cannot be extracted from code
def validate_operation_date(operation_date, code):
    code_date = extract_date_from_code(code)
    if code_date:
        # Compare dates (allowing for small differences)
        return abs((operation_date - code_date).days) <= 1
    return True

if __name__ == '__main__':
    print('Operation classifiers module created successfully')