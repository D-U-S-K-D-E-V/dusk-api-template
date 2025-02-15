from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.example import routes_example
app = FastAPI()

origins = [
    "http://localhost<port_num>",
    "http://<service>:<port_num>"
    "https://<service>:<port_num>",
    "https://<domain>.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_example.router)

@app.get("/")
async def root():
    return {"message": "root"}