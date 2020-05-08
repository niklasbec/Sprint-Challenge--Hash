#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashTable = {}
    route = []

    for i in range(length):
        hashTable[tickets[i].source] = tickets[i].destination
        i = i+1

    current = hashTable["NONE"]
    while current != "NONE":
        route.append(current)
        current = hashTable[current]
    route.append(current)
    return route


t1 = Ticket("PIT", "ORD")
t2 = Ticket("XNA", "SAP")
t3 = Ticket("SFO", "BHM")
t4 = Ticket("FLG", "XNA")
t5 = Ticket("NONE", "LAX")
t6 = Ticket("LAX", "SFO")
t7 = Ticket("SAP", "SLC")
t8 = Ticket("ORD", "NONE")
t9 = Ticket("SLC", "PIT")
t10 = Ticket("BHM", "FLG")

tripTickets = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]

print("RESULT", reconstruct_trip(tripTickets, len(tripTickets)))