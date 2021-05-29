from fastapi import APIRouter, BackgroundTasks

from config.db import db_connection

from models.task import Task

from schemas.task import tasksEntity, taskEntity

from bson import ObjectId

from services.helpers import insert_to_queue_task, task_in_work

task = APIRouter()


@task.get('/task')
async def get_all_tasks():
    with db_connection as conn:
        return tasksEntity(conn.local.task.find())


@task.get('/task/{id}')
async def get_task(id):
    with db_connection as conn:
        return taskEntity(conn.local.task.find_one({"_id": ObjectId(id)}))


@task.post('/task', status_code=201)
async def create_task(task: Task, background_tasks: BackgroundTasks):
    """Добавление задачи в список задач, очередь и выполнение в фоне"""
    with db_connection as conn:
        conn.local.task.insert_one(dict(task))
        inserted_id = insert_to_queue_task(dict(task), conn)
        inserted_queue_task = conn.local.queue.find_one({"_id": ObjectId(inserted_id)})
        background_tasks.add_task(task_in_work, inserted_queue_task, conn)

    return tasksEntity(db_connection.local.task.find())


@task.put('/task/{id}')
async def update_task(id, task: Task):
    with db_connection as conn:
        conn.local.task.find_one_and_update({"_id": id}, {
            "$set": dict(task)
            })
        return taskEntity(conn.local.task.find_one({"_id": ObjectId(id)}))


@task.delete('/task/{id}')
async def delete_task(id):
    return taskEntity(db_connection.local.task.find_one_and_delete({"_id": ObjectId(id)}))
