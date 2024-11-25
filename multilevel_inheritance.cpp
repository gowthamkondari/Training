
#include <iostream>
using namespace std; 
class base
{ 
 public: 
 void display() 
 { 
 cout << "Class base1" << endl; 
 } 
}; 
class derived1 : public base
{ 
 public: 
 void print() 
 { 
 cout << "This is the 1st derived class" << endl; 
 } 
}; 
class derived2: public derived1
{ 
 void view() 
 { 
 cout << "This is the 2nd derived class" << endl; 
 } 
}; 
int main() 
{ 
 derived2 d; 
 d.display();
 d.print();
 d.view(); 
 return 0; 
} 
