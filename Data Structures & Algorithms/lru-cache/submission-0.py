class DDL:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = DDL(-1, -1)
        self.tail = DDL(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.hashmap = {}
        
    def _add(self, node) -> None:
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = DDL(key, value)
        if key in self.hashmap:
            delete_node = self.hashmap[key]
            self._remove(delete_node)
        self.hashmap[key] = node
        self._add(node)

        cur_len = len(self.hashmap)
        if cur_len > self.capacity:
            delete_node = self.head.next
            self._remove(delete_node)
            del self.hashmap[delete_node.key]


 


        
