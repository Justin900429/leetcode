# 460 - LFU Cache

## Problem Description

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the `LFUCache` class:

* `LFUCache(int capacity)`Initializes the object with the `capacity` of the data structure.
* `int get(int key)` Gets the value of the `key`if the `key` exists in the cache. Otherwise, returns `-1`.
* `void put(int key, int value)` Update the value of the `key` if present, or inserts the `key` if not already present. When the cache reaches its `capacity`, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used `key` would be invalidated.

To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to `1` (due to the `put` operation). The use counter for a key in the cache is incremented either a `get` or `put` operation is called on it.

The functions `get` and `put` must each run in `O(1)` average time complexity.

### Example

```text
Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
```

> [Link to the problem](https://leetcode.com/problems/lfu-cache/)

## Concept

This problem is similar to [LRU cahce](https://leetcode.com/problems/lru-cache/). But we should not treat the whole problem as the doubly-linked list. We maintain a frequency hash map to access the first level of the doubly-linked list and another hash map for mapping the frequency from node.

## Solution

The `update` function below is to increase the frequency of the given node.

```python
class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
class DLink:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
        self.size += 1
    
    def pop(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1
        return node
    
    def pop_least(self):
        if self.size >= 1:
            return self.pop(self.tail.prev)
        else:
            raise ValueError("what")
    

class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.freq = defaultdict(DLink)
        self.min_size = 0
        self.cap = capacity
        
    def update(self, key):
        node, freq = self.cache[key]
        self.cache[key][1] += 1
        
        old_freq = self.freq[freq]
        old_freq.pop(node)
        
        if freq == self.min_size and old_freq.size == 0:
            self.min_size += 1
        
        self.freq[freq + 1].insert(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.update(key)
        return self.cache[key][0].val
        

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key in self.cache:
            self.cache[key][0].val = value
            self.update(key)
        else:
            if len(self.cache) == self.cap:
                del_node = self.freq[self.min_size].pop_least()
                del self.cache[del_node.key]
            
            self.min_size = 1
            new_node = Node(key, value)
            self.freq[self.min_size].insert(new_node)
            self.cache[key] = [new_node, 1]
```

> Time complexity: $\text{get}: O(n)$, $\text{put}: O(1)$ \
> Space complexity: $O(n)$
