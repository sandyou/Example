from queue import Queue

print('這是FIFO的程式')
q = Queue()

for i in range(3):
    q.put(i)

while not q.empty():
    print(q.get())
