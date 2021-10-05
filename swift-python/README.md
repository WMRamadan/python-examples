We first compile the library:
swiftc -emit-library swift_module.swift

Then we copy the library to our share libraries directory:
cp libswift_module.so /usr/local/lib/python3.8/lib-dynload/

Now copy the "swift_module.py" python module to the following path:
cp swift_module.py /usr/local/lib/python3.8/site-packages/

Execute the python file:
python3 main.py