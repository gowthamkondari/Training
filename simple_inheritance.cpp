#include <iostream>
class Animal {
public:
  void eat() {
    std::cout << "Animal is eating." << std::endl;
  }
};
class Dog : public Animal {
public:
  void bark() {
    std::cout << "Dog is barking." << std::endl;
  }
};
int main() {
  Dog dog;
  dog.eat(); // Animal is eating.
  dog.bark(); // Dog is barking.
  return 0;
}



/*

The Dog class in this example in C++ Compiler derives from the Animal class. 
This means that the Dog class includes all of the members of the Animal class, as well as any extra 
members defined by it. 
The Dog class defines an additional member method called bark() in this situation. 
The main() function creates a Dog class object and calls its eat() and bark() member functions.    */
