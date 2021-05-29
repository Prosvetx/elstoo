from typing import List, Optional

from pydantic import BaseModel


class Result(BaseModel):
    title: str
    list_results: Optional[List]
