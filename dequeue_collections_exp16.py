from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to queue")

    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue.popleft()
        print(f"{item} removed from queue")
        return item

    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty. Nothing to peek.")
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Front item:", q.peek())
    q.safe_dequeue()
    q.safe_dequeue()
    q.safe_dequeue()
    q.safe_dequeue() 
