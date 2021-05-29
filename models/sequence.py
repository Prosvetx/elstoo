from pydantic import BaseModel


class Sequence(BaseModel):
    title: str
    seq: 0