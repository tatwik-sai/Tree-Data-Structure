# simple-pytree

Easy to use Tree Data Structure with many useful methods.

Developed by Tatwik.

# Examples of using simple-pytree

![Tree Example](https://adrianmejia.com/images/tree-parts.jpg)

We will consider this image as an example for the below code.

## Creating a Tree
---

1. Adding the root node at initialization.

```python
  from tree import Tree
  tree = Tree(root_nodes=['a'])
```

> 1. We can have multiple root nodes, Just by passing multiple nodes to the parameter 'root_nodes'

2. Adding the root node after initialization.

```python
  from tree import Tree
  tree = Tree()
  tree.add_node(('nil', 'a'))
```

> 1. Here the parent node of the root node 'a' is 'nil'.
> 2. You can modify the 3rd line of the above code as 
> ```python
> tree.add_children('nil', ['a'])
> ```
> The above function helps to add multiple root nodes instead of one root node 'a'.

3. Adding the remaining nodes to the tree.

```python
# level-1
tree.add_children('a', ['b', 'c', 'd'])
# level-2
tree.add_children('b', ['e', 'f'])
tree.add_children('d', ['g', 'h'])
# level-3
tree.add_children('h', ['i', 'j'])
```
> 1. Now we have created a Tree that's in the above image.

> 2. Let's print the Tree we have created.
> ```python
> print(tree.tree)
> ```
> Output:
> 
> {'nil': (None, ['a']), 'a': ('nil', ['b', 'c', 'd']), 'b': ('a', ['e', 'f']), 'c': ('a', []), 'd': ('a', ['g', 'h']), 'e': ('b', []), 'f': ('b', []), 'g': ('d', []), 'h': ('d', ['i', 'j']), 'i': ('h', []), 'j': ('h', [])}
> 
> Let's check the above Output dictionary.
> - Dict Keys - Node names
> - Dict Values - (parent node, [child nodes])
> 
> Let's see an example:
> Consider: 'a': ('nil', ['b', 'c', 'd'])
> - Here 'a' is the node name.
> - 'nil' is the parent node of 'a'.
> - ['b', 'c', 'd'] are the children nodes of node 'a'.

## Using the methods of Tree class
---

### add_node()
> Adds the node to the tree.
> - parameter node: tuple, Tuple with parent and child.
> ```python
> tree.add_node(('parent_node', 'node_name'))
> ```

### add_children()
