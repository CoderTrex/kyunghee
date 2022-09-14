class MoneyType 
{
public:
  void  Initialize(long, long);
  // Initializes dollars and cents.
  long  DollarsAre() const;			
  // Returns dollars.
  long  CentsAre() const;			
  // Returns cents.
private:
  long  dollars;
  long  cents;
};

void  MoneyType::Initialize(long newDollars, long newCents)  
// Post: dollars is set to newDollars; cents is set to
//     newCents.
{
  dollars = newDollars;
  cents = newCents;
}

long  MoneyType::DollarsAre() const
// Post: Class member dollars is returned.
{
  return dollars;
}

long  MoneyType::CentsAre() const
// Post: Class member cents is returned.
{
  return cents;
}

