#include <iostream>
using namespace std;


const int NULL_EDGE = 0;

template<class VertexType>
class GraphType{
public:
    GraphType(int);
    ~GraphType();
    void MakeEmpty();
    bool IsFull() const;
    
    // 파라미터 하나 주고 표현
    void AddVertex(VertexType); 
    
    // 버텍스와 버텍스를 주고, weight값 추가 -> edge 생성
    void AddEdge(VertexType, VertexType, int); 
    
    
    int WeightIs(VertexType, VertexType);
    
    // 버텍스를 하나 보내면 이웃 버텍스를 모두 queue에 넣어서 보내줘라
    void GetToVertices(VertexType, QueType<VertexType>&);
    void ClearMarks();
    void MarkVertex(VertexType);
    bool IsMarked(VertexType) const;

private:
    int numVertices;
    int maxVertices;

    // 버텍스들의 정보에 대해서
    VertexType *vertices;
    int **edge;
    bool *mark;
};

template<class VertexType>
GraphType<VertexType>::GraphType(int maxV)
{
    numVertices = 0;
    maxVertices = maxV;

    // 버텍스들을 1차원으로 만들어하기 때문에 생성함
    vertices = new VertexType[maxV];

    // edge의 가로값 똑같이 maxV의 크기 만큼 만들어 둠
    edges = new int[maxV];
    for (int i = 0; i < maxV; i++)
        // edge의 세로값도 똑같이 maxV의 크기 만큼 만들어 둠
        edges[i] = new int[maxV];
    marks = new bool[maxV]
}

template<class VerTexType>
GraphType<VerTexType>::~GraphType()
{
    delete[] vertices;
}

template<class VertexType>
void GraphType<VertexType>::AddVertex (VertexType vertex)
{
    vertices[numVertices] = vertex;
        for(int index = 0; index < numVertices; index++) {
        edges[numVertices][index] = NULL_EDGE;
        edges[index][numVertices] = NULL_EDGE;
    }
    numVertices++;
}

template<class VertexType>
void GraphType<VertexType>::AddEdge (VertexType fromVertex, VertexType toVertex, int weight)
{
    int row;
    int column;
    row = IndexIs(vertices, fromVertex);
    col = IndexIs(vertices, toVertex);
    edges[row][col] = weight;
}

template<class VertexType>
int GraphType<VertexType>::WeightIs (VertexType fromVertex, VertexType toVertex)
{
    int row;
    int column;

    // 각각의 가로 세로값을 가져오고 이와 관련된 index값을 찾아서 리턴함
    row = IndexIs(vertices, fromVertex);
    col = IndexIs(vertices, toVertex);
    return edges[row][col];
}