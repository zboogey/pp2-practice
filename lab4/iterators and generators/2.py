def even_numbers_up_to_n(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number (n): "))

even_numbers = even_numbers_up_to_n(n)

print("Even numbers between 0 and", n, ":", end=" ")
for number in even_numbers:
    print(number, end=", ")

