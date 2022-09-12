from xml.dom import IndexSizeErr
from QueType import *
from StackType import *

NULL_EDGE = 0


def index_is(vertices, vertex):
    index = 0
    while index < len(vertices) and vertex != vertices[index]:
        index += 1
    if not index < len(vertices):
        return -1
    else:
        return index


class GraphType:
    def __init__(self, maxV=50):
        self.numVertices = 0
        self.maxVertices = maxV
        self.vertices = [None] * maxV
        self.edges = [[NULL_EDGE] * maxV for _ in range(maxV)]
        self.marks = [None] * maxV

    def add_vertex(self, vertex):
        self.vertices[self.numVertices] = vertex
        for idx, _ in enumerate(self.edges):
            self.edges[self.numVertices][idx] = NULL_EDGE
            self.edges[idx][self.numVertices] = NULL_EDGE
        self.numVertices += 1

    def add_edge(self, fromVertex, toVertex, weight):
        row = index_is(self.vertices, fromVertex)
        col = index_is(self.vertices, toVertex)
        self.edges[row][col] = weight

    def weight_is(self, fromVertex, toVertex):
        row = index_is(self.vertices, fromVertex)
        col = index_is(self.vertices, toVertex)
        return self.edges[row][col]

    def get_to_vertices(self, vertex, adjVertices: QueType):
        from_index = index_is(self.vertices, vertex)
        for i in range(self.numVertices):
            if self.edges[from_index][i] != NULL_EDGE:
                adjVertices.enqueue(self.vertices[i])

    def clear_marks(self):
        for i in range(len(self.marks)):
            self.marks[i] = False

    def is_marked(self, vertex):
        i = index_is(self.vertices, vertex)
        return self.marks[i]

    def mark_vertex(self, vertex):
        i = index_is(self.vertices, vertex)
        self.marks[i] = True

    def delete_edge(self, fromVertex, toVertex):
        fromIndex = index_is(self.vertices, fromVertex)
        toIndex = index_is(self.vertices, toVertex)
        self.edges[fromIndex][toIndex] = NULL_EDGE
