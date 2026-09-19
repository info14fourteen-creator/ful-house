from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Numeric, Text, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class BankStatement(Base):
    __tablename__ = 'bank_statements'

    id = Column(Integer, primary_key=True)
    bank_name = Column(String(50), nullable=False)  # 'Alfa-Bank', 'Sber', 'T-Bank'
    account_number = Column(String(50), nullable=False)
    statement_period_start = Column(DateTime, nullable=False)
    statement_period_end = Column(DateTime, nullable=False)
    opening_balance = Column(Numeric(15, 2), nullable=False)
    closing_balance = Column(Numeric(15, 2), nullable=False)
    file_path = Column(String(255))
    import_date = Column(DateTime, default=datetime.utcnow)
    is_processed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship with operations
    operations = relationship("BankOperation", back_populates="statement")


class BankOperation(Base):
    __tablename__ = 'bank_operations'

    id = Column(Integer, primary_key=True)
    statement_id = Column(Integer, ForeignKey('bank_statements.id'), nullable=False)
    operation_date = Column(DateTime, nullable=False)
    operation_code = Column(String(20))
    description = Column(Text)
    amount = Column(Numeric(15, 2), nullable=False)
    direction = Column(String(10), nullable=False)  # 'income' or 'expense'
    opening_balance = Column(Numeric(15, 2))
    closing_balance = Column(Numeric(15, 2))
    account_requisites = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship with statement
    statement = relationship("BankStatement", back_populates="operations")

    # For linking with IPDS operations
    ipds_operation_id = Column(Integer)
    is_linked = Column(Boolean, default=False)
    link_status = Column(String(20))  # 'linked', 'unlinked', 'partial'
