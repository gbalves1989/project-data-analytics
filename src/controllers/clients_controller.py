from fastapi import APIRouter
from src.data.clients_data import clients_df


clients_controller = APIRouter()


@clients_controller.get("/clientes")
def get_clients():
    return clients_df.to_dict(orient="records")
