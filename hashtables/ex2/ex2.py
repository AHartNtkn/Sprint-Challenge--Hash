#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = {}
    route = [None] * length

    for t in tickets:
        ht[t.source] = t.destination

    current_city = ht["NONE"]
    i = 0
    while current_city != "NONE":
        route[i] = current_city
        current_city = ht[current_city]
        i += 1
    route[i] = "NONE"
    
    return route
