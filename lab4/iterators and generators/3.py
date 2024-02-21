def divisible_by_3_and_4(start, end):
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

start = 0
end = 20

for number in divisible_by_3_and_4(start, end):
    print(number)
