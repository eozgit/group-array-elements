import pytest
from group import group_array_elements


def test_sample():
    assert group_array_elements([1, 2, 3, 4, 5], 3) == [[1, 2], [3, 4], [5]]


def test_equal_element_and_group_count():
    assert group_array_elements([1, 2, 3, 4], 4) == [[1], [2], [3], [4]]


def test_no_remainder():
    assert group_array_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [
        [1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_uneven():
    assert group_array_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 2) == [
        [1, 2, 3, 4, 5], [6, 7, 8, 9]]


def test_invalid_group_count():
    with pytest.raises(Exception) as ex:
        group_array_elements([], -1)

    assert str(ex.value) == 'group_count must be a positive integer'


def test_invalid_element_count():
    with pytest.raises(Exception) as ex:
        group_array_elements([1, 2], 3)

    assert str(ex.value) == 'not enough elements to group'
