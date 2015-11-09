# Compatible-meetings
Find all the sets of compatible meetings (cliques) in a network: python, Bron-Kerbosch

Given a list of the start and stop times of some meetings, this code spits back the combinations of meeetings that don't overlap.

Consider a group of meetings. Say that meetings are nodes of a network, and two nodes are connected if the meeting times don't overlap. In this framework, a set of mutually non-overlapping meetings is a clique, so we want to find all the cliques. This is a well documented problem, and can be solved using the Bron-Kerbosch algorithm. 

First, setup the netowrk. If there are `n` meetings, the network will be represented here as an `n`-by-`n` matrix with elements denoting connections or no connections between meetings `i` and `j` by `1` and `0`. 

```
graph=[(meets[i][1]<=meets[j][0] or meets[i][0]>=meets[j][1])*1 for i in range(L) for j in range(L)]
    graph=zip(*[iter(graph)]*L)
```

The code is to implement the Bron-Kerbosch algorithm is based off a.u.r.'s code found [here](http://stackoverflow.com/questions/13904636/implementing-bron-kerbosch-algorithm-in-python).
