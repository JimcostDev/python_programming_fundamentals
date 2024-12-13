from fastapi import APIRouter, HTTPException, Query, status

from models import Customer, Transaction, TransactionCreate, PaginatedTransactionsResponse
from db import SessionDep
from sqlmodel import select

router = APIRouter(tags = ['transactions'])

@router.post("/transactions", status_code=status.HTTP_201_CREATED)
async def create_transation(transaction_data: TransactionCreate, session: SessionDep):
    transaction_data_dict = transaction_data.model_dump()
    customer = session.get(Customer, transaction_data_dict.get("customer_id"))
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    
    transaction = Transaction.model_validate(transaction_data_dict)
    session.add(transaction)
    session.commit()
    session.refresh(transaction)
    return transaction

@router.get("/transactions", response_model=PaginatedTransactionsResponse)
async def list_transactions(
    session: SessionDep,
    skip: int = Query(0, description="Registros a omitir"),
    limit: int = Query(10, description="Número de registros por página"),
):
    # Consulta de transacciones con paginación
    query = select(Transaction).offset(skip).limit(limit)
    transactions = session.exec(query).all()

    # Obtener el total de registros en la base de datos (sin paginación)
    total_count_query = select(Transaction)
    total_count = len(session.exec(total_count_query).all())  # Contamos los registros

    # Calcular el total de páginas
    total_pages = (total_count + limit - 1) // limit  # Redondear hacia arriba

    # Crear la respuesta paginada
    response = PaginatedTransactionsResponse(
        total_count=total_count,
        total_pages=total_pages,
        current_page=(skip // limit) + 1,  # Calcular la página actual
        limit=limit,
        transactions=transactions
    )

    return response