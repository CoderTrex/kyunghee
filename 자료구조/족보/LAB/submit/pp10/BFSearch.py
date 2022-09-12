from GraphType import *


def breadth_first_search(graph: GraphType, startVertex, endVertex):
    queue = QueType()
    vertexQ = QueType()
    found = False

    graph.clear_marks()
    queue.enqueue(startVertex)
    print(startVertex)
    while queue.is_empty() == False and found == False:
        v = queue.dequeue()
        if v == endVertex:
            found = True
        else:
            if graph.is_marked(v) == False:
                graph.mark_vertex(v)
                graph.get_to_vertices(v, vertexQ)
                while vertexQ.is_empty() == False:
                    item = vertexQ.dequeue()
                    print(item)
                    if graph.is_marked(item) == False:
                        queue.enqueue(item)

    if found == False:
        print("Path not found")
