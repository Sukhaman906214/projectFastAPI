from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
# Route to display the login form
@app.get("/", response_class=HTMLResponse)
async def show_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

#use to encrypt the pawd
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


app.post("login")


async def login():
    return {"message":"login Successfully"}
@app.post("/signup")
asyn def signup():
    return {"message ":" Sign up Successfully"}
