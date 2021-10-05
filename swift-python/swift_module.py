import ctypes

swift_module = ctypes.CDLL('/usr/local/lib/python3.8/lib-dynload/libswift_module.so')
swift_module.add.argtypes = (ctypes.c_int, ctypes.c_int)
swift_module.strlen.argtypes = (ctypes.c_char_p,)
swift_module.custom_function.argtypes = (ctypes.c_char_p,)
swift_module.custom_function.restype = ctypes.c_char_p

def add(x,y):
    result = swift_module.add(ctypes.c_int(x), ctypes.c_int(y))
    return int(result)

def strlen(x):
    y = ctypes.c_char_p(x.encode())
    return swift_module.strlen(y)

def custom_function(x):
    y = ctypes.c_char_p(x.encode())
    return swift_module.custom_function(y).decode()
