# Design Hashmap Coding Interview
## Interviewer Cheatsheet
Process
- Naive Solution (Part 1) without the use of dictionaries [10 minutes]
    - Rule: cannot use dictionary
    - Should be going for an array solution with [-1] initialization
    - Review space and time of each method
- Probe
    - Can you make this more optimal? Try implementing a hashing function.
    - This is where you decide to move forward with Chaining or Random Remove (Part 2)
    - Review space and time of each method
- Chaining (Part 2a)
    - Should be going for a fixed smaller array with each element initialized with [None] linked lists
    - Review space and time of each method
- Random Remove (Part 2b)
    - Rule: size of collection should change with each additional key
    - Review space and time of each method

- (optional) Hashing Probing Questions: 
    - What is a hash function we can use when designing hash map? >> k % m == key value % initial size of map
    - How to reduce collisions? >> Using a greater initial size of Hash Table (resulting in lower load factors)
    - Do we have to worry about load factors? >> Yes. alpha = n/N = number of elements/size of table. Alpha should always be less than 1. We should also avoid high load factors of alpha >~ 0.85, where we would recommend rehashing.


Feedback
- If either part 2s was answered successfully with sufficient test cases, give pass.
- If both parts were answered successfully, give strong pass.

## Part 1. Design Hashmap
[YouTube](https://www.youtube.com/watch?v=ISir207RuKQ) | Challenge: Push for use of non-dictionary solution

## Part 2a. Design Hashmap with Chain Hashing
[YouTube](https://www.youtube.com/watch?v=ISir207RuKQ)
Array of linked list were collisions are handled by linked lists

## Part 2b. Design Hashmap with Random Remove

[B1, B2, B3, B4, ... , Bn]  Array of LinkedList of size n

B1 = ListNode (N1) -> N2 -> ...  LinkedList B1

B2 = ListNode (M1) -> M2 -> ...  LinkedList B2

Bn = ListNode (O1) -> O2 -> ...  LinkedList Bn

## Additional notes on HashMaps



Understand the HashMap data structure and collision
https://www.youtube.com/watch?v=zeMa9sg-VJM

Hashing - provides O(1) time on average for insert, search, and delete
Hash function - hash function maps a big number or string to a small integer that can be used as an index in hash table (or bucket)

h(k) = k % m
k: value of key
m: initial size of hash table

A good hash function satisfies two basic properties: 1) it should be very fast to compute; 2) it sohuld minimize collisions (duplication of output values)

Resolving collision via (1) open hashing/closed addressing [CHAINING] and (2) closed hashing/open addressing

Chaining: the idea is to make each cell of hash table point to a linked list of records that have same hash function value
