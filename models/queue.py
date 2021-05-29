from pydantic import BaseModel


class Queue(BaseModel):
    history_number: int
    create_time: str
    num: int
    timeout: int