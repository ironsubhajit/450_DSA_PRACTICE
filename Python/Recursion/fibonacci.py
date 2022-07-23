def fibonacci(num: int):
    """Recursive function"""
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == '__main__':
    no = int(input("Enter a positive number: "))
    if no < 0:
        raise ValueError("Can not be a negative number")

    for i in range(no):
        print(fibonacci(i), end=" ")