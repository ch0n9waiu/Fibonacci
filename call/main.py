import sys

sys.path.append("..")
from fibo import funFibo

def main():
    while True:
        try:
            n = int(input("Enter the n: "))
            if n <= 0:
                raise ValueError
            else:
                print(funFibo(n))
            break
        except ValueError:
            print('Must be a integer bigger than one')

if __name__ == '__main__':
    main()