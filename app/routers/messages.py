from datetime import datetime

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.utils.connection_manager import ConnectionManager

router = APIRouter()

manager = ConnectionManager()


@router.websocket('/{chat_id}')
async def messages(websocket: WebSocket, chat_id: str):
    await manager.connect(chat_id, websocket)

    try:
        while True:
            message = await websocket.receive_text()
            data = {
                'message': message,
                'created_at': datetime.now().strftime('%H:%M:%S'),
            }
            await manager.broadcast(chat_id, data)
    except WebSocketDisconnect:
        manager.disconnect(chat_id, websocket)
