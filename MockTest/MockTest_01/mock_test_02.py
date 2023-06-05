############ Solution ############

def unique_character(s: str) -> int:
    '''Return the index of first non-repeating character in the string if it not exists then returns -1.'''
    chars = set()
    for i in range(len(s)):
        if s[i] not in chars:
            if s.count(s[i]) == 1:
                return i
        chars.add(s[i])

    return -1
    
############ testing #############

if __name__ == '__main__':
    test_cases = [
        'leetcode',
        'loveleetcode', 
        'aabb',
        'cocunuts',
        'duckduckgo',
        ''
    ]

    for test in test_cases:
        print('_'*25)
        print('Input:', test)
        print('Output:', unique_character(test))