INF = 99999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 (adjacency matrix) 표현
#              0 (node)
#             / \
#     (edge) 7   5 (edge)
#           /     \
#   (node) 1       2 (node)


graph = [
    [0, 7, 5],   # node 0
    [7, 0, INF], # node 1
    [5, INF, 0]  # node 2
]

print(graph)