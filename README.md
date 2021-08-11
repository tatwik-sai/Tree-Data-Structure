# simplepytree

Easy to use Tree Data Structure with many useful methods.

Developed by Tatwik.

# Examples of using simplepytree

![Tree Example](https://adrianmejia.com/images/tree-parts.jpg)

We will consider this image as an example for the below code.

## Creating a Tree
---

1. Adding the root node at initialization.

```python
  from simplepytree import Tree
  tree = Tree(root_nodes=['a'])
```

> 1. We can have multiple root nodes, Just by passing multiple nodes to the parameter 'root_nodes'

2. Adding the root node after initialization.

```python
  from simplepytree import Tree
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

- ### add_node()
> Adds the node to the tree.
> - parameter node: Tuple with parent and child.
> ```python
> tree.add_node(('parent_node', 'node_name'))
> ```

- ### add_children()
> Adds multiple children to the node.
> - parameter node: The name of the node.
> - parameter children: List of children of the node.
> ```python
> tree.add_children('node_name', ['child_node1', 'child_node2', 'child_node3'])
> ```

- ### get_parent()
> Returns the parent of the given node.
> - parameter node: The name of the node.
> - returns: The parent of the given node.
> ```python
> tree.get_parent('b')
> ```
> Output: 'a'

- ### get_children()
> Returns the list of childeren of the given node.
> - parameter node: The name of the node.
> - returns: The list of children for the node.
> ```python
> tree.get_children('a')
> ```
> > Output: ['b', 'c', 'd']

- ### get_path()
> Returns The path from root node to the given node.
> - parameter node: The name of the node.
> - return: The list of path from root node to the given node.
> ```python
> tree.get_path('i')
> ```
> > Output: ['a', 'd', 'h', 'i']

- ### get_depth()
> Returns the depth at where the node is located in the tree.
> - parameter node: The name of the node.
> - return: The depth at which the node is located in the tree.
> ```python
> tree.get_depth('g')
> ```
> > Output: 2

- ### delete()
> Deletes the node and the tree to the down of the node.
> - parameter node: The name of the node.
> ```python
> tree.delete('d')
> ```
> Because we deleted node 'd' all the nodes below it will also get deleted so the nodes ['d', 'g', 'h', 'i', 'j'] will be deleted.

---

[Mail me](mailto:sreenu143anupama@gmail.com)
