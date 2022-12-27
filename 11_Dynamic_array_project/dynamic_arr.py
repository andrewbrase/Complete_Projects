import ctypes

class DynamicArray(object):
    def __init__(self):
        self.n = 0 # count of elements in array
        self.capacity = 1 # max elements
        self.A_arr = self.make_array(self.capacity) # creates an array with a cap of 1

    def __len__(self):
        '''Returns n number of elements stored in array'''
        return self.n

    def __str__(self):
        if self.n >= 1:
            return str([e for e in self.A_arr])
        else:
            return '[]'

    def __getitem__(self, i):
        '''Returns element from index i of A_arr'''
        if not 0 <= i < self.n:
        # if the index you pass in is not between 0 and amount of elements in array
            return IndexError(f'Error: index {i} not in arr')
        return self.A_arr[i]
    
    def append(self, data):
        '''Adds element (data) to the end of the array'''
        if self.n == self.capacity:
        # if the count of elements is == to the capacity
        # the capacity will be doubled
            self.resize(2 * self.capacity)
        self.A_arr[self.n] = data # set last element to data
        self.n += 1 # count is increased by one 
    
    def resize(self, new_capacity):
        '''Resize the internal array to the new_capacity'''
        B_arr = self.make_array(new_capacity) # create a second array with larger cap than A
        for i in range(self.n):
            B_arr[i] = self.A_arr[i] # every element pointer in A is copied over to B
        self.A_arr = B_arr # set A to = B
        self.capacity = new_capacity # set cap to larger cap 

    def make_array(self, new_capacity):
        """
        Create a new array with a capacity of `new_capacity` elements, using the `ctypes` module.

        Args: 
        new_capacity (int): The size of the array to create.

        Returns:
        A pointer to the first element in the newly created array.
        """
        return (new_capacity * ctypes.py_object)()


my_dynamic_arr = DynamicArray()

print(my_dynamic_arr) # ---> []

print(len(my_dynamic_arr)) # ---> 0

print(my_dynamic_arr[0]) # ---> Error: index 0 not in arr

my_dynamic_arr.append('T')
my_dynamic_arr.append('E')
my_dynamic_arr.append('S')
my_dynamic_arr.append('T')

print(len(my_dynamic_arr)) # ---> 4

print(my_dynamic_arr) # ---> ['T', 'E', 'S', 'T']

print(my_dynamic_arr[0]) # ---> T