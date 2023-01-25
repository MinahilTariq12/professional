def return_count_even(n):
    count = 0
    for i in arr:
        if i % 2 == 0:
            count += 1
    return count
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(return_count_even(arr))
