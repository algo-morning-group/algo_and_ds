def binary_search_exact_match(arr, target):
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

    if arr[b] == target: return b
    if arr[e] == target: return e
    return -1


if __name__ == '__main__':
    arr = [1, 2, 10, 17, 22, 46, 78]
    assert -1 == binary_search_exact_match(arr, 11)
    assert -1 == binary_search_exact_match(arr, 16)
    assert -1 == binary_search_exact_match([], 16)
    assert -1 == binary_search_exact_match(arr, 0)
    assert -1 == binary_search_exact_match(arr, 100)
    assert 0 == binary_search_exact_match(arr, 1)
    assert 3 == binary_search_exact_match(arr, 17)
    assert 6 == binary_search_exact_match(arr, 78)
    print('Passed')
