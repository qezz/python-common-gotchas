class LinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        res = "["
        current = self
        while current != None:
            # current =
            res = res + str(current.get())
            if current.next != None:
                res = res + ", "
            current = current.next
        return res + "]"

    def get(self):
        return self.value

    def tail(self):
        return self.next

    def append(self, value):
        current = self
        print("to append:", value)
        while current.next != None:
            print("curr:", current.value)
            current = current.next
        current.next = LinkedList(value)

    def recur_reverse(self):
        head = self.get()
        tail = self.tail()
        # print("(", head, " . ", tail, ")", sep="")
        if tail != None:
            reversed_tail = tail.recur_reverse()
            # print("temp reversed tail is:", reversed_tail)

            reversed_tail.append(head)
            return reversed_tail
        else:
            return LinkedList(head)

    def linear_rev(self):
        # get first two values
        fst = self.get()

        new_node = LinkedList(fst)

        curr_ll = self.next

        while curr_ll != None:
            curr_val = curr_ll.get()
            old_node = new_node
            new_node = LinkedList(curr_val)
            new_node.next = old_node
            # print(new_node)
            curr_ll = curr_ll.next

        return new_node


ll = LinkedList(0)
ll.append(1)
ll.append(2)
ll.append(3)
print(ll)
llr = ll.recur_reverse()
print(" recur:", llr)
llr2 = ll.linear_rev()
print("linear:", llr2)
