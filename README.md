# DATA STRUCTURES

**Author**: Gabriel Meringolo, Marco Zangari

## Overview
Sample code for classic data structures

## Linked-List

###Make a linked list:

```
from linked_list import LinkedList

ll = LinkedList()
```

Big O runtime: 0(1)

###Push a value:

```
ll.push('one')
```

Big 0 runtime: 0(1)

###Pop a value:

```
ll.pop()
'one'
```

Big 0 runtime: 0(1)

###Size a value:

```
ll.push('one')
len(ll)
1
```

Big 0 runtime: 0(1)

###Search a value:

```
ll.search('one')
<linked_list.Node at 0x106b6ce10>
```

Big 0 runtime: 0(n)

###Remove a value:

```
node = ll.search('one')
ll.remove(node)
```

Big 0 runtime: 0(n)

###Display the linked list:

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