from datetime import datetime

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.utils.connection_manager import ConnectionManager

router = APIRouter()

manager = ConnectionManager()


@router.websocket('/')
async def messages(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            message = await websocket.receive_text()
            data = {
                'message': message,
                'created_at': datetime.now().strftime('%H:%M:%S'),
            }
            await manager.broadcast(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
