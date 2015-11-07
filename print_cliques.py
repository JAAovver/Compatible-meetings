def N(vertex,graph): #give neighbors
    l= [i for i in range(len(graph[vertex])) if graph[vertex][i]]
    return l 
def bronk(r,p,x,graph): #Bron-Kerbosch algorithm
    if not any((x,p)):
        print r
    for vertex in p[:]:
        r_new = r[:]
        r_new.append(vertex)
        p_new = [val for val in p if val in N(vertex,graph)]
        x_new = [val for val in x if val in N(vertex,graph)]
        bronk(r_new,p_new,x_new,graph)
        p.remove(vertex)
        x.append(vertex)
def main():
    meets = [[1,2],[3,4],[2,2.5],[3,6],[1,4],[7,8]] #example meeting list
    L = len(meets)
    graph=[(meets[i][1]<=meets[j][0] or meets[i][0]>=meets[j][1])*1 for i in range(L) for j in range(L)]
    graph=zip(*[iter(graph)]*L)
    
    bronk([],range(L),[],graph)
if __name__ == '__main__':
    main()
