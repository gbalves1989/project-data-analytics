from fastapi import APIRouter
from src.core.config import settings
from fastapi.requests import Request
from fastapi.responses import Response


home_controller = APIRouter()


@home_controller.get("/")
def get_home(request: Request) -> Response:
    context = {
        "request": request
    }

    return settings.TEMPLATES.TemplateResponse(
        "index.html", 
        context=context
    )
