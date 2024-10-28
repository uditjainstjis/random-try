def print_perfect_numbers(a, b):
    for num in range(a, b + 1):
        if num > 1:
            divisors_sum = 1
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    divisors_sum += i
                    if i != num // i:
                        divisors_sum += num // i
            if divisors_sum == num:
                print(num, end=" ")
a=int(input())
b=int(input())
print_perfect_numbers(a,b)