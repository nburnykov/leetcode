from design_hash_map.app_hashmap import MyHashMap


def test_case_1():
    mhm = MyHashMap()
    assert mhm.get(100) == -1
    mhm.put(10, 10)
    assert mhm.get(10) == 10
    mhm.remove(10)
    assert mhm.get(10) == -1