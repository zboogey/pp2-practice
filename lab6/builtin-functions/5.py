def all_true_elements(tup):
    return all(tup)

if __name__ == "__main__":
    my_tuple = (True, True, True, False)
    result = all_true_elements(my_tuple)
    
    if result:
        print("All elements in the tuple are true.")
    else:
        print("Not all elements in the tuple are true.")
