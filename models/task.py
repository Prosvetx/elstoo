from pydantic import BaseModel


class Task(BaseModel):
    num: int
    timeout: int
