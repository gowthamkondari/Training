// Program to calculate the area of a rectangle
#include <iostream>
using namespace std;

class Rectangle {
  public:
    // Variables required for area calculation
    int length;
    int breadth;

    // Constructor to initialize variables
    Rectangle(int len, int brth) : length(len), breadth(brth) {}

    // Function to calculate area
    int getArea() {
      return length * breadth;
    }
};

int main() {
  // Create object of Rectangle class
  Rectangle rect(8, 6);

  // Call getArea() function
  cout << "Area = " << rect.getArea();

  return 0;
}


/* In the above example, we are calculating the area of a rectangle.

To calculate an area, we need two variables: length and breadth and a function: getArea(). 

Hence, we bundled these variables and function inside a single class named Rectangle.

Here, the variables and functions can be accessed from other classes as well. Hence, this is not data hiding.

This is only encapsulation. We are just keeping similar codes together. */



