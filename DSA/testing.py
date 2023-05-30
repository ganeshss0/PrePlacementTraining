
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:

    nums1[:] = nums1[:m]
    # nums2[:] = nums2[:n]
    if n == 0:
        return
    elif m == 0:
        nums1[:] = nums2[:n]
        return
    i, j = 0, 0

    while i < (m + j) and j < n:
        if nums1[i] > nums2[j]:
            nums1.insert(i, nums2[j])
            j += 1
        i += 1

    if j < n:
        nums1.extend(nums2[j:n])






if __name__ == '__main__':
    num1 = [1, 2, 3, 4, 9, 19, 111]
    # num1 = [2, 0]
    num2 = [3, 5, 6, 9]
    # num2 = [1]

    merge(
        num1,
        4,
        num2,
        3
    )

    print(num1)
