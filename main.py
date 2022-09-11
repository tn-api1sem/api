import uvicorn, shutil, os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.api import router as api_router


#Backup on start
files = ["test.json"]
fileDir = os.path.dirname(os.path.realpath('__file__'))
for f in files:
    src = fileDir + "\\database\\"+f
    dst = fileDir + "\\database\\backup_"+f
    shutil.copy(src, dst)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

