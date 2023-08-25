from collections import defaultdict


app_db = None

def get_fake_db() -> dict:
    global app_db
    if app_db == None:
        app_db = defaultdict(list)
    return app_db
