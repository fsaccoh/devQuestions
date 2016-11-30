def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
        return output

# Remove duplicates from this list.
values = [1, 3, 7, 7, 8, 9, 9, 9, 10]
result = remove_duplicates(values)
print(result)


