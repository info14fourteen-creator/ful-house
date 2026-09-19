# Database migration for bank statements
# This script creates tables for bank statements and operations

import os
import sys
from sqlalchemy import create_engine, text

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../')

# Create database connection
DATABASE_URL = os.environ.get('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is required")

engine = create_engine(DATABASE_URL)

# SQL for creating bank statements table
create_statements_table_sql = '''
CREATE TABLE IF NOT EXISTS bank_statements (
    id SERIAL PRIMARY KEY,
    bank_name VARCHAR(50) NOT NULL,
    account_number VARCHAR(50) NOT NULL,
    statement_period_start TIMESTAMP NOT NULL,
    statement_period_end TIMESTAMP NOT NULL,
    opening_balance NUMERIC(15, 2) NOT NULL,
    closing_balance NUMERIC(15, 2) NOT NULL,
    file_path VARCHAR(255),
    import_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_processed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''

# SQL for creating bank operations table
create_operations_table_sql = '''
CREATE TABLE IF NOT EXISTS bank_operations (
    id SERIAL PRIMARY KEY,
    statement_id INTEGER NOT NULL REFERENCES bank_statements(id),
    operation_date TIMESTAMP NOT NULL,
    operation_code VARCHAR(20),
    description TEXT,
    amount NUMERIC(15, 2) NOT NULL,
    direction VARCHAR(10) NOT NULL,
    opening_balance NUMERIC(15, 2),
    closing_balance NUMERIC(15, 2),
    account_requisites VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ipds_operation_id INTEGER,
    is_linked BOOLEAN DEFAULT FALSE,
    link_status VARCHAR(20)
);
'''

# Indexes for performance
create_indexes_sql = '''
CREATE INDEX IF NOT EXISTS idx_bank_statements_account ON bank_statements(account_number);
CREATE INDEX IF NOT EXISTS idx_bank_statements_period ON bank_statements(statement_period_start, statement_period_end);
CREATE INDEX IF NOT EXISTS idx_bank_operations_statement ON bank_operations(statement_id);
CREATE INDEX IF NOT EXISTS idx_bank_operations_date ON bank_operations(operation_date);
CREATE INDEX IF NOT EXISTS idx_bank_operations_code ON bank_operations(operation_code);
'''

def upgrade():
    with engine.connect() as conn:
        conn.execute(text(create_statements_table_sql))
        conn.execute(text(create_operations_table_sql))
        conn.execute(text(create_indexes_sql))
        conn.commit()

if __name__ == "__main__":
    upgrade()