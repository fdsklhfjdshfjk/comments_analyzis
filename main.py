

def main():
    a = int(input())
    b = int(input())

    op = input()

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a/b)
    else:
        print("неизвестная операция")

main()