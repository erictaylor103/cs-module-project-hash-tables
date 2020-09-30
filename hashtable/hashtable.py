class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

#create the linked list with an empty head
class LinkedList:
    def __init__(self):
        self.head = None

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        #self.hash_table = [None] * capacity
        self.hash_table = [LinkedList()] * capacity
        self.item_count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        #return self.hash_table
        return len(self.hash_table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.item_count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for k in key: 
            hash = (( hash << 5) + hash) + ord(k)
            
        return hash & 0xffffffff # 32 bit (8 f's)

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        #self.hash_table[index] = value
        if self.hash_table[index].head == None:
            self.hash_table[index].head = HashTableEntry(key, value)
            self.item_count += 1
            return
        
        else:
            current = self.hash_table[index].head
        
        while current.next is not None:
            if current.key == key:
                current.value = value
            current = current.next
        
        current.next = HashTableEntry(key, value)
        self.item_count += 1

        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current = self.hash_table[index].head
        removed_value = self.hash_table[index]

        #if self.hash_table[index] is None:
        #    print("The key is not in here")
        #else:
        #    self.hash_table[index] = None

        if current.key == key:
            self.hash_table[index].head = self.hash_table[index].head.next
            self.item_count += 1
            return
        
        while current.next is not None:
            previous = current
            current = current.next
            if current.key == key:
                previous.next = current.next
                current.next = None
                self.item_count -= 1
                print(f"Removed Value: {removed_value}")
                return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current = self.hash_table[index].head

        if current == None:
            return None
        
        if current.key == key:
            return current.value
        
        while current.next is not None:
            current = current.next
            if current.key == key:
                return current.value
        #if we get here it's because the key is not in the hashtable
        return None
        

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity
        new_list = [LinkedList()] * self.capacity
        print(f"MY NEW CAPACITY IS: {self.capacity} \n")

        for i in self.hash_table:
            current = i.head

            while current is not None:
                index = self.hash_index(current.key)

                if new_list[index].head == None:
                    new_list[index].head = HashTableEntry(current.key, current.value)

                else:
                    node = HashTableEntry(current.key, current.value)

                    node.next = new_list[index].head

                    new_list[index].head = node

                current = current.next
            self.hash_table = new_list


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
