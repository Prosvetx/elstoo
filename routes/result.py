from fastapi import APIRouter

from config.db import db_connection
from schemas.result import resultsEntity

result = APIRouter()


@result.get('/result')
async def get_result():
    with db_connection as conn:
        return resultsEntity(conn.local.result.find())
