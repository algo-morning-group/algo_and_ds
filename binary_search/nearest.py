def binary_search_nearest(arr, target):
    if len(arr) == 0:
        return -1

    b = 0
    e = len(arr) - 1

    while b + 1 < e:
        m = b + (e - b) // 2

        if arr[m] == target:
            return m
        if arr[m] < target:
            b = m
        else:
            e = m

    return b if abs(arr[b] - target) < abs(arr[e] - target) else e


if __name__ == '__main__':
    arr = [1, 2, 10, 17, 22, 46, 78]
    assert 2 == binary_search_nearest(arr, 11)
    assert 3 == binary_search_nearest(arr, 16)
    assert -1 == binary_search_nearest([], 16)
    assert 0 == binary_search_nearest(arr, 0)
    assert 6 == binary_search_nearest(arr, 100)
    assert 0 == binary_search_nearest(arr, 1)
    print('Passed')
