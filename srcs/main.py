from fastapi import FastAPI

app = FastAPI(
    # title="Weather API", # TODO Check this part
    # description="Simple API showing weather in France",
    # version="0.0.1",
    # docs_url="/docs",  # Modifier l'URL de Swagger UI
    # redoc_url="/redocumentation" 
)


@app.get("/")
def read_root():
    return {"message": "Hello"}
