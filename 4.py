
sorted_list = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6]
deduplicated_list = []

for item in sorted_list:
    if item not in deduplicated_list:
        deduplicated_list.append(item)

print(deduplicated_list)  # Output: [1, 2, 3, 4, 5, 6]