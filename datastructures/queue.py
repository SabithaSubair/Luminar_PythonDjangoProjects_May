#queue
#insertion......enqueue
#deletion........dequeue
#order.......FIFO.....First In First Out
que=[]
size=int(input("enter size:"))
front=0
rear=0
n=0
def insert():
    global front,rear,size,que
    if rear>=size:
        print("queue is full")
    else:
        p=int(input("enter the elemnt wants to insert:"))
        que.insert(rear,p)
        rear +=1

        for i in range (front,rear):
            print(que[i])
def delete():
    global front, rear, size, que
    if rear == front:
        print("queue is empty")
    else:
        front +=1
        for i in range(front,rear):
            print(que[i])
while n!=1:
    print("enter option u want to perform")
    opt=int(input("press 1.enqueue 2.dequeue"))
    if opt==1:
        insert()
    elif opt==2:
        delete()
    n = int(input("do u want to continue press 1 for exit"))