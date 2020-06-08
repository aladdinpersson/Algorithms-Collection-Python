def merge_sort(array):
    total_inversions = 0
    if len(array) <= 1:
        return (array, 0)

    midpoint = int(len(array) / 2)

    (left, left_inversions) = merge_sort(array[:midpoint])
    (right, right_inversions) = merge_sort(array[midpoint:])
    (merged_array, merge_inversions) = merge_and_count(left, right)

    return (merged_array, left_inversions + right_inversions + merge_inversions)


def merge_and_count(left, right):
    count_inversions = 0
    result = []
    left_pointer = right_pointer = 0
    left_len = len(left)
    right_len = len(right)

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] <= right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1

        elif right[right_pointer] < left[left_pointer]:
            count_inversions += left_len - left_pointer
            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return (result, count_inversions)


if __name__ == "__main__":
    array = [9, 2, 1, 5, 2, 3, 5, 1, 2, 32, 12, 11]
    print(array)

    result = merge_sort(array)
    print(result)
