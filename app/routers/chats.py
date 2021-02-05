from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from starlette import status

from app.config import templates
from app.utils.funcs import generate_chat_id

router = APIRouter()


@router.get('/new')
def create_chat():
    chat_id = generate_chat_id()
    url = f'/chats/{chat_id}'
    return RedirectResponse(url)


@router.post('/connect')
def connect_to_chat(chat_id: str = Form(...)):
    url = f'/chats/{chat_id}'
    return RedirectResponse(url, status_code=status.HTTP_303_SEE_OTHER)


@router.get('/{chat_id}')
def chat(request: Request, chat_id: str):
    context = {'request': request, 'chat_id': chat_id}
    return templates.TemplateResponse('chat.html', context)
