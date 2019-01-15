class OrderedDict:
    # Constructor
    def __init__(self):
        
        # Backing field use _var name
        # Private attribute
        # "Helper function/attribute"
        # Use zip object to merge the keys and values from two collections
        self._keys = []
        self._values = []
    #Backing Methods
    def keys(self):
        return self._keys
    def values(self):
        return self._values
    
    # Magic Method __setitem__ like a setter
    def __setitem__(self, key, value):
        # Add values from self into the private key list
        self._keys.append(key)
        self._values.append(value)
        # test_set_new_items is passed
    
    # To store items
    def items(self):
        result = []
        # Add the new item by zipping the two indexed items
        for key, value in zip(self._keys, self._values):
            result.append((key, value))
        return result   
        # test_items_method is passed
    # Make the item "subscribable"
    def __getitem__(self, a_key):
        for key, value in zip(self._keys, self._values):
            if key == a_key:
                return value
        raise KeyError(repr(a_key))
    
    def __contains__(self, a_key):
        # Elegant Pythonic
        # return a_key in self._keys

        for key in self._keys:
            if key == a_key:
                return True
        return False
    
    # Returns the length of the keys dictionary
    def __len__(self):
        return len(self._keys)
    
    def __eq__(self, other):
        # Compares length of the two dicitonaries
        # This is the len function defined above ^^
        if len(self) != len(other):
            return False
        for key, value in zip(self._keys, self._values):
            # If the 'key' is not in the 'other' dictionary
            # OR the 'key' is in 'other' is not equal to the value
            if key not in other or other[key] != value:
                return False
        return True
    # test_equal_compared_to_python_dict is passed
    # test_dictionaries_are_equal is passed
    
    # String output of the data
    def __str__(self):
        s = "{"
        for key, value in zip(self._keys, self._values):
            s += "{}: {}, ".format(repr(key), repr(value))
        s = s.rstrip(", ")
        s += "}"
        return s
     # To make __repr__ the same as __str__
    __repr__ = __str__
    # test_str_and_repr is passed
    
    # __add__ function - add a new item
    def __add__(self, other):
        new = OrderedDict()
        for key, value in self.items():
            # Assigning a new key and value to the new item
            new[key] = value
        for key, value in other.items():
            # Assigning a new key and value to the new item
            new[key] = value
        return new
    # test_add_two_dicts_with_unique_keys is passed
    
    # @classmethod
    # Using the OrderedDict as a class and not an instance
    @classmethod
    def from_keys(cls, sequence):
        #New class object
        new = cls()
        for elem in sequence:
            new[elem] = None
        return new
    # test_from_keys_with_dequences is passed
    
    
    #TODOs - delete the @pytest.mark.skip decorators and complete the final three tests