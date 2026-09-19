from sqlalchemy import Column, Integer, String, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class BankAccount(Base):
    __tablename__ = 'bank_accounts'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)  # Сбер, Т-Банк, Альфа-Банк
    account_number = Column(String(50), nullable=False)
    bank_name = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)


class BankStatement(Base):
    __tablename__ = 'bank_statements'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, nullable=False)
    statement_date = Column(DateTime)
    period_start = Column(DateTime)
    period_end = Column(DateTime)
    opening_balance = Column(Numeric(15, 2))
    closing_balance = Column(Numeric(15, 2))
    file_path = Column(String(255))
    imported_at = Column(DateTime, default=datetime.utcnow)
    is_processed = Column(Boolean, default=False)


class BankOperation(Base):
    __tablename__ = 'bank_operations'

    id = Column(Integer, primary_key=True)
    statement_id = Column(Integer, nullable=False)
    operation_date = Column(DateTime)
    operation_code = Column(String(20))
    description = Column(Text)
    amount = Column(Numeric(15, 2))
    direction = Column(String(10))  # 'income' or 'expense'
    opening_balance = Column(Numeric(15, 2))
    closing_balance = Column(Numeric(15, 2))
    account_number = Column(String(50))
    is_matched = Column(Boolean, default=False)
    matched_with_ipds_id = Column(Integer)  # ID операции в IPDS
    created_at = Column(DateTime, default=datetime.utcnow)


class InternalReport(Base):
    __tablename__ = 'internal_reports'

    id = Column(Integer, primary_key=True)
    statement_id = Column(Integer, nullable=False)
    report_number = Column(String(50))
    period_start = Column(DateTime)
    period_end = Column(DateTime)
    opening_balance = Column(Numeric(15, 2))
    total_income = Column(Numeric(15, 2))
    total_expense = Column(Numeric(15, 2))
    closing_balance = Column(Numeric(15, 2))
    file_path = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)