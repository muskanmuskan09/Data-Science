from itertools import combinations

def sublist_generator(lst, n):
    for sublist in combinations(lst, n):
        yield list(sublist)

# Test sublist generator
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for sublist in sublist_generator(lst, 3):
    print(sublist)
