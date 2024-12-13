
from models import Invoice
from fastapi import APIRouter

router = APIRouter(tags = ['invoices'])

@router.post("/invoices",
          tags=['invoices'],
          response_model=Invoice)
async def create_invoice(invoice_data: Invoice):
    breakpoint()
    return invoice_data