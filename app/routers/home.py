from fastapi import APIRouter, Request

from app.config import templates

router = APIRouter()


@router.get('/')
def home(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})
