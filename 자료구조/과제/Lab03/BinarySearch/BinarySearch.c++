#include <iostream>
using namespace std;

int  BinarySearch(int array[], int sizeOfArray, int value){

}


void SortedType::RetrieveItem ( ItemType& item, bool& found )
// ASSUMES info ARRAY SORTED IN ASCENDING ORDER
{ 
    int midPoint ;
    int first = 0;
    int last = length - 1 ;
    bool moreToSearch = ( first <= last ) ;
    found = false ;
    while ( moreToSearch && !found )
    { 
        midPoint = ( first + last ) / 2 ;
        switch ( item.ComparedTo( info [ midPoint ] ) )
        {
            case LESS:
                last = midPoint - 1 ;
                moreToSearch = ( first <= last ) ;
                break ;
            case GREATER : first = midPoint + 1 ;
                moreToSearch = ( first <= last ) ;
                break ;
            case EQUAL : found = true ;
                item = info[ midPoint ] ;
                break ;
        }
    }
}