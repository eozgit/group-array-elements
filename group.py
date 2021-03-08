from typing import Any


def group_array_elements(array: list[Any], group_count: int) -> list[list[Any]]:
    """Given an array of length >= 0, and a positive integer group_count,
    returns the contents of the array divided into group_count equally sized arrays.
    Where the size of the original array cannot be divided equally by group_count,
    the final part should have a length equal to the remainder.

    Finds the minimum element count to go in each group and if there are residual elements to distribute
    Loops through the group count calculating the start and end indices to slice the array 
    from and append to the result array. In each iteration end is calculated by first 
    calculating the number of elements needed in the group and adding that to the start index. 
    The element count in a group is calculated as the sum of minimum elements per group and
    an additional 1 if the group needs to hold a remainder element which is determined by comparing
    the index of the group to the remainder of the array length divided by group count.
    The start index is set to the end index at the end of every iteration as that is where 
    slicing needs to start on the next iteration.

    :array: The array to split into groups
    :group_count: Number of groups to split the array into
    """

    if group_count < 1:
        raise Exception('group_count must be a positive integer')

    array_length = len(array)

    if array_length < group_count:
        raise Exception('not enough elements to group')

    elements_per_group = array_length // group_count
    groups_with_extra_element = array_length % group_count

    result = []
    start = 0
    for i in range(group_count):
        end = start + elements_per_group

        if i < groups_with_extra_element:
            end += 1

        result.append(array[start:end])

        start = end

    return result
