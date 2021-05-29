from fastapi import FastAPI

from routes.queue import queue
from routes.result import result
from routes.task import task

app = FastAPI()
app.include_router(task)
app.include_router(queue)
app.include_router(result)


