import ctypes

# Load the shared library
mylib = ctypes.CDLL("./mylib.so")

# Call the exported Go function
mylib.SayHello()
