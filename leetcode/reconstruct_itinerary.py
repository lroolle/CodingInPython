"""LeetCode 332. Reconstruct Itinerary

> Given a list of airline tickets represented by pairs of departure and
arrival airports [from, to], reconstruct the itinerary in order. All of the
tickets belong to a man who departs from JFK. Thus, the itinerary must begin
with JFK.

- Note:

> 1. If there are multiple valid itineraries, you should return the itinerary
that has the smallest lexical order when read as a single string. For example,
the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
2. All airports are represented by three capital letters (IATA code).
3. You may assume all tickets form at least one valid itinerary.

- Example 1:

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].

- Example 2:

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL",
"SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But
it is larger in lexical order.

"""
import collections


def find_itinerary(tickets):
    start = ['JFK', 'ZZZ']
    for i in tickets:
        if i[0] == start[0] and i[1] < start[1]:
            start[1] = i[1]
    itinerary = start
    tickets.remove(start)
    for j in range(len(tickets)):
        for x in tickets:
            if x[0] == start[1]:
                itinerary.append(x[1])
                start = x
                tickets.remove(x)

    return itinerary


def find_itinerary2(tickets):
    routes = collections.defaultdict(list)
    for s, e in tickets:
        routes[s].append(e)

    def solve(start):
        left, right = [], []
        for end in sorted(routes[start]):
            if end not in routes[start]:
                continue
            print(end)
            routes[start].remove(end)
            subroutes = solve(end)
            if start in subroutes:
                left += subroutes
            else:
                right += subroutes
        return [start] + left + right

    return solve("JFK")


def find_itinerary3(tickets):
    routes = collections.defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        routes[a] += b,
    print(routes)
    route = []

    def visit(airport):
        while routes[airport]:
            visit(routes[airport].pop())
        route.append(airport)
        print(route)
    visit('JFK')
    return route[::-1]


print(find_itinerary3(
    [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL",
                                                                      "SFO"]]))
