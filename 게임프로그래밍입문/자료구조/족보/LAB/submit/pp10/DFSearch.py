from GraphType import *


def depth_first_search(graph, startVertex, endVertex):
    stack = StackType()
    vertexQ = QueType()
    path = QueType()
    found = False

    graph.clear_marks()
    stack.push(startVertex)
    print(startVertex)
    while stack.is_empty() == False and found == False:
        v = stack.top()
        stack.pop()
        if v == endVertex:
            found = True
        else:
            if graph.is_marked(v) == False:
                graph.mark_vertex(v)
                graph.get_to_vertices(v, vertexQ)
                while vertexQ.is_empty() == False:
                    item = vertexQ.dequeue()
                    path.enqueue(item)
                    if graph.is_marked(item) == False:
                        stack.push(item)

    if found is False:
        print("Path not found")
    else:
        while path.is_empty() == False:
            print(path.dequeue())
