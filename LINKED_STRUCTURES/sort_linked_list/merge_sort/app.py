def merge_sort_recursive(array: list) -> list:
    if len(array) == 1:
        return array
    middle = len(array) // 2

    left = merge_sort_recursive(array[:middle])
    right = merge_sort_recursive(array[middle:])

    ptr_right, ptr_left = 0, 0

    result = []
    while ptr_left < len(left) and ptr_right < len(right):
        val_left, val_right = left[ptr_left], right[ptr_right]

        if  val_left < val_right:
            result.append(val_left)
            ptr_left += 1
        else:
            result.append(val_right)
            ptr_right += 1

    result.extend(left[ptr_left:] or right[ptr_right:])

    return result

def merge_sort_iterative(array: list):
    step, max_step = 2, 2
    while max_step < len(array):
        max_step *= 2

    while step <= max_step:
        middle = step // 2
        for i in range(0, len(array), step):

            left = array[i: i+middle]
            right = array[i+ middle: i + step]

            ptr_left, ptr_right = 0, 0
            result = []

            while ptr_left < len(left) and ptr_right < len(right):
                val_left, val_right = left[ptr_left], right[ptr_right]

                if val_left < val_right:
                    result.append(val_left)
                    ptr_left += 1
                else:
                    result.append(val_right)
                    ptr_right += 1

            result.extend(left[ptr_left:] or right[ptr_right:])
            array[i:i+len(result)] = result

        step *= 2


