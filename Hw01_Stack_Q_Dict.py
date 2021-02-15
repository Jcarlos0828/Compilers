class node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class stack:
    def __init__(self):
        self.head = node()
        self.end = None

    def push(self, nVal):
        if self.head.val is None:
            self.head.val = nVal
            self.end = self.head
        else:
            self.end.next = node(nVal)
            self.end = self.end.next
    
    def pop(self):
        if self.head.val is None:
            print("The stack is empty, try again")
            return

        curr = self.head
        while curr.next.next is not None:
            print(curr.val)
            curr = curr.next
        del curr.next
        curr.next = None
        self.end = curr
    
    def printt(self):
        print(self.end.val)

class queue:
    def __init__(self):
        self.head = node()
        self.end = None
    
    def push(self, nVal):
        if self.head.val is None:
            self.head.val = nVal
            self.end = self.head
        else:
            self.end.next = node(nVal)
            self.end = self.end.next
    
    def pop(self):
        if self.head.val is None:
            print("The queue is empty, try again")
            return

        self.head.val = None
        self.head = self.head.next
    
    def printt(self):
        print(self.head.val)

class dictionary:
    def __init__(self):
        self.key = []
        self.vals = []
    
    def add(self, nkey, nval):
        if len(self.vals) == 0:
            self.key.append(nkey)
            self.vals.append(nval)
        elif nval >= self.vals[len(self.vals)-1] or nval <= self.vals[0]:
            if nval <= self.vals[0]:
                self.vals.insert(0, nval)
                self.key.insert(0, nkey)
            else:
                self.vals.append(nval)
                self.key.append(nkey)
        else:
            top = len(self.vals) - 1
            low = 0
            while low <= top:
                mid = (top+low)//2
                if self.vals[mid] == nval:
                    self.vals.insert(mid, nval)
                    self.key.insert(mid, nkey)
                    return
                elif self.vals[mid] >= nval:
                    top = mid -  1
                else:
                    low = mid + 1
            self.vals.insert(top+1, nval)
            self.key.insert(top+1, nkey)

    
    def get(self, nkey):
        low = 0
        top = len(self.key)-1
        while low <= top:
            mid = (top+low) // 2
            if self.key[mid] == nkey:
                return self.vals[mid]
            elif self.key[mid] >= nkey:
                top = mid - 1
            else:
                low = mid + 1
        print("The key don't exist, try again")
        
    def delete(self, nkey):
        
        low = 0
        top = len(self.key)-1
        while low <= top:
            mid = (top+low) // 2
            if self.key[mid] == nkey:
                self.vals.pop(mid)
                self.key.pop(mid)
                return

            elif self.key[mid] >= nkey:
                top = mid - 1
            else:
                low = mid + 1
        print("The key don't exist, try again")

    def keys(self):
        return self.key
    
    def values(self):
        return self.vals                  