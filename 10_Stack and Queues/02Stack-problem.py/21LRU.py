

'''

Program for Least Recently Used (LRU) Page Replacement Algorithm

Problem Statement: Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity): Initialize the LRU cache with positive size capacity.
int get(int key): Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value): Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.


Input: ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output: [null, null, null, 1, null, -1, null, -1, 3, 4]
Explanation: 
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
Input: ["LRUCache","put","get"]
[[1],[2,1],[2] 
Output: [null, null, 1]
Explanation: 
LRUCache lRUCache = new LRUCache(1);
lRUCache.put(2, 1); // cache is {2=1}
lRUCache.get(2);    // return 1
'''


class LRUCache:
    # Doubly linked list node class
    class Node:
        # Constructor to initialize node
        def __init__(self, _key, _val):
            self.key = _key
            self.val = _val
            self.next = None
            self.prev = None

    # Constructor to initialize LRU cache
    def __init__(self, capacity: int):
        # Head and tail dummy nodes
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        # Capacity of cache
        self.cap = capacity
        # Hash map to store key-node mapping
        self.m = {}

    # Function to add a node right after head
    def addNode(self, newNode):
        temp = self.head.next
        newNode.next = temp
        newNode.prev = self.head
        self.head.next = newNode
        temp.prev = newNode

    # Function to remove a given node from list
    def deleteNode(self, delNode):
        delPrev = delNode.prev
        delNext = delNode.next
        delPrev.next = delNext
        delNext.prev = delPrev

    # Function to get value from cache
    def get(self, key_):
        # If key exists in cache
        if key_ in self.m:
            resNode = self.m[key_]
            res = resNode.val
            # Remove old mapping
            del self.m[key_]
            # Move accessed node to front
            self.deleteNode(resNode)
            self.addNode(resNode)
            # Update map
            self.m[key_] = self.head.next
            return res
        # If not found
        return -1

    # Function to put key-value into cache
    def put(self, key_, value):
        # If key already exists
        if key_ in self.m:
            existingNode = self.m[key_]
            del self.m[key_]
            self.deleteNode(existingNode)
        # If capacity reached
        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.deleteNode(self.tail.prev)
        # Insert new node at front
        self.addNode(self.Node(key_, value))
        self.m[key_] = self.head.next

object = LRUCache(2)
print(object.put(1, 1))  # cache is {1=1}
print(object.put(2, 2))  # cache is {1=1, 2=2}
print(object.get(1))    # return 1