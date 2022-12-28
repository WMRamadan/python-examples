'''
The pickle module implements binary protocols for serializing and de-serializing a
Python object structure. Pickling is the process where a Python object is converted
into a byte stream, and unpickling is the inverse operation, where a byte stream is
converted back into an object. Pickling is also known as serialization, marshaling,
or flattening.

Warning: The pickle module is not secure. Only unpickle data you trust.
'''
import pickle


class my_class:
    number_data = 3
    string_data = "hello"
    list_data = [1,2,3]
    dict_data = {"first": "a", "second": 2, "third": [1,2,3]}
    tuple_data = (11, 22)


my_object = my_class()
print(f"This is the original object:\n{my_object.dict_data}\n")

# Pickle data into a byte string object in serialized format
my_byte_string_pickled_object = pickle.dumps(my_object)
print(f"This is my byte string pickled object:\n{my_byte_string_pickled_object}\n")

with open('data.pickle', 'wb') as file:
    # Pickle data into a file object in serialized format
    my_file_pickled_object = pickle.dump(my_object, file)
    print(f"File pickled object saved to:\n{file}\n")

my_object.dict_data = None
print(f"This is the original object after modification:\n{my_object.dict_data}\n")

# Convert byte serialized format back to orginal data type
my_byte_string_unpickled_object = pickle.loads(my_byte_string_pickled_object)
print(f"dict_data of unpickled object:\n{my_byte_string_unpickled_object.dict_data}\n")

with open('data.pickle', 'rb') as file:
    # Convert file serialized format back to orginal data type
    my_file_unpickled_object = pickle.load(file)
    print(f"This is my file unpickled object:\n{my_file_unpickled_object.dict_data}\n")
