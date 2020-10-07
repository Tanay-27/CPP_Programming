# Stack
Stack is a linear data structure which follows a particular order in whice the operations are performed. The order may be LIFO of FILO
Mainly three basic operations are performed in the stack.
- Push: Adds an item at the top of stack, if stack is full, then it is said to be an overflow condition.
- Pop: Removes an item from stack. Items are removed in reverse order. If stack is empty it is said to be in underflow condition.
- Peek or Top: Returns top element of stack.
- isEmpty: Returns true if stack is empty.

Implementation of stack
Using linked list or using array
if you use array the size of stack is fixed.
If you use linked list more memory is used due to pointers.

### Stacks in C++ STL
The functions associated with stack are:
- empty() – Returns whether the stack is empty – Time Complexity : O(1)
- size() – Returns the size of the stack – Time Complexity : O(1)
- top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
- push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
- pop() – Deletes the top most element of the stack – Time Complexity : O(1)

### Stacks in Python
One can implement using either
- Lists
- Deque from collections library
- LifoQueue from queue library

### Infix and Postfix
Infix expression:The expression of the form a op b. When an operator is in-between every pair of operands.
Postfix expression:The expression of the form a b op. When an operator is followed for every pair of operands.
The repeated scanning makes it very in-efficient. It is better to convert the expression to postfix(or prefix) form before evaluation.
Postfix can be easily implemented using stacks
