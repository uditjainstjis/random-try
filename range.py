def find_odd_numbers(n):
    odd_numbers = [num for num in range(n + 1) if num % 2 != 0]
    return odd_numbers

# Example usage:
n = int(input("Enter a number: "))
odd_numbers = find_odd_numbers(n)
print(f"Odd numbers from 0 to {n}: {odd_numbers}")
