def resultEntity(item) -> dict:
    return {
        "title": item["title"],
        "list_results": item["list_results"]
        }


def resultsEntity(entity):
    return [resultEntity(item) for item in entity]
