def sequenceEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "seq": item["seq"]
        }
