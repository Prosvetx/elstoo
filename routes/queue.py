from fastapi import APIRouter

from config.db import db_connection

from schemas.queue import queuesEntity


queue = APIRouter()


@queue.get('/queue')
async def get_queues():
    with db_connection as conn:
        return queuesEntity(conn.local.queue.find().sort("create_time"))


