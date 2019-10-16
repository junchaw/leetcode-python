# https://leetcode.com/problems/implement-stack-using-queues/
#
# Implement the following operations of a stack using queues.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# Example:
#
# MyStack stack = new MyStack();
#
# stack.push(1);
# stack.push(2);
# stack.top();   // returns 2
# stack.pop();   // returns 2
# stack.empty(); // returns false
# Notes:
#
# You must use only standard operations of a queue -- which means only push
# to back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may
# simulate a queue by using a list or deque (double-ended queue), as long as
# you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top
# operations will be called on an empty stack).
import collections


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rq = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        t = collections.deque()
        for _ in range(len(self.rq)):
            t.append(self.rq.popleft())
        self.rq.append(x)
        for _ in range(len(t)):
            self.rq.append(t.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.rq.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        value = self.rq.popleft()
        self.rq.appendleft(value)
        return value

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.rq) < 1



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

def solve():
    obj = MyStack()

    assert obj.empty()

    obj.push(1)
    obj.push(2)

    assert not obj.empty()

    assert obj.top() == 2  # not 1

    assert not obj.empty()

    assert obj.pop() == 2  # not 1
    assert obj.pop() == 1

    assert obj.empty()
