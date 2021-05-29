def taskEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "num": item["num"],
        "timeout": item["timeout"]
        }


def tasksEntity(entity) -> list:
    return [taskEntity(item) for item in entity]

