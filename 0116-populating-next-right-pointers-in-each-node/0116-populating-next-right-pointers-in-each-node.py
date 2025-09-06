class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        self._connect(root, None)
        return root

    def _connect(self, current: 'Optional[Node]', next_node: 'Optional[Node]') -> None:
        if current is None:
            return
        else:
            current.next = next_node  # connect

        self._connect(current.left, current.right)

        if next_node is not None:
            self._connect(current.right, next_node.left)
        else:
            self._connect(current.right, None)