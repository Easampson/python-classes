class Stack
    def __inti__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return slef.items[len(self.items)-1]

    def size(self):
        return len(self.items)

