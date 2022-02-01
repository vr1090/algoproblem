class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.deque = deque()
        self.map = dict()

    def get(self, key: int) -> int:
        #print("get..",key, self.deque, self.map)
        if key not in self.map.keys():
            return -1
        else:
            self.deque.remove(key)
            self.deque.appendleft(key)
            return self.map[key]
        

    def put(self, key: int, value: int) -> None:
        if( len(self.deque) == self.capacity and key not in self.map.keys()):
            # do the clean up
            #print("request insert",key, value, "dequeue..", self.deque, "map..", self.map)
            keyJing = self.deque.pop()
            del self.map[keyJing]
            #print("after eviction,", self.deque, self.map)    
           
        
        if key in self.map.keys():
            self.deque.remove(key)
        
        self.deque.appendleft(key)
        self.map[key] = value
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)