from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.routes import router

app = FastAPI(
    title="API Agronegócio",
    description="API REST para gestão agrícola — fazendas, safras, colheitas, estoque e comercial.",
    version="1.0.0",
)

@app.middleware("http")
async def add_cors_headers(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")

@app.get("/", tags=["Status"])
def root():
    return {"status": "online", "docs": "/docs"}
