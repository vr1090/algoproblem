class Graph:
    def __init__(self, adjList = {}):
        # the adjacency list is of type Dict[int,List[int]]
        self.adjList = adjList
        
# Parameters:
#  graph: Graph
#  root: int
# return type: None

# WARNING: There are no testcases for this problem, compare your solution with the one explained in the video

def dfs(graph, root):
    checked = []
    stack = []
    stack.append(root)
    
    while len(stack) > 0:
        node = stack.pop()
        print(node)

        if node not in checked:
            checked.append(node)
            for n in graph.adjList[node]:
                if n not in checked:
                    stack.append(n)
    
        
def should_return_1():
    checked = [2,3]
    node = [1,2,3]
    result = []

    for x in node:
        if x not in checked:
            result.append(x)
    
    return result

if __name__ == "__main__":
    print(should_return_1())