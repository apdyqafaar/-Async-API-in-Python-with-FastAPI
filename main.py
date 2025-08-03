from fastapi import FastAPI  

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}



@app.get("/article/{id}")
def getArticles(id:int):
   return {"article":{id}}