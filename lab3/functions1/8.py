def spy_game(nums):
    zeros_seen = 0
    sevens_seen = False
    for num in nums:
        if num == 0:
            zeros_seen += 1
        elif zeros_seen >= 2 and num == 7:
            sevens_seen = True
            break  
    return sevens_seen

# Test cases
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # Output: True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # Output: True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # Output: False
