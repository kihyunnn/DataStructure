class UndiretedGraph:
    """무방향 그래프"""
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, v1, v2):
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)
        # v1과 v2를 연결 [Hint: 무방향 그래프이므로 양방향 추가]
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")

    def to_adjacency_matrix(self):
        """인접 행렬 출력"""
        vertices = sorted(self.adj_list.keys())
        index_map = {v: i for i, v in enumerate(vertices)}
        n = len(vertices)
        matrix = [[0] * n for _ in range(n)]

        for u in self.adj_list:
            for v in self.adj_list[u]:
                i, j = index_map[u], index_map[v]
                # 인접 행렬에서 (i,j), (j,i)에 1을 할당
                matrix[i][j] = 1
                matrix[j][i] = 1

        print("\n[Adjacency Matrix]")
        print(" ", " ".join(vertices))
        for i, row in enumerate(matrix):
            print(vertices[i], " ".join(str(x) for x in row))

        return matrix

class DiretedGraph:
    """방향 그래프"""
    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v, weight=1):
        self.add_vertex(u)
        self.add_vertex(v)
        # u와 v를 연결 [Hint: 방향성은 u → v 이며, 간선에 가중치 포함]
        self.adj_list[u].append((v, weight))

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")

    def to_adjacency_matrix(self):
        """인접 행렬 출력"""
        vertices = sorted(self.adj_list.keys())
        index_map = {v: i for i, v in enumerate(vertices)}
        n = len(vertices)
        matrix = [[0] * n for _ in range(n)]

        for u in self.adj_list:
            for v, weight in self.adj_list[u]:
                # u → v 방향에 가중치 설정 (matrix[i][j] = weight)
                i, j = index_map[u], index_map[v] 
                matrix[i][j] = weight

        print("\n[Adjacency Matrix]")
        print(" ", " ".join(vertices))
        for i, row in enumerate(matrix):
            print(vertices[i], " ".join(str(x) for x in row))

        return matrix