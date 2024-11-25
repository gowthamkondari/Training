#include <iostream>

using namespace std;

class TestAbstraction {
    private: string x, y;

    public:

        // method to set values of 
        // private members
        void set(string a, string b) {
            x = a;
            y = b;
        }
    //printing values  
    void print() {
        cout << "x = " << x << endl;
        cout << "y = " << y << endl;
    }
};

int main() {
    // object of TestAbstraction
    TestAbstraction t1;
    t1.set("Scaler", "Academy");
    t1.print();

    return 0;
}


/*    Explanation:

In this example, abstraction is achieved using classes and access specifiers.
TestAbstraction class is declared with string x, y as its private members, which means we could not access these strings outside the class.
void set(string a, string b) and void print() are declared public members' functions.
TestAbstraction t1 creates the object of TestAbstraction class.
t1.set("Scaler", "Academy"); sets the private member's string x as Scaler, y as Academy. These implementation details are hidden from the user.
t1.print() prints the members of t1 object.  */
