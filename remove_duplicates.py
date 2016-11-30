def remove_duplicates(lst):
    lst.sort()
    i = len(lst) - 1
    while i > 0:  
        if lst[i] == lst[i - 1]:
            lst.pop(i)
        i -= 1
    return lst

# Remove duplicates from this list.
lst = [1, 3, 7, 7, 8, 9, 9, 9, 10]
result = remove_duplicates(lst)
print(result)


