class Queue:
    """队列"""

    def __init(self):
        # self.__list = []
        self.__list = []

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        # self.__list.append(item)
        self.__list.append(item)

    #         self.__list.insert(0, item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)

    #         return self.__list.pop()

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    #         return not self.__list

    def size(self):
        """返回队列大小"""
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    #     q.enqueue(2)
    #     q.enqueue(3)
    #     q.enqueue(4)
    #     print(q.dequeue())
    #     print(q.dequeue())
    #     print(q.dequeue())
    #     print(q.dequeue())