class Dlist:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Dlist(-1, -1)
        self.tail = Dlist(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.node_dict = {}
        self.capacity = capacity        

    def get(self, key: int) -> int:
        if key in self.node_dict:
            node = self.node_dict[key]
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.node_dict:
            self.node_dict[key].val = value
            self._remove(self.node_dict[key])
            self._add(self.node_dict[key])
        else:
            node = Dlist(key, value)
            self.node_dict[key] = node
            self._add(node)
            if len(self.node_dict) > self.capacity:
                delete_node = self.tail.prev
                del self.node_dict[delete_node.key]
                self._remove(delete_node)

    def _add(self, node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node


        
