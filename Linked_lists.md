# Linked Lists
A linked list is a linera data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list zre linked using pointers.
Simply put, a linked list consists of nodes where each node contains a daa field and a refernece(link) to the next node in the list.
Advantages
- Dynamic size
- Ease of insertion/deletion
Drawbacks
- Random access is not allowed, we have to access elements sequentially, binary search cannot be performed.
- Extra memory space for pointer with each element in the list.
- Not cache freindly.

Representation
A inked list is represented  by a pointer to the first node of the linked list.
The first node is called the head. If linked list is empty the value of head node is NUL.

A simple C++ program to introduce a linked list
```
class Node{
publice:
  int data;
  Node* next;
};
void print(Node* n){
    while(n!=NULL){
        cout << n->data << " ";
        n = n->next;
    }
}
int main(){
    Node* head = new Node();
    Node* second = new Node();
    Node* third = new Node();
    head->data = 1;
    head->next = second;
    second->data=2;
    second->next=third;
    third->data=3;
    third->next= NULL;
    print(head);
}
```
A program to insert a new element at the start, end after an element
```
class Node  
{  
    public: 
    int data;  
    Node *next;  
};  
/* Given a reference (pointer to pointer) to the head of a list and an int, inserts a new node on the front of the list. */
void push(Node** head_ref, int new_data)  
{  
    /* 1. allocate node */
    Node* new_node = new Node(); 
  
    /* 2. put in the data */
    new_node->data = new_data;  
  
    /* 3. Make next of new node as head */
    new_node->next = (*head_ref);  
  
    /* 4. move the head to point to the new node */
    (*head_ref) = new_node;  
}  
  
/* Given a node prev_node, insert a new node after the given  
prev_node */
void insertAfter(Node* prev_node, int new_data)  
{  
    /*1. check if the given prev_node is NULL */
    if (prev_node == NULL)  
    {  
        cout<<"the given previous node cannot be NULL";  
        return;  
    }  
  
    /* 2. allocate new node */
    Node* new_node = new Node(); 
  
    /* 3. put in the data */
    new_node->data = new_data;  
  
    /* 4. Make next of new node as next of prev_node */
    new_node->next = prev_node->next;  
  
    /* 5. move the next of prev_node as new_node */
    prev_node->next = new_node;  
}  
  
/* Given a reference (pointer to pointer) to the head  of a list and an int, appends a new node at the end */
void append(Node** head_ref, int new_data)  
{  
    /* 1. allocate node */
    Node* new_node = new Node(); 
    Node *last = *head_ref; /* used in step 5*/
  
    /* 2. put in the data */
    new_node->data = new_data;  
  
    /* 3. This new node is going to be the last node, so make next of  it as NULL*/
    new_node->next = NULL;  
  
    /* 4. If the Linked List is empty, then make the new node as head */
    if (*head_ref == NULL)  
    {  
        *head_ref = new_node;  
        return;  
    }  
  
    /* 5. Else traverse till the last node */
    while (last->next != NULL)  
        last = last->next;  
  
    /* 6. Change the next of last node */
    last->next = new_node;  
    return;  
}  
  
// This function prints contents of linked list starting from head  
void printList(Node *node)  
{  
    while (node != NULL)  
    {  
        cout<<" "<<node->data;  
        node = node->next;  
    }  
}  
  
/* Driver code*/
int main()  
{  
    /* Start with the empty list */
    Node* head = NULL;  
      
    // Insert 6. So linked list becomes 6->NULL  
    append(&head, 6);  
      
    // Insert 7 at the beginning.  So linked list becomes 7->6->NULL  
    push(&head, 7);  
      
    // Insert 1 at the beginning. So linked list becomes 1->7->6->NULL  
    push(&head, 1);  
      
    // Insert 4 at the end. So  linked list becomes 1->7->6->4->NULL  
    append(&head, 4);  
      
    // Insert 8, after 7. So linked  list becomes 1->7->8->6->4->NULL  
    insertAfter(head->next, 8); 
    cout<<"Created Linked list is: ";  
    printList(head);  
      
    return 0;  
}  
```
Function to delete the entire linked list
The idea is to iterate over each node and free it
```
void deleteList(Node** head_ref)  
{  
      
/* deref head_ref to get the real head */
Node* current = *head_ref;  
Node* next;  
  
while (current != NULL)  
{  
    next = current->next;  
    free(current);  
    current = next;  
}  
      
/* deref head_ref to affect the real head back  
    in the caller. */
*head_ref = NULL;  
}  
```
To print nth node from last
```

void printNthFromLast(struct Node* head, int n) 
{ 
    static int i = 0; 
    if (head == NULL) 
        return; 
    printNthFromLast(head->next, n); 
    if (++i == n) 
        printf("%d", head->data); 
} 
```
Another method
Maintain two pointers – reference pointer and main pointer. Initialize both reference and main pointers to head. First, move reference pointer to n nodes from head. Now move both pointers one by one until the reference pointer reaches the end. Now the main pointer will point to nth node from the end. Return the main pointer.

To find the middle element
```
    while (fast_ptr != NULL && fast_ptr->next != NULL)  
        {  
            fast_ptr = fast_ptr->next->next;  
            slow_ptr = slow_ptr->next;  
        }  
```
To detect loop in linked list
method-1 Hashing
To store the addresses of the nodes in a hash table and if the address matches return true
```
bool detectLoop(struct Node* h){
    unordered_set<Node*> s;
    while (h != NULL) {
        // If this node is already present in hashmap it means there is a cycle (Because you we encountering the node for the second time).
        if (s.find(h) != s.end())
            return true;
        // If we are seeing the node for the first time, insert it in hash
        s.insert(h);
        h = h->next;
    }
    return false;
}
 ```
 Method-2 Flags
 We can change the structure of the linked list to include a variable flag `int flag;` or `bool flag;`
And assign 0 or false while inserting data
While traversing the linked list modify this parameter to 1 or True. a simple if condition can help us detect if we have come to this node before.

Method =3
Floyd's Cycle finding algorithm
This states that if we traverse through a linked list with  pointers 1 moving wice as fast as the slow one
If a loop exists they will definietly meet, thus compare the 2 pointers at each iteration.
This is the fastest solution.

To find the length of loop in linked list
We first use the floyds cycle detection algorithm to detect a loop, store the address of the pointer where they meet
Keep going next untill the same node is reached again while increasing the counter at each iteration.
This gives the length of loop

To remove loop from linked list
- First we need to detect if thee is a loop present.
- Count the number of loops in the linked list.
- Fix one pointer at head another at kth position from start.
- Increase both at same pace, they'll meet at the start of loop
- Get the node before that, and change the next address to null
Loop is removed.

To find if linked list is palindrome
Method-1 Recursive
- Call the function again and again untill right end is reacheed 
- Then compare the last and first value, if not same return false
- If same shift the left pointer by 1 place
- If end is reached, return true

Method -2 
Using stack
- Create `stack<int> s;` then push each element inside `s.push(ptr->data)`
- Compare and pop each element `s.top();` and `s.pop();`

#### To Reverse a linked list
```
void reverse() 
    { 
        // Initialize current, previous and next pointers 
        Node* current = head; 
        Node *prev = NULL, *next = NULL; 
  
        while (current != NULL) { 
            // Store next 
            next = current->next; 
  
            // Reverse current node's pointer 
            current->next = prev; 
  
            // Move pointers one position ahead. 
            prev = current; 
            current = next; 
        } 
        head = prev; 
    } 
    ```
    Huge number calculation can be erformed using doubly linked list
    Effecint way to implementing doubly linked list is using XOR function while storing xxored address for previous and next.
    
