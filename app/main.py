from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import home, chats, messages

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(home.router, prefix='')
app.include_router(chats.router, prefix='/chats')
app.include_router(messages.router, prefix='/messages')
