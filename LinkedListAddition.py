class Node(object):
    def __init__(self, data, next=None):
        self.next = None
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_data(self):
        return self.data

class LinkedList(object):
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self, data):
        new_node = Node(data=data)
        if self.root is None:
            self.root = new_node
            new_node.set_next(None)
        else:
            temp = self.root
            while temp.get_next() is not None:
                temp = temp.get_next()
            temp.set_next(new_node)
            new_node.set_next(None)

    def printll(self):
        if self.root is not None:
            temp = self.root
            while temp != None:
                print(temp.get_data(), '-> ', end='')
                temp = temp.get_next()
            print()
        else:
            print('Empty linked list')

def addLL(l1, l2):
    l1_ptr = l1.get_root()
    l2_ptr = l2.get_root()
    res = LinkedList()
    sum, carry = 0, 0
    while l1_ptr is not None or l2_ptr is not None:
        if l1_ptr is not None:
            l1_data = l1_ptr.get_data()
        else:
            l1_data = 0
        if l2_ptr is not None:
            l2_data = l2_ptr.get_data()
        else:
            l2_data = 0
        sum = l1_data + l2_data + carry
        if sum > 9:
            digit = sum%10
            carry = int(sum/10)
            res.insert(digit)
        else:
            res.insert(sum)
            carry = 0
        if l1_ptr is not None:
            l1_ptr = l1_ptr.get_next()
        if l2_ptr is not None:
            l2_ptr = l2_ptr.get_next()
    if carry != 0:
        res.insert(carry)
    return res

def createLL():
    int1, int2 =0,0
    l1 = LinkedList()
    l2 = LinkedList()
    if int1 !=0 and int2 !=0:
        while int1 != 0:
            l1.insert(int1%10)
            int1 = int(int1 / 10)
        while int2 != 0:
            l2.insert(int2%10)
            int2 = int(int2/10)
    elif int1 == 0 and int2 == 0:
        print('What is the point? ')
        exit()
    elif (int1 == 0 and int2 < 10) or (int1 < 10 and int2 == 0):
        l1.insert(int1)
        l2.insert(int2)

    print('List1: ')
    l1.printll()
    print('List2')
    l2.printll()
    res = addLL(l1, l2)
    print('result', )
    res.printll()

createLL()