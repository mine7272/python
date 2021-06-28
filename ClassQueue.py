class MyQueue:
    #생성자
    def __init__(self):
        self.data=[]
    
    def get(self):
        return self.data.pop(0)
    def put(self,newItem) :
        self.data.append(newItem)
    
    def empty(self):
        return len(self.data)==0
    def qsize(self):
        return len(self.data)

queue=MyQueue()
queue.put("안녕")
queue.put(10)
queue.put(20)
print(queue.empty())
print(queue.qsize())
while not queue.empty():
    print(queue.get())
#FIFO 선입선출의 구조