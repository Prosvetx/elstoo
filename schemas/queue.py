def queueEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "history_number": item["history_number"],
        "create_time": str(item["create_time"]),
        "num": item["num"],
        "timeout": item["timeout"]
        }


def queuesEntity(entity) -> list:
    return [queueEntity(item) for item in entity]

