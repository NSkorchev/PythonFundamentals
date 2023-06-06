# Read user input
def merge_el(element, start, end):
    merge_result = ""
    for idx in range(start, end + 1):
        merge_result += element[idx]

    return merge_result


words = input().split()
# Logic
while True:
    line = input()
    if line == "3:1":
        break

    command, first_arg, second_arg = line.split()

    if command == "merge":
        start_idx = int(first_arg)
        end_idx = int(second_arg)

        start_idx = max(0, start_idx)
        end_idx = min(len(words) - 1, end_idx)

        if start_idx >= end_idx:
            continue

        merged_el = merge_el(words, start_idx, end_idx)
        remove_count_ops = end_idx - start_idx + 1
        for _ in range(remove_count_ops):
            words.pop(start_idx)
        words.insert(start_idx, merged_el)

    elif command == "divide":
        el_idx = int(first_arg)
        partitions = int(second_arg)

        element = words[el_idx]
        element_parts = []
        partition_size = len(element) // partitions

        current_partition = ""
        for idx in range((partitions - 1) * partition_size):
            current_partition += element[idx]
            if len(current_partition) == partition_size:
                element_parts.append(current_partition)
                current_partition =""

        current_partition = ""
        for idx in range((partitions - 1) * partition_size, len(element)):
            current_partition += element[idx]

        element_parts.append(current_partition)

        words.pop(el_idx)
        for idx in range(len(element_parts)):
            words.insert(el_idx + idx, element_parts[idx])

# Output
print(" ".join(words))
