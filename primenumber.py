def prime_number(num):
    if num <= 1:
        print("Not A Prime Number")
    for i in range(2,num-1):
        if num%i == 0:
            print("Not A Prime Number")
            break
    else:
        print("Prime Number")


if __name__ == '__main__':
    prime_number(897)


