class ListNode:
    def __init__(self,val=0,key = 0,next=None,prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.first = None
        self.last = None
        self.capacity = capacity
        self.count = 0
        self.d = {}
    def changePostion(self,head):
        x = head
        if self.first.key == x.key:
            self.first = self.first.next
        if x.next:
            x.next.prev = x.prev
        if x.prev:
            x.prev.next = x.next
        x.next = None
        x.prev = None
        if self.last:
            self.last.next = x
            x.prev = self.last
            self.last = self.last.next
        else:
            self.last = x
        self.d[self.last.key] = self.last

        return self.last.val

    def get(self, key: int) -> int:
        if key in self.d:
            return self.changePostion(self.d[key])
        return -1


    def put(self, key: int, value: int) -> None:
        if self.count == 0: # if count is 0 creating first node and last node and increasing the count
            self.last = ListNode(value,key)
            self.first = self.last
            self.count += 1
            self.d[key] = self.last
        else:
            if key in self.d: # changing the position to the last
                self.changePostion(self,key)
                return
            else: #appending new (key,value) at last node
                self.last.next = ListNode(val=value,key=key,prev=self.last)
                self.last = self.last.next
                self.d[key] = self.last
            if self.count >= self.capacity: # if count is greater than capacity deleting first node
                if self.first:
                    del self.d[self.first.key]
                    self.first = self.first.next
            else: # if count is less than capacity incrementing the count
                self.count += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(3)
# param_1 = obj.get(key)
print(obj.put(1,1))
print(obj.put(2,2))
print(obj.put(3,3))
print(obj.get(1))
print(obj.last.val)
print(obj.first.val)
# print(obj.put(4,4))
# print(obj.get(2))
