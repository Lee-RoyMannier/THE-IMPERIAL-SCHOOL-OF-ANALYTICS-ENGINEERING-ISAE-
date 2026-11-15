from lab import two_sum

def test_nominal():
    lst = [1,2,3,4,5]
    result = two_sum(lst,7)
    
    assert result == (2,3)

def test_without_solution():
    lst = [1,2,3,4,5]
    result = two_sum(lst,743)
    
    assert result == None


def test_two_sum_same_element_not_allowed():
    nums = [3, 4, 5]
    target = 6

    result = two_sum(nums, target)

    assert result is None

def test_two_sum_duplicates():
    nums = [3, 3]
    target = 6

    assert two_sum(nums, target) == (0, 1)

