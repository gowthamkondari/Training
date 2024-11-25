
#include <iostream>
using namespace std;
class Birds {
 public:
 void type() {
 cout << "I'm an oviparous bird" << endl;
 }
};

class pigeon: public Birds{
 public:
 void name1() {
 cout << "I am a pigeon." << endl;
 }
};

class Sparrow: public Birds {
 public:
 void name2() {
 cout << "I am a sparrow." << endl;
 }
};

int main() {
 pigeon p; // object of pigeon class
 cout << "\npigeon Class:" << endl;
 p.type(); // base class method
 p.name1();

 Sparrow h; // object of Sparrow class
 cout << "\nSparrow Class:" << endl;
 h.type(); // base class method
 h.name2();

 return 0;
} 
