from lab import deduplicate

def test_nominal():
    lst = [1,2,3,4]
    new_lst = deduplicate(lst)
    assert new_lst == [1,2,3,4]

def test_emplty_lst():
    lst = []
    new_lst = deduplicate(lst)
    assert new_lst == []

def test_deduplicate_lst():
    lst = [1,2,1,3,3,4]
    new_lst = deduplicate(lst)
    assert new_lst == [1,2,3,4]

