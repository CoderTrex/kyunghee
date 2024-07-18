#include "GraphType.h"
#include <iostream>

int main()
{
	GraphType<char *> g;

	g.AddVertex("dog");
	g.AddVertex("cat");
	g.AddVertex("animal");
	g.AddVertex("vertebrate");
	g.AddVertex("oyster");
	g.AddVertex("shellfish");
	g.AddVertex("invertebrate");
	g.AddVertex("crab");
	g.AddVertex("poodle");
	g.AddVertex("monkey");
	g.AddVertex("banana");
	g.AddVertex("dalmatian");
	g.AddVertex("dachshund");

	g.AddEdge("vertebrate", "animal", 10);
	g.AddEdge("invertebrate", "animal", 20);
	g.AddEdge("dog", "vertebrate", 30);
	g.AddEdge("cat", "vertebrate", 40);
	g.AddEdge("monkey", "vertebrate", 50);
	g.AddEdge("shellfish", "invertebrate", 60);
	g.AddEdge("crab", "shellfish", 70);
	g.AddEdge("oyster", "invertebrate", 80);
	g.AddEdge("poodle", "dog", 90);
	g.AddEdge("dalmatian", "dog", 100);
	g.AddEdge("dachshund", "dog", 110);

	std::cout << "Weight of 'vertebrate to animal' is " << g.WeightIs("vertebrate", "animal") << std::endl;
	std::cout << "Weight of 'poodle to dog' is " << g.WeightIs("poodle", "dog") << std::endl;

	g.DeleteEdge("poodle", "dog");
	std::cout << "Weight of 'poodle to dog' is " << g.WeightIs("poodle", "dog") << std::endl;
	std::cout << std::endl
			  << "GetToVertices(dog, queue)" << std::endl;

	QueType<char *> queue;
	g.GetToVertices("dog", queue);

	while (!queue.IsEmpty())
	{
		char *item;
		queue.Dequeue(item);
		std::cout << item << std::endl;
	}
}
