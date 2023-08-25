from collections import defaultdict


def to_camel(string: str) -> str:
    string_split = string.split("_")
    return string_split[0] + "".join(word.capitalize() for word in string_split[1:])

def get_fake_db():
    global app_db
    if app_db == None:
        app_db = defaultdict(list)
    return app_db