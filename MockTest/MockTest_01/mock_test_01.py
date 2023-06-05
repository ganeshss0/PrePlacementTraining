############ Solution ############

def move_zero_2_end(nums: list[int]) -> None:
    '''Moves all zeros in nums to end of list, keeps order of non-zero element unchanged.'''

    i = zeros = 0
    n = len(nums)

    while i < n:
        if nums[i] == 0:
            nums.pop(i)
            n -= 1
            zeros += 1
        else:
            i += 1
    else:
        nums += [0] * zeros



############ testing #############
if __name__ == '__main__':

    test_cases = [
        [0, 1, 0, 3, 12],
        [1, 11, 0, 0, 11], 
        [3, 2, 1, 1, 0],
        [0, 0, 0, 1],
        [1],
        []
    ]

    for test in test_cases:
        print('_'*25)
        print('Input:', test)
        move_zero_2_end(test)
        print('nums:', test)