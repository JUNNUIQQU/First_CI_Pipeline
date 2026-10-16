import importlib

module = importlib.import_module("24_merge_sorted_lists")
merge_sorted_lists = module.merge_sorted_lists


def test_normal_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]


def test_empty_lists():
    assert merge_sorted_lists([], []) == []


def test_first_list_empty():
    assert merge_sorted_lists([], [1, 2]) == [1, 2]


def test_second_list_empty():
    assert merge_sorted_lists([1, 2], []) == [1, 2]


def test_duplicates():
    assert merge_sorted_lists([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]


def test_negative_numbers():
    assert merge_sorted_lists([-3, 0], [-2, 1]) == [-3, -2, 0, 1]