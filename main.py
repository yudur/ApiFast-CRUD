from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def create_user():
    return {"Hello": "World"}

def read_user():
    pass

def update_user():
    pass

def delete_user():
    pass