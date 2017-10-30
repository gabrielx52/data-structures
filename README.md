# DATA STRUCTURES

**Author**: Gabriel Meringolo, Marco Zangari

## Overview
Sample code for classic data structures

## Deque

### Make a Deque
```
from deque import Deque
dq = Deque()
```

### Append a Value
```
dq.append('one')
```

Big 0 runtime: 0(1)

### Appendleft a Value
```
dq.append('one')
```

Big 0 runtime: 0(1)

### Pop a Value
```
dq.pop()
```

Big 0 runtime: 0(1)

### Popleft a Value
```
dq.popleft()
```

Big 0 runtime: 0(1)

### Peek a Value
```
dq.peek()
```

### Peekleft a Value
```
dq.peekleft()
```

Big 0 runtime: 0(1)


## Queue

#### Make a Queue

```
from que_ import Queue

q = Queue()
```

Big 0 runtime: 0(1)

### Add a value to a Queue

```
q.enqueue('one')
```

Big 0 runtime: 0(1)

### Remove a value from Queue

```
q.dequeue()
```

Big 0 runtime: 0(1)

### Peek

```
q.peek()
```

Big 0 runtime: 0(1)

### Size

```
q.size()
```

Big 0 runtime: 0(1)

### Len

```
len(q)
```

Big 0 runtime: 0(1)


## Doubly Linked List

### Make a Doubly Linked List

```
from doubly_linked_list import DoublyLinKedList

dll = DoublyLinkedList()
```

Big 0 runtime = O(1)

### Push a Value:

```
dll.push('one')
```

Big 0 runtime = O(1)

### Append a Value:

```
dll.append('one')
```

Big 0 runtime = O(1)

### Pop a Value:

```
ll.pop()
```

Big 0 runtime = O(1)

### Shift a Value:

```
ll.shift()
```

Big 0 runtime = O(1)

### Remove a Value:

```
ll.remove('one')
```

Big 0 runtime = O(n)


## Stack

### Make a stack:

```
from stack import Stack

stck = Stack()
```

Big 0 runtime: 0(1)

### Push a value:

```
stck.push('one')
```

Big 0 runtime: 0(1)

### Pop a value:

```
stck.pop()
```

Big 0 runtime: 0(1)

### Get a length value:

```
len(stck)
```

Big 0 runtime: 0(1)


## Linked-List

### Make a linked list:

```
from linked_list import LinkedList

ll = LinkedList()
```

Big O runtime: 0(1)

### Push a value:

```
ll.push('one')
```

Big 0 runtime: 0(1)

### Pop a value:

```
ll.pop()
'one'
```

Big 0 runtime: 0(1)

### Size a value:

```
ll.push('one')
len(ll)
1
```

Big 0 runtime: 0(1)

### Search a value:

```
ll.search('one')
<linked_list.Node at 0x106b6ce10>
```

Big 0 runtime: 0(n)

### Remove a value:

```
node = ll.search('one')
ll.remove(node)
```

Big 0 runtime: 0(n)

### Display the linked list:

```
ll.push('one')
ll.push('two')
ll.push('three')
ll.display()
"('one', 'two', 'three')"
```

Big 0 runtime: 0(n)

## Architecture
Written in python, tested with pytest and tox.