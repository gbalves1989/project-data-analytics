from fastapi import APIRouter
from src.data.tickets_data import tickets_df


tickets_controller = APIRouter()


@tickets_controller.get("/pedidos")
def get_tickets():
    return tickets_df.to_dict(orient="records")
