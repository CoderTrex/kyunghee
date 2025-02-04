#include <cctype>
#include <fstream>
#include <iostream>
#include <cstring>

#include "StrType.h"
#include <cctype> 
#define _CRT_SECURE_NO_WARNINGS
using namespace std;

// Prototypes of auxiliary functions.
// Note: If skip is true, non-allowable leading characters are
//  skipped. If end-of-file is encountered while skipping
//  characters, the empty string is returned. If the number
//  of allowable characters exceeds MAX_CHARS, the rest are
//  read and discarded.

void GetAlphaNum(bool skip, char letters[], std::ifstream& inFile);
// Post: letters array contains only alphanumeric characters.

//void GetAlpha(bool skip, char letters[], std::ifstream& inFile);
// Post: letters array contains only alphabetic characters.

//void GetNonWhite(bool skip, char letters[], std::ifstream& inFile);
// Post: letters array contains only non-whitespace characters.

void GetTilNew(bool skip, char letters[], std::ifstream& inFile);
// Post: letters array contains everything up to newline character.

void StrType::GetStringFile(bool skip, InType charsAllowed, std::ifstream& inFile)
{
  switch (charsAllowed)
  {
    case ALPHA_NUM : GetAlphaNum(skip, letters, inFile); 
                     break;
//    case ALPHA     : GetAlpha(skip, letters, inFile);
//                     break;
//    case NON_WHITE : GetNonWhite(skip, letters, inFile);
 //                    break;
    case NOT_NEW   : GetTilNew(skip, letters, inFile);
                     break;
  }
}

void GetAlphaNum(bool skip, char letters[], std::ifstream& inFile)
// Post: If skip is true, non-alphanumeric letters are skipped.
//       Alphanumeric characters are read and stored until a
//       non-alphanumeric character is read or MAX_CHARS characters
//       have been stored. If the stream is not in the fail state,
//       the last character read was a non-alphanumeric character.
{
  using namespace std;
  char letter;
  int count = 0;

  if (skip)
  {// skip non-alphanumeric characters
    inFile.get(letter);
    while (!isalnum(letter) && inFile)
      inFile.get(letter);
  }
  else
    inFile.get(letter);
  if (!inFile || !isalnum(letter))
  // No legal character found; empty string returned.
    letters[0] = '\0';
  else
  {// Read and collect characters.
    do
    {
      letters[count] = letter;
      count++;
      inFile.get(letter);
    } while (isalnum(letter) && inFile && (count < MAX_CHARS));

    letters[count] = '\0';
    // Skip extra characters if necessary.
    if (count == MAX_CHARS && isalnum(letter))
      do
      {
        inFile.get(letter);
      } while (isalnum(letter) && inFile);
  }
      
}

void GetTilNew(bool skip, char letters[], std::ifstream& inFile)
// Post: If skip is true, newline characters are skipped.
//       All characters are read and stored until a newline
//       character is read or MAX_CHARS characters have been
//       stored. If the stream is not in the fail state, the
//       last character read was a newline character.
{
  using namespace std;
  char letter;
  int count = 0;
  if (skip)
  {// skip newlines.
      inFile.get(letter);
      while ((letter == '\n') &&inFile)
        inFile.get(letter);
  }
  else
    inFile.get(letter);
  if (!inFile || letter == '\n')
    letters[0] = '\0';
  else
  {// Read and collect characters.
    do
    {
      letters[count] = letter;
      count++;
      inFile.get(letter);
    } while ((letter != '\n') && inFile && (count < MAX_CHARS));

    letters[count] = '\0';
    // Skip extra characters if necessary.
    if (count == MAX_CHARS && letter != '\n')

    do
    {
      inFile.get(letter);
    } while ((letter != '\n') && inFile);
  }
}

void StrType::PrintToScreen(bool newLine)
// Post:  letters has been sent to the output stream.
{
  if (newLine)
  cout  << endl;
  cout  << letters;
}

void StrType::MakeEmpty()
{
  letters[0] = '\0';
}  

void StrType::PrintToFile(bool newLine, ofstream& outFile)
{
  if (newLine)
    outFile << endl;
    outFile << letters;
}
     
void StrType::CopyString(StrType& newString)
// Post: letters has been copied into newString.letters.
{ 
  strcpy(newString.letters, letters);
}

int StrType::LengthIs()
{
  return strlen(letters);
}

// A) strcmp 사용하여 함수 작성
RelationType StrType::ComparedTo(StrType &otherString) {
  int result = strcmp(this->letters, otherString.letters);

  if (result > 0) {
    return GREATER;
  } 
  else if (result < 0) {
    return LESS;
  } 
  else {
    return EQUAL;
  }
}

// B) 비교하는 부분을 직접 작성한다.
RelationType StrType::ComparedTo(StrType &otherString) {
  int idx;

  idx = 0;
  while (this->letters[idx] == otherString.letters[idx]) {
    if (this->letters[idx] == 0) {
      break;
    }
    idx++;
  }
  if (this->letters[idx] > otherString.letters[idx]) {
    return GREATER;
  } 
  else if (this->letters[idx] == otherString.letters[idx]) {
    return EQUAL;
  } 
  else {
    return LESS;
  }
}
