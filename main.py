from fastapi import FastAPI,Form, HTTPException

from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from mode import JobSubmission,enrty
app = FastAPI()
# Route to display the login form
@app.get("/", response_class=HTMLResponse)
async def show_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
#  Pydantic model to represent the response from the external AI service
class AIResponse(BaseModel):
    status_code: int
    response_json: Dict[str, Any]



PRICING_TIERS = {"basic": 100, "standard": 250, "premium": 500}
templates = Jinja2Templates(directory="templates")
Base.metadata.create_all(engine)
SECRET_KEY = " donotworkingsodoitagain "
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
app.mount(
    "/static", StaticFiles(directory="D:/PYTHONAPI/project/templates"), name="static"
)

logging.basicConfig(filename='server.log', level=logging.DEBUG)

#use to encrypt the pawd
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


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
        
    credits = PRICING_TIERS[pricing_tier]
    hashed_password = pwd_context.hash(password)
    new_user = enrty(
        email=email, password=hashed_password, full_name=full_name, credits=credits
    )
    db = SessionLocal()
    db.add(new_user)
    db.commit()
    db.close()
    return {"message ":" Sign up Successfully"}

# Route to serve the index.html file from the root path
@app.get("/client", response_class=HTMLResponse)
async def get_index():
    return FileResponse("D:/PYTHONAPI/project/templates/client.html")

