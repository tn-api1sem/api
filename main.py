import webbrowser
import uvicorn
import shutil
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.api import router


#Configure fastapi
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "null"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

#Open login file on start
url = os.path.realpath('src\web\login.html');
webbrowser.open(url,new=2)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
