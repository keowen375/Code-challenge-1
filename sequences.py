def remove_duplicates(sequence):
    special_items = set()
    new_item = []

    for item in sequence:
        if item not in special_items:
            special_items.add(item)
            new_item.append(item)

    return new_item

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)