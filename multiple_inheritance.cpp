
#include <iostream>
using namespace std;

class Birds {
 public:
 Birds() {
 cout << "Birds are of two types" << endl;
 }
};

class Oviparous {
 public:
 Oviparous() {
 cout << "Oviparous birds lay eggs." << endl;
 }
};

class Sparrow: public Birds, public Oviparous {
public:
 void display() {
 cout << "I am a sparrow." << endl;
 }
};

int main() {
 Sparrow h1;
 h1.display();
 return 0;
}
