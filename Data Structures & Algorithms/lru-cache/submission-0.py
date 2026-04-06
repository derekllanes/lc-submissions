class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    
    def remove(self, node):
        # Delete the key
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        # Insert the key on right of DLL
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        nxt.prev = node
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])

        else:
            if len(self.cache) >= self.cap:
                del self.cache[self.left.next.key]
                self.remove(self.left.next)
                self.cache[key] = Node(key, value)
                self.insert(self.cache[key])
            else:
                self.cache[key] = Node(key, value)
                self.insert(self.cache[key])



