import uvicorn
import shutil
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.api import router
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask, render_template, request

# Backup on start
files = ['test.json', 'profiles.json', 'rates.json', 'sprints.json', 'team_sprint.json',
         'teams.json', 'user_profile.json', 'user_rate.json', 'user_team.json', 'users.json']
fileDir = os.path.dirname(os.path.realpath('__file__'))
for f in files:
    src = fileDir + "/database/"+f
    dst = fileDir + "/database/backup_"+f
    shutil.copy(src, dst)


app = FastAPI()
flask_app = Flask(__name__)
# Mount Flask on FastAPI
app.mount("/api/v1/autenticacao", WSGIMiddleware(flask_app))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@flask_app.get('/')
def login_page():
    return render_template('login.html')


"""
CHAMANDO ASSIM DEU CERTO
@flask_app.route('/', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        return "Email: " + email + " <br> " + "Password: " + password

"""


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
