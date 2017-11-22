[![Build Status](https://travis-ci.org/gabrielx52/data-structures.svg?branch=bst)](https://travis-ci.org/gabrielx52/data-structures)

# DATA STRUCTURES

**Author**: Gabriel Meringolo, Marco Zangari

## Overview
Sample code for classic data structures

## Graph

### Make a Graph
```
from graph_1 import Graph
g = Graph()
```

Big O runtime: O(1)

### Add a node
```
g.add_node(1)
```

Big O runtime: O(1)

### Add an edge
```
g.add_edge(1, 2)
```

Big O runtime: O(1)

### Display nodes
```
g.nodes()
[1, 2]
```

Big O runtime: O(1)

### Display edges
```
g.edges()
[(1, 2)]
```

Big O runtime: O(n**2)

### Delete node
```
g.del_node(1)
```

Big O runtime: O(n**2)

### Delete edge
```
g.del_edge((1, 2))
```

Big O runtime: O(n**2)

### Check if graph has node
```
g.has_node(1)
True
```

Big O runtime: O(1)

### See node's neighbors
```
g.neighbors(1)
[2, 3, 4]
```

Big O runtime: O(1)

### See if two nodes are connected by an edge
```
g.adjacent((1, 7))
False
```

Big O runtime: O(1)

### Breatdth first traversal
```
g.breadth_first_traversal(1)
[1, 2, 3, 4, 5]
```

Big O runtime: O(n)

### Depth first traversal
```
g.breadth_first_traversal(1)
[1, 2, 5, 3, 5]
```

Big O runtime: O(nk)

## Priority Que

### Make a Priority Que
```
from priority_que import Priorityq
pq = Priorityq()
```

Big O runtime: O(1)

### Insert a Value
```
pq.insert(2,3)
```

Big O runtime: O(1)

## Peek a Value
```
pq.peek()
```

Big O runtime: O(n)

### Pop a Value
```
pq.pop()
```

Big O runtime: O(n)


## Max Heap

### Make a Max Heap
```
from max_heap import MaxHeap
mh = MaxHeap()
```

Big O runtime: O(1)

### Push a Max Heap
```
mh.push(1)
```

Big O runtime: O(log n)

#### Pop a Max Heap
```
mh.pop()
```

Big O runtime: O(log n)


## Deque

### Make a Deque
```
from deque import Deque
dq = Deque()
```

Big O runtime: O(1)

### Append a Value
```
dq.append('one')
```

Big O runtime: O(1)

### Appendleft a Value
```
dq.append('one')
```

Big O runtime: O(1)

### Pop a Value
```
dq.pop()
```

Big O runtime: O(1)

### Popleft a Value
```
dq.popleft()
```

Big O runtime: O(1)

### Peek a Value
```
dq.peek()
```

### Peekleft a Value
```
dq.peekleft()
```

Big O runtime: O(1)

### Size
```
dq.size()
```

Big O runtime: O(1)


## Queue

#### Make a Queue

```
from que_ import Queue

q = Queue()
```

Big O runtime: O(1)

### Add a value to a Queue

```
q.enqueue('one')
```

Big O runtime: O(1)

### Remove a value from Queue

```
q.dequeue()
```

Big O runtime: O(1)

### Peek

```
q.peek()
```

Big O runtime: O(1)

### Size

```
q.size()
```

Big O runtime: O(1)

### Len

```
len(q)
```

Big O runtime: O(1)


## Doubly Linked List

### Make a Doubly Linked List

```
from doubly_linked_list import DoublyLinKedList

dll = DoublyLinkedList()
```

Big O runtime = O(1)

### Push a Value:

```
dll.push('one')
```

Big O runtime = O(1)

### Append a Value:

```
dll.append('one')
```

Big O runtime = O(1)

### Pop a Value:

```
ll.pop()
```

Big O runtime = O(1)

### Shift a Value:

```
ll.shift()
```

Big O runtime = O(1)

### Remove a Value:

```
ll.remove('one')
```

Big O runtime = O(n)


## Stack

### Make a stack:

```
from stack import Stack

stck = Stack()
```

Big O runtime: O(1)

### Push a value:

```
stck.push('one')
```

Big O runtime: O(1)

### Pop a value:

```
stck.pop()
```

Big O runtime: O(1)

### Get a length value:

```
len(stck)
```

Big O runtime: O(1)


## Linked-List

### Make a linked list:

```
from linked_list import LinkedList

ll = LinkedList()
```

Big O runtime: O(1)

### Push a value:

```
ll.push('one')
```

Big O runtime: O(1)

### Pop a value:

```
ll.pop()
'one'
```

Big O runtime: O(1)

### Size a value:

```
ll.push('one')
len(ll)
1
```

Big O runtime: O(1)

### Search a value:

```
ll.search('one')
<linked_list.Node at 0x106b6ce10>
```

Big O runtime: O(n)

### Remove a value:

```
node = ll.search('one')
ll.remove(node)
```

Big O runtime: O(n)

### Display the linked list:

```
ll.push('one')
ll.push('two')
ll.push('three')
ll.display()
"('one', 'two', 'three')"
```

Big O runtime: O(n)

## Architecture
Written in python, tested with pytest and tox.