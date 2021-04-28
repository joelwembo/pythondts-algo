Tree

A tree is an abstract data type that stores elements hierarchically. With the exception of the top element, each element in a tree has a parent element and zero or
more children elements. A tree is usually visualized by placing elements inside
ovals or rectangles, and by drawing the connections between parents and children
with straight lines. (See Figure 8.2.) We typically call the top element the root
of the tree, but it is drawn as the highest element, with the other elements being
connected below (just the opposite of a botanical tree).

p.element( ): Return the element stored at position p.
The tree ADT then supports the following accessor methods, allowing a user to
navigate the various positions of a tree:
T.root( ): Return the position of the root of tree T,
or None if T is empty.
T.is root(p): Return True if position p is the root of Tree T.
T.parent(p): Return the position of the parent of position p,
or None if p is the root of T.
T.num children(p): Return the number of children of position p.
T.children(p): Generate an iteration of the children of position p.
T.is leaf(p): Return True if position p does not have any children.
len(T): Return the number of positions (and hence elements) that
are contained in tree T.
T.is empty( ): Return True if tree T does not contain any positions.
T.positions( ): Generate an iteration of all positions of tree T.
iter(T): Generate an iteration of all elements stored within tree T
