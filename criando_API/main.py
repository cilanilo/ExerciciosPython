from fastapi import FastAPI # importar o FastAPI

app = FastAPI() # Criar uma distância para a classe FastAPI

@app.get("/") #Definir um decorador de rota, que será responsável por tratar as requisições que vão para a rota "/" usando o opreador get
def hello_root():  # Definir a função da rota
	return {"message": "Ola catulo"}

@app.get("/dobro/{numero}")
def read_item(numero: int):
    return {"dobro": numero * 2}