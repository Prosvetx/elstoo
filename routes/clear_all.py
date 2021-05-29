from fastapi import APIRouter
from config.db import db_connection

clear = APIRouter()


@clear.get('/clear_all')
async def clear_all():
    with db_connection as conn:
        conn.local.queue.remove({})
        conn.local.task.remove({})
        conn.local.result.remove({})
        conn.local.sequence.remove({})
    return None
