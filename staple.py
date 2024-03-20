class queue:
    def __init__(self):
        self.liste = []

    def is_Empty(self):
        return len(self.liste) == 0
    def enqueue(self, element):
        self.liste.append(element)
    def dequeue(self):
        if not self.is_Empty():
            return self.liste.pop(0)
        return None
    def peek(self):
        if not self.is_Empty():
            return self.liste[0]
        return None
    def size(self):
        return len(self.liste)


class staple(queue):
    def dequeue(self):
        if not self.is_Empty():
            return self.liste.pop(-1)
        return None

    def peek(self):
        if not self.is_Empty():
            return self.liste[-1]
        return None

class priorityQueue(queue):
    def enqueue(self, value, priority=0):
        index = 0
        for i, (existing_value,prio_in_queue) in enumerate(self.liste):
            if priority < prio_in_queue:
                index = i
                break
            else:
                index += 1
        self.liste.insert(index, (value,priority))


queue = queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.is_Empty())
print(queue.dequeue()) # Liefert 1 zurück
print(queue.dequeue()) # Liefert 2 zurück
print(queue.peek()) # Liefert 3 zurück
print(queue.dequeue()) # Liefert 3 zurück
print(queue.size()) # Liefert 0 zurück

queue2 = staple()
queue2.enqueue(1)
queue2.enqueue(2)
queue2.enqueue(3)

print(queue2.is_Empty())
print(queue2.dequeue()) # Liefert 1 zurück
print(queue2.dequeue()) # Liefert 2 zurück
print(queue2.peek()) # Liefert 3 zurück
print(queue2.dequeue()) # Liefert 3 zurück
print(queue2.size()) # Liefert 0 zurück

queue3 = priorityQueue()
queue3.enqueue("Huge Priority",10)
queue3.enqueue("Not Important",23)
queue3.enqueue("That really is important",0)
queue3.enqueue("kinda important",1)

print(queue3.is_Empty())
print(queue3.dequeue()) # Liefert 1 zurück
print(queue3.dequeue()) # Liefert 2 zurück
print(queue3.peek()) # Liefert 3 zurück
print(queue3.dequeue()) # Liefert 3 zurück
print(queue3.size()) # Liefert 0 zurück