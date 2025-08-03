from collections import deque
'''graph = {}


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()

        if not person in searched:
            if person_is_seller(person):
                print(person + "mango seller found")
            else:
                search_queue += graph[person]
                search.append(person)
    return False
search("you") '''

graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anju", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anju": [],
    "peggy": [],
    "thom": [],
    "jonny": []




}


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()

        if person not in searched:
            if person_is_seller(person):
                print(person + " " "is a seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")
