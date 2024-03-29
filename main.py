from fastapi import FastAPI

app = FastAPI()
app.get("/")


async def show_login_form():
    return "login form"


app.post("login")


async def login():
    return {"message":"login Successfully"}
