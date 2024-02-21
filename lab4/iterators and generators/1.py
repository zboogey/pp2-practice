def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2

N = 5
squares_up_to_N = square_generator(N)

for square in squares_up_to_N:
    print(square)
