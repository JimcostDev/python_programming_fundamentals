
from fastapi import APIRouter, HTTPException, Query, status
from models import (
    Customer,
    CustomerCreate,
    CustomerPlan,
    CustomerUpdate,
    Plan,
)
from db import SessionDep
from sqlmodel import select

router = APIRouter(tags = ['customers'])

# crear customers
@router.post("/customers", 
          response_model=Customer,
          status_code=status.HTTP_201_CREATED)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

# listar customers
@router.get("/customers", 
         response_model=list[Customer])
async def list_customer(session: SessionDep):
    return session.exec(select(Customer)).all()

# obtener customer por id
@router.get("/customers/{customer_id}", 
         response_model=Customer)   
async def get_customer(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if  customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return customer

# eliminar customer por id
@router.delete("/customers/{customer_id}", 
         )
async def delete_customer(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if  customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    session.delete(customer)
    session.commit()
    return {"message": "Customer deleted"}

# actualizar customer por id
@router.patch("/customers/{customer_id}", 
         response_model=Customer,
         status_code=status.HTTP_202_ACCEPTED)
async def update_customer(customer_id: int, customer_data: CustomerUpdate, session: SessionDep):    
    customer = session.get(Customer, customer_id)
    if  customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    customer_data_dict = customer_data.model_dump(exclude_unset=True) # exclude_unset=True para excluir los valores que no se han enviado
    customer.sqlmodel_update(customer_data_dict)
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

# suscribir customer a plan
@router.post("/customers/{customer_id}/plans/{plan_id}")
async def subscribe_customer_to_plan(
    customer_id: int,
    plan_id: int,
    session: SessionDep,
    plan_status: bool = Query(..., description="Plan status")
):
    customer_db = session.get(Customer, customer_id)
    plan_db = session.get(Plan, plan_id)
    if not customer_db or not plan_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The customer or plan doesn't exist",
        )
    customer_plan_db = CustomerPlan(
        plan_id=plan_db.id, customer_id=customer_db.id, status=plan_status
    )

    session.add(customer_plan_db)
    session.commit()
    # Verificar si el objeto tiene un id generado antes de llamar a refresh
    print(customer_plan_db.id) 
    session.refresh(customer_plan_db)
    return customer_plan_db


@router.get("/customers/{customer_id}/plans")
async def subscribe_customer_to_plan(
    customer_id: int, session: SessionDep, plan_status: bool = Query()
):
    customer_db = session.get(Customer, customer_id)

    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    query = (
        select(CustomerPlan)
        .where(CustomerPlan.customer_id == customer_id)
        .where(CustomerPlan.status == plan_status)
    )
    plans = session.exec(query).all()
    return plans