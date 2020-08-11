from collections import deque

graph = {}
graph["voce"] = ["alice", "bob", "claire"]
graph["bob"]   = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thomi", "jonny"]
graph["anuj"] = []
graph["peggy"] = ["voce"]
graph["thomi"] = []
graph["jonny"] = []


def is_seller(person):
    return person[-1] == 'm'

def search(name):
    queue_list = deque()
    queue_list += graph[name]
    visited = set()
    while queue_list:
        person = queue_list.popleft()
        if not person in person:
            if is_seller(person):
                print(person + "is a watermellon seller")
                return True
            else:
                queue_list += graph[person]
                visited.add(person)

    return False

print(search("voce"))