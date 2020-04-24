def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def get_prime(max_prime):
    prime_list = []
    for i in range(2, max_prime):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


prime = int(input("Enter the maximum prime to find: "))
prime = get_prime(prime)

for num in prime:
    print(num, end=" ")
