
from typing import Optional, List
from pydantic import EmailStr, field_validator
from sqlmodel import SQLModel, Field, Relationship, Session, select
from db import engine

# ---- planes ----- #
class CustomerPlan(SQLModel, table=True, autoincrement=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id") # muchos a muchos
    plan_id: int = Field(foreign_key="plan.id") # muchos a muchos
    status: bool = Field(default=True) # true para activo, false para inactivo
    
class Plan(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    description: Optional[str] = None
    price: float
    customers: List["Customer"] = Relationship(back_populates="plans", link_model=CustomerPlan)

# ----- customers ----- #
class CustomerBase(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    email: EmailStr = Field(default=None, unique=True)
    age: int = Field(default=None)
    
    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        session = Session(engine)
        query = select(Customer).where(Customer.email == value)
        result = session.exec(query).first()
        if result:
            raise ValueError("This email is already registered")
        return value

class CustomerCreate(CustomerBase):
    pass

    class Config:
        json_schema_extra = {
            "example": {
                "name": "JimcostDev",
                "description": "Developer",
                "email": "email@test.com",
                "age": 25
            }
        }

class CustomerUpdate(CustomerBase):
    pass

class Customer(CustomerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # Relaciones - back_populates para indicar la relación
    invoices: List["Invoice"] = Relationship(back_populates="customer")
    transactions: List["Transaction"] = Relationship(back_populates="customer")
    plans: List[Plan] = Relationship(back_populates="customers", link_model=CustomerPlan)

# ----- transactions ----- #
class TransactionBase(SQLModel):
    amount: int
    description: str

class TransactionCreate(TransactionBase):
    customer_id: Optional[int] = Field(default=None, foreign_key="customer.id")
    
class Transaction(TransactionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: Optional[int] = Field(default=None, foreign_key="customer.id") # foreign_key="customer.id" para indicar la relación
    customer: Customer = Relationship(back_populates="transactions")
    
# Respuesta que incluirá las transacciones y la paginación
class PaginatedTransactionsResponse(SQLModel):
    total_count: int  # Total de elementos
    total_pages: int   # Total de páginas
    current_page: int  # Página actual
    limit: int         # Límite de elementos por página
    transactions: List["Transaction"]  # Transacciones en la página actual
    
# ----- invoices ----- #
class InvoiceBase(SQLModel):
    description: Optional[str] = None
    
class InvoiceCreate(InvoiceBase):
    customer_id: Optional[int] = Field(default=None, foreign_key="customer.id")

class Invoice(InvoiceBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: Optional[int] = Field(default=None, foreign_key="customer.id")
    customer: Optional[Customer] = Relationship(back_populates="invoices")

    @property
    def amount_total(self) -> int:
        return sum(transaction.amount for transaction in self.transactions)