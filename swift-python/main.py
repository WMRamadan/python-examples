import swift_module

def main():
    print("Swift Add Function:", swift_module.add(28, 42))

    print("Swift String Length Function:", swift_module.strlen('Compute the length of this string!'))

    print("Swift Custom Function:", swift_module.custom_function('World!'))

if __name__ == "__main__":
    main()