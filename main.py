import json

person = {
    "User1": {
        "name": "Musharraf",
        "username": "Musharraf@",
        "email": "musharraf@gmail.com",
        "phone": "909999088",
        "website": "wepPython.org",
    },
    "User2": {
        "name": "Alice",
        "username": "Alice",
        "email": "Ali@gmail.com",
        "phone": "909999088",
        "website": "wepPython.org",
    },
    "User3": {
        "name": "Jamshid",
        "username": "Alice",
        "email": "Ali@gmail.com",
        "phone": "909999088",
        "website": "wepPython.org",
    },
    "User4": {
        "name": "Akbar",
        "username": "Alice",
        "email": "Ali@gmail.com",
        "phone": "909999088",
        "website": "wepPython.org",
    }
}


# with open("person.json", "w") as JsonFile:
#     json.dump(person, JsonFile, indent=2)


def write_json(data):
    with open("person.json", "w") as JsonFile:
        json.dump(data, JsonFile, indent=2)
    return "file write data"

# print(write_json(person))
