from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from src.controllers.home_controller import home_controller
from src.controllers.clients_controller import clients_controller
from src.controllers.tickets_controller import tickets_controller


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/static", 
    StaticFiles(directory="static"), 
    name="static"
)

app.include_router(home_controller)
app.include_router(clients_controller)
app.include_router(tickets_controller)

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
    