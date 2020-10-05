# Data Structures 
## 1. Arrays
An array is a collection of items stored at contiguous memory locations.
Sotring multiple elements together makes it esier to calculate the position of each element by simply adding offest to a base value.
Advantages
- Arrays allow random access of elements. This makes accessing elements by position faster.
- Arrays have better cache locality that can make a big difference in performance.
(locality of reference, also known as the principle of locality,[1] is the tendency of a processor to access the same set of memory locations repetitively over a short period of time.
Locality is a type of predictable behavior that occurs in computer systems. Systems that exhibit strong locality of reference are great candidates for performance optimization through the use of techniques such as the caching, prefetching for memory and advanced branch predictors at the pipelining stage of a processor core.)

Disadvantages
- Size cannot be changes once declared, unline a linked list, an array in c++ is not dynamic.
- Insertion and deletion of elements can be costly since the elements need to be managed in accordance with new memory allocation.
If you declare `int arr[6] = {1,2,3,4}` it will initialize array of size 6 and keep lasst 2 elements as 0.

#### No index out of bound checking 
If an index which is not present in the array is called, the program will compile but show garbage values.
If you declare the array as `int arr[2] = {1,2,3,4};` this will give an error- too many initializers for int[2]

#### Difference between pointer and an array
- Pointers are used for storing address of dynamically allocated arrays and for arrays which are passed as arguments to functions. 
- Sizeof() function shows they are of diffrent size
- Assigning any adress to pointer is allowed but to array variable is not.
- Compiler uses pointer arithmetic to access array element. For example, an expression like “arr[i]” is treated as *(arr + i) by the compiler. That is why the expressions like *(arr + i) work for array arr, and expressions like ptr[i] also work for pointer ptr.
- Array parameters are always passed as pointers, even when we use square brackets.

### Vectors in C++
Vector in cpp is a class in STL that represents an array. 
Advantages-
- Vectors support dynamic sizes.
- Vectors have many in-built function like, removing an element, etc.

Vectors are same as dynamic arrays with the ability to resize itself automatically when an element is inserted or deleted, with their storage being handled automatically by the container. Vector elements are placed in contiguous storage so that they can be accessed and traversed using iterators. In vectors, data is inserted at the end. Inserting at the end takes differential time, as sometimes there may be a need of extending the array. Removing the last element takes only constant time because no resizing happens. Inserting and erasing at the beginning or in the middle is linear in time.

#### Memory allocation
Like other variables, arrays can be allocated memory in any of the three segments, data, heap and stack.
Dynamically allocated arrays are allocated memory on heap.
Static or global arrays are allocated memory on data segment and local arrays are allocated memory on stack segment.
