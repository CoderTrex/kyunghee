from GraphType import *
from BFSearch import *
from DFSearch import *

if __name__ == '__main__':
    graph = GraphType()

    graph.add_vertex("dog")
    graph.add_vertex("cat")
    graph.add_vertex("animal")
    graph.add_vertex("vertebrate")
    graph.add_vertex("oyster")
    graph.add_vertex("shellfish")
    graph.add_vertex("invertebrate")
    graph.add_vertex("crab")
    graph.add_vertex("poodle")
    graph.add_vertex("monkey")
    graph.add_vertex("banana")
    graph.add_vertex("dalmatian")
    graph.add_vertex("dachshund")

    graph.add_edge("vertebrate", "animal", 10)
    graph.add_edge("invertebrate", "animal", 20)
    graph.add_edge("dog", "vertebrate", 30)
    graph.add_edge("cat", "vertebrate", 40)
    graph.add_edge("monkey", "vertebrate", 50)
    graph.add_edge("shellfish", "invertebrate", 80)
    graph.add_edge("crab", "shellfish", 70)
    graph.add_edge("oyster", "invertebrate", 80)
    graph.add_edge("poodle", "dog", 90)
    graph.add_edge("dalmatian", "dog", 100)
    graph.add_edge("dachshund", "dog", 110)

    print()
    print("DepthFirstSearch(graph, \"dalmatian\", \"animal\")")
    depth_first_search(graph, "dalmatian", "animal")

    print()
    print("BreadthFirstSearch(graph, \"dalmatian\", \"animal\")")
    breadth_first_search(graph, "dalmatian", "animal")
