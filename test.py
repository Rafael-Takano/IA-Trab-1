import queue
p_queue = queue.PriorityQueue()
p_queue.put((2, "A"))
p_queue.put((1, "B"))
p_queue.put((3, "C"))
print(p_queue.get())
print(p_queue.get()[1])
print(p_queue.get()[0])