def needs_human(query, docs):
    query = query.lower()

    if "refund" in query:
        return True

    if "cancel account" in query:
        return True

    if len(docs) == 0:
        return True

    return False