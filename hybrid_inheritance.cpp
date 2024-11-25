
#include <iostream>
using namespace std;

class Birds {
public:
 Birds() {
 cout << "Birds are of two types" << endl;
 }
};

class Oviparous : public Birds {
public:
 Oviparous() {
 cout << "Oviparous birds lay eggs." << endl;
 }
};

class Sparrow {
public:
 void name2() {
 cout << "I am a sparrow." << endl;
 }
};

class HybridSparrow : public Oviparous, public Sparrow {
public:
 void display() {
 name2();
 cout << "HybridSparrow class is a combination of Oviparous and Sparrow." << endl;
 }
};

int main() {
 HybridSparrow h1;
 h1.display();
 return 0;
}
