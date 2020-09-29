Difference between front(), back() and begin, end() function
begin() and end() function return an iterator(like a pointer) initialized to the first or the last element of the container that can be used to iterate through
the collection, while front() and back() function just return a reference to the first or the last element of the container

Tokenizing a string denotes splitting a string with respect to a delimiter.
```
#include <iostream> 
#include <string> 
using namespace std; 
  
int main() 
{ 
    string str; 
  
    cout << "Please enter your name: \n"; 
    getline(cin, str); 
    cout << "Hello, " << str 
         << " welcome to GfG !\n"; 
  
    return 0; 
}
```


It is recommended by many of the programmers that strncat() is safe as compared to strcat() because strcat() does not check for the size of the copied data, 
and copies until it gets to a null terminator, it might cause a buffer overflow while strncat() check for the size of the copied data, and will copy only ‘n’ bytes.
strcat(destinaion,source)
strncat(destination,source,n)


int r = strpbrk(s1,s2)
This function finds the first character in the string s1 that matches any character specified in s2

https://www.geeksforgeeks.org/cc-programs/

A template is a simple and yet very powerful tool in C++. The simple idea is to pass data type as a parameter so that we don’t need to write the same code 
for different data types. For example, a software company may need sort() for different data types. Rather than writing and maintaining the multiple codes, 
we can write one sort() and pass data type as a parameter. 
```
template <typename T> 
T myMax(T x, T y) 
{ 
   return (x > y)? x: y; 
} 
  
int main() 
{ 
  cout << myMax<int>(3, 7) << endl;  // Call myMax for int 
  cout << myMax<double>(3.0, 7.0) << endl; // call myMax for double 
  cout << myMax<char>('g', 'e') << endl;   // call myMax for char 
  
  return 0; 
}
```

Sorting in cpp
it is implemented using hybrid of QuickSort, HeapSort and InsertionSort.By default, it uses QuickSort but if QuickSort is doing unfair partitioning and taking more 
than N*logN time, it switches to HeapSort and when the array size becomes really small, it switches to InsertionSort.

Function in stl predefined
binary_search(a, a + 10, 2)

```
  // Reversing the Vector 
    reverse(vect.begin(), vect.end()); 
  
    cout << "\nVector after reversing is: "; 
    for (int i=0; i<6; i++) 
        cout << vect[i] << " "; 
  
    cout << "\nMaximum element of vector is: "; 
    cout << *max_element(vect.begin(), vect.end()); 
  
    cout << "\nMinimum element of vector is: "; 
    cout << *min_element(vect.begin(), vect.end()); 
  
    // Starting the summation from 0 
    cout << "\nThe summation of vector elements is: "; 
    cout << accumulate(vect.begin(), vect.end(), 0); 
  
    return 0; 
} 
```

Wrtie down the whole of this
https://www.geeksforgeeks.org/c-magicians-stl-algorithms/

Valarrays
min max shift apply functions are easily calculated

https://www.geeksforgeeks.org/std-valarray-class-c/

