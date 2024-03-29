from fastapi import FastAPI

app = FastAPI()
@app.get("/", response_class=HTMLResponse)
async def show_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


app.post("login")


async def login():
    return {"message":"login Successfully"}
