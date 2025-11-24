class Queue:
    """
    A simple Queue data structure (FIFO: First-In-First-Out).

    Methods:
        enqueue(item): Add an item to the end of the queue.
        dequeue(): Remove and return the item at the front of the queue.
        peek(): Return the front item without removing it.
        is_empty(): Check if the queue is empty.
        size(): Return the number of items in the queue.
    """

    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the front item of the queue.
        Returns:
            The front item if the queue is not empty.
            None if the queue is empty (edge case handled).
        """
        if self.is_empty():
            print("Warning: Attempt to dequeue from empty queue")
            return None
        return self.items.pop(0)

    def peek(self):
        """
        Return the front item without removing it.
        Returns:
            The front item if the queue is not empty.
            None if the queue is empty (edge case handled).
        """
        if self.is_empty():
            print("Warning: Attempt to peek at empty queue")
            return None
        return self.items[0]

    def is_empty(self):
        """Return True if the queue is empty, else False."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)


# -------------------------------
# Testing the Queue class
# -------------------------------

q = Queue()

# Test enqueue
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue after enqueues:", q.items)  # [10, 20, 30]

# Test peek
print("Peek:", q.peek())  # 10

# Test dequeue
print("Dequeue:", q.dequeue())  # 10
print("Dequeue:", q.dequeue())  # 20
print("Dequeue:", q.dequeue())  # 30

# Test edge case: dequeue from empty queue
print("Dequeue from empty queue:", q.dequeue())  # Warning + None

# Test edge case: peek at empty queue
print("Peek at empty queue:", q.peek())  # Warning + None

# Test size and is_empty
print("Queue size:", q.size())          # 0
print("Is queue empty?", q.is_empty())  # True
