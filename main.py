from fastapi import FastAPI,Form
from model import enrty
from fastapi.responses import HTMLResponse
app = FastAPI()
# Route to display the login form
@app.get("/", response_class=HTMLResponse)
async def show_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

#use to encrypt the pawd
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@app.post("/login/")
async def login(
    request: Request, email: EmailStr = Form(...), password: str = Form(...)
):

    # Establish a database session
    # Establish a database session
    with SessionLocal() as db:
        # Query the database for the user
        user = db.query(enrty).filter(enrty.email == email).first()

        # Check if user exists and password is correct
        if not user or not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Incorrect email or password")

    




async def login():
    return {"message":"login Successfully"}
@app.post("/signup")
asyn def signup(email: str = Form(...),
    password: str = Form(...),
    full_name: str = Form(...),
    pricing_tier: str = Form(...),):
    return {"message ":" Sign up Successfully"}
