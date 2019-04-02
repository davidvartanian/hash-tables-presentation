import random


class Node:
    """
    LinkedList node implementation
    """
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value


class LinkedList:
    """
    LinkedList example implementation
    """
    def __init__(self):
        self.head = None

    def add(self, node):
        """
        Add element to the linked list
        :param node:
        :return:
        """
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def get_list(self):
        """
        Generate a list of elements contained in the linked list
        :return:
        """
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def find(self, key):
        """
        Find an element based on a key (particular implementation only for example purposes
        :param key:
        :return:
        """
        for n in self.get_list():
            assert 'name' in n.value, 'invalid node value'
            if n.value['name'] == key:
                return n
        return None

    def __str__(self):
        """
        String representation of the linked list
        :return:
        """
        return ' > '.join([str(x.value) for x in self.get_list()])


class HashTable:
    """
    Example of closed addressing hash table implementation
    """
    data = dict()

    def __init__(self, m: int):
        self.m = m
        self.p = self.__find_prime(m)
        self.a = random.choice(range(0, self.p))
        self.b = random.choice(range(0, self.p))
        self.__init_data(m)

    def __init_data(self, m: int):
        """
        Allocate linked lists into the hash table of size m
        :param m:
        :return:
        """
        for i in range(m):
            self.data[i] = LinkedList()

    def __find_prime(self, m: int):
        """
        Helper function to find a prime number
        :param m:
        :return:
        """
        assert m > 1, "m must be greater than 1"
        found = False
        x = m
        while found is False:
            x += 1
            for i in range(2, x):
                if x % x:
                    continue
                found = True
        return x

    def hash(self, key: str):
        """
        Hash function
        Returns the integer position of the table based on the Universal Hashing Method
        :param key:
        :return: int
        """
        num_key = sum([ord(x) for x in key])
        return ((self.a * num_key + self.b) % self.p) % self.m

    def insert(self, key, data):
        """
        Insert element into the correct linked list according to the key's hash
        :param key:
        :param data:
        :return:
        """
        self.data[self.hash(key)].add(Node(data))

    def search(self, key):
        """
        Look for data based on the given key
        :param key:
        :return:
        """
        ll = self.data[self.hash(key)]
        assert ll is not None, 'not found'
        return ll.find(key)

    def __str__(self):
        return "\n".join(['{}: {}'.format(k, str(self.data[k])) for k in self.data.keys()])


if __name__ == '__main__':
    ht = HashTable(10)
    ht.insert('Paul', {'name': 'Paul', 'surname': 'McCartney'})
    ht.insert('John', {'name': 'John', 'surname': 'Lennon'})
    ht.insert('Ringo', {'name': 'Ringo', 'surname': 'Starr'})
    ht.insert('George', {'name': 'George', 'surname': 'Harrison'})
    ht.insert('Mick', {'name': 'Mick', 'surname': 'Jagger'})
    ht.insert('Curt', {'name': 'Curt', 'surname': 'Cobain'})
    ht.insert('Jimi', {'name': 'Jimi', 'surname': 'Hendrix'})
    ht.insert('Bob', {'name': 'Bob', 'surname': 'Dylan'})
    ht.insert('David', {'name': 'David', 'surname': 'Bowie'})


    print('Hash Table:')
    print(ht)