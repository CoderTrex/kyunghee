// ItemType.h  contains the specifications for the data for the real 
//  estate manipulation program.


const int MAX_ITEMS = 25; 
#include <fstream> 
#include "StrTypeAugmented.h"   // Gain access to String ADT.

enum RelationType {LESS, EQUAL, GREATER};
class HouseType
{ 
public:
  void GetFromFile(std::ifstream&); 
  void WriteToFile(std::ofstream&); 
  void GetFromUser(); 
  void PrintHouseToScreen(); 
  void GetNameFromUser(); 
  void PrintNameToScreen(); 
  RelationType ComparedTo(HouseType); 
  bool operator==(const HouseType& house);
  bool operator<(const HouseType& house);

private:
  StrType lastName; 
  StrType firstName; 
  StrType address; 
  float price; 
  int squareFeet; 
  int bedRooms; 
  int bathroom;
}; 

// Make ItemType an alias for HouseType. 
typedef HouseType ItemType;


// ItemType.cpp is the implementation file for data for the real 
//  estate manipulation program.
