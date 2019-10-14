# https://leetcode.com/problems/implement-queue-using-stacks/
#
# Implement the following operations of a queue using stacks.
#
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Example:
#
# MyQueue queue = new MyQueue();
#
# queue.push(1);
# queue.push(2);
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false
# Notes:
#
# You must use only standard operations of a stack -- which means only push
# to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may
# simulate a stack by using a list or deque (double-ended queue), as long as
# you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek
# operations will be called on an empty queue).

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack, self.outStack = [], []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inStack.append(x)

    def transfer(self):
        for _ in range(len(self.inStack)):
            self.outStack.append(self.inStack.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.outStack:
            return self.outStack.pop()
        if self.inStack:
            self.transfer()
            return self.pop()
        raise ValueError("No more element")

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.outStack:
            return self.outStack[-1]
        if self.inStack:
            self.transfer()
            return self.peek()
        raise ValueError("No element")

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.inStack and not self.outStack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


def solve():
    obj = MyQueue()

    assert obj.empty()

    obj.push(1)
    obj.push(2)

    assert not obj.empty()

    assert obj.peek() == 1  # not 2

    assert not obj.empty()

    assert obj.pop() == 1  # not 2
    assert obj.pop() == 2

    assert obj.empty()
