import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel,Field
import joblib
from fastapi.responses import JSONResponse,HTMLResponse
from fastapi.middleware.cors import CORSMiddleware 


class DataCheck(BaseModel):
    email: str=Field(...,Description='Enter email',example='Congratulations! You won a free iPhone,click the link to claim now!')

model = joblib.load('spam-detector.pkl')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/',response_class=HTMLResponse)
def home():
    with open('index.html','r') as f:
        return f.read()

 

@app.post('/predict')
def chech_spam(m:DataCheck):
    

    result=model.predict(pd.DataFrame({
        'email':[m.email]
    }))[0]
    output= "SPAM Message" if result ==1 else 'Not Spam Message'
    return JSONResponse(status_code=200,content={'message':output})