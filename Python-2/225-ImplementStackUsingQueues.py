class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queues = [[], []]

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        # Push to the queue with element.
        queue = self.queues[0] if self.queues[0] else self.queues[1]
        queue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        queue_to_pop, _ = self.dump()
        queue_to_pop.pop()

    def top(self):
        """
        :rtype: int
        """
        queue_to_pop, queue_to_push = self.dump()
        top = queue_to_pop[0]
        queue_to_push.append(queue_to_pop.pop(0))
        return top

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queues[0] and not self.queues[1]

    def dump(self):
        queue_to_pop, queue_to_push = ((self.queues[0], self.queues[1])
                                       if self.queues[0] else
                                       (self.queues[1], self.queues[0]))
        while len(queue_to_pop) != 1:
            queue_to_push.append(queue_to_pop.pop(0))
        return queue_to_pop, queue_to_push
