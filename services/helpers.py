import asyncio

from pymongo import MongoClient

from schemas.queue import queueEntity

from datetime import datetime

from schemas.sequence import sequenceEntity


def modification_task_sequence(connection: MongoClient, val: int) -> int:
    connection.local.sequence.update({"title": "queue_sequence"}, {"$inc": {"seq": val}}, True)
    sequence = sequenceEntity(connection.local.sequence.find_one({"title": "queue_sequence"}))
    return sequence["seq"]


async def task_in_work(queue_obj, connection):
        queue_entity = queueEntity(queue_obj)
        await asyncio.sleep(queue_entity["timeout"])
        connection.local.result.update({"title": "tasks_results"},
                                                    {"$push": {"list_results": queue_entity["num"]}}, True)
        modification_task_sequence(connection, -1)
        connection.local.queue.delete_one(queue_obj)


def insert_to_queue_task(item: dict, connection: MongoClient) -> str:
    seq_num = modification_task_sequence(connection, 1)
    return connection.local.queue.insert_one({
        "history_number": seq_num,
        "create_time": datetime.now().strftime('%H:%M:%S'),
        "num": item["num"],
        "timeout": item["timeout"]
        }).inserted_id
