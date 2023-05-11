from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_root():
	return {"message": "Ola catulo"}

@app.get("/dobro/{numero}")
def read_item(numero: int):
    return {"dobro": numero * 2}