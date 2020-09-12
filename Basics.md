#### Storage Classes 
_A storage class defines the scope (visibility) and life-time of variables and/or functions within a C++ Program. These specifiers precede the type that they modify._
- **Auto** - This is the default storage class for all local variables. It is the same whether explicitly defined or not.
- **Register** - The register storage class is used to define local variables that should be stored in a register instead of RAM. This means that the variable has a maximum size equal to the register size (usually one word) and can't have the unary '&' operator applied to it (as it does not have a memory location). The register should only be used for variables that require quick access such as counters. It should also be noted that defining 'register' does not mean that the variable will be stored in a register. It means that it MIGHT be stored in a register depending on hardware and implementation restrictions.
- **Static** - The static storage class instructs the compiler to keep a local variable in existence during the life-time of the program instead of creating and destroying it each time it comes into and goes out of scope. Therefore, making local variables static allows them to maintain their values between function calls.
The static modifier may also be applied to global variables. When this is done, it causes that variable's scope to be restricted to the file in which it is declared.In C++, when static is used on a class data member, it causes only one copy of that member to be shared by all objects of its class.
- **Extern** - The extern storage class is used to give a reference of a global variable that is visible to ALL the program files. When you use 'extern' the variable cannot be initialized as all it does is point the variable name at a storage location that has been previously defined.When you have multiple files and you define a global variable or function, which will be used in other files also, then extern will be used in another file to give reference of defined variable or function. Just for understanding extern is used to declare a global variable or function in another file.The extern modifier is most commonly used when there are two or more files sharing the same global variables or functions
Example- 
```
\\ File1
#include <iostream>
int count ;
extern void write_extern();
 
main() {
   count = 5;
   write_extern();
}
```
```
\\File2
#include <iostream>

extern int count;

void write_extern(void) {
   std::cout << "Count is " << count << std::endl;
}
```
Complie them together
`$g++ main.cpp support.cpp -o write`
Now when you run the _write_ executable the count will be printed
- **Mutable** - The mutable specifier applies only to class objects, which are discussed later in this tutorial. It allows a member of an object to override const member function. That is, a mutable member can be modified by a const member function.

#### Function
A function is a group of statements that together perform a task. Every C++ program has at least one function, which is main(), and all the most trivial programs can define additional functions.
The general form of a C++ function definition is as follows −
```
return_type function_name( parameter list ) {
   body of the function
}
```
- Return Type − A function may return a value. The return_type is the data type of the value the function returns. Some functions perform the desired operations without returning a value. In this case, the return_type is the keyword void.
- Function Name − This is the actual name of the function. The function name and the parameter list together constitute the function signature.
- Parameters − A parameter is like a placeholder. When a function is invoked, you pass a value to the parameter. This value is referred to as actual parameter or argument. The parameter list refers to the type, order, and number of the parameters of a function. Parameters are optional; that is, a function may contain no parameters.
- Function Body − The function body contains a collection of statements that define what the function does.
**Properties**
- A function declaration tells the compiler about a function name and how to call the function. The actual body of the function can be defined separately.Parameter names are not important in function declaration only their type is required, so following is also valid declaration − `int max(int, int);`
- Function declaration is required when you define a function in one source file and you call that function in another file. In such case, you should declare the function at the top of the file calling the function.
- If a function is to use arguments, it must declare variables that accept the values of the arguments. These variables are called the formal parameters of the function. The formal parameters behave like other local variables inside the function and are created upon entry into the function and destroyed upon exit.
    - Call by Value - This method copies the actual value of an argument into the formal parameter of the function. In this case, changes made to the parameter inside the function have no effect on the argument.
    - Call by Pointer - This method copies the address of an argument into the formal parameter. Inside the function, the address is used to access the actual argument used in the call. This means that changes made to the parameter affect the argument.
    - Call by Reference - This method copies the reference of an argument into the formal parameter. Inside the function, the reference is used to access the actual argument used in the call. This means that changes made to the parameter affect the argument.
    
#### Mathematical Operations
```
#include <iostream>
#include <cmath>
using namespace std;
int main () {
   // number definition:
   short  s = 10;   int    i = -1000;   long   l = 100000;   float  f = 230.47;   double d = 200.374;
   // mathematical operations;
   cout << "sin(d) :" << sin(d) << endl;
   cout << "abs(i)  :" << abs(i) << endl;
   cout << "floor(d) :" << floor(d) << endl;
   cout << "sqrt(f) :" << sqrt(f) << endl;
   cout << "pow( d, 2) :" << pow(d, 2) << endl;
   return 0;
}
```
#### String Functions
# TO be updated

#### Pointers
_A pointer is a variable whose value is the address of another variable. Like any variable or constant, you must declare a pointer before you can work with it._
The actual data type of the value of all pointers, whether integer, float, character, or otherwise, is the same, a long hexadecimal number that represents a memory address. The only difference between pointers of different data types is the data type of the variable or constant that the pointer points to.



