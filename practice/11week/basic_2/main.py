from queue import Queue    

'''
    Basic 2: 깊이 우선 탐색 <DFS>와 너비 우선 탐색(BFS) 구현하고, 
             DFS를 이용한 신장 트리를 구현하여라.
             
             - 아래 보이는 출력이 될 수 있도록, 각각의 탐색 함수들을 완성하여라.
             
'''

''' 깊이 우선 탐색 (DFS)'''
def DFS(vtx, adj, s, visited) :
    print(vtx[s], end=' ')          
    visited[s] = ### block ###
    for v in range(len(vtx)) :      
        if adj[s][v] != 0 :         
            if visited[v]==False:   
                DFS(### block ###)

''' DFS를 이용한 신장트리(인접행렬 방식) '''   
def ST_DFS(vtx, adj, s, visited) :
    visited[s] = ### block ###               
    for v in range(len(vtx)) :     
        if adj[s][v] != 0 :     
            if visited[v]==False:  
                print("(", vtx[s], vtx[v], ")", end=' ') 
                ST_DFS(### block ###)

''' 너비 우선 탐색 (DFS)'''
def BFS(vtx, aList, s):
    n = len(vtx)                        
    visited = ### block ###                
    Q = Queue()                         
    Q.put(s)                            
    visited[s] = ### block ###                   
    while not Q.empty() :
        s = Q.get()                     
        print(vtx[s], end=' ')          
        for v in aList[s] :             
            if ### block ### :      
                Q.put(v)                
                visited[v] = True  
                               
def main() :
    vtx = ['U','V','W','X','Y']  
    edge= [[0,  1,  1,  0,  0],     
           [1,  0,  1,  1,  0],
           [1,  1,  0,  0,  1],
           [0,  1,  0,  0,  0],
           [0,  0,  1,  0,  0]]
    aList=[[1, 2],              
           [0, 2, 3],   
           [0, 1, 4],
           [1],
           [2]]
        
    print('DFS (출발: U): ', end="")
    DFS(vtx, edge, 0, [False]*len(vtx))
    print()
    print('ST_DFS_AM    : ', end="")
    ST_DFS(vtx, edge, 0, [False]*len(vtx))
    print()
    print('BFS (출발: U): ', end="")
    BFS(vtx, aList, 0)
    print()

if __name__ == "__main__":
    main()