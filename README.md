# simple-pytree

Easy to use Tree Data Structure with many useful methods.

Developed by Tatwik.

## Examples of using simplepygraph

![Tree Example](https://adrianmejia.com/images/tree-parts.jpg)

We will consider this image as an example for the below code.

### Creating a Graph

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
