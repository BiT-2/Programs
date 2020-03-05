def longestPalindrome( s: str) -> str:
        if len(s) < 1:
            return ''
        elif len(s) == 1:
            return s
        else:
            substr_list = []
            palindrome_list = []
            for i in range(0, len(s)):
                for j in range(i + 1, len(s) + 1):
                    substr_list.append(s[i:j])
            for substr in substr_list:
                if len(substr) > 1:
                    if isPalindrome(substr) == True:
                        palindrome_list.append(substr)
            if not palindrome_list:
                return substr_list[0]
            else:
                return max(palindrome_list, key=len)


def isPalindrome(string1: str):
    palindrome = False
    if len(string1) % 2 == 0:
        i = int(len(string1) / 2) - 1
        j = int(len(string1) / 2)
        while i >= 0 and j < len(string1):
            if string1[i] == string1[j]:
                i = i - 1
                j = j + 1
                palindrome = True
            else:
                palindrome = False
                break

    elif len(string1) % 2 != 0:
        i = int(len(string1) / 2) - 1
        j = int(len(string1) / 2) + 1
        while i >= 0 and j < len(string1):
            if string1[i] == string1[j]:
                palindrome = True
                i = i - 1
                j = j + 1
            else:
                palindrome = False
                break
    return palindrome

print(longestPalindrome(s = 'ababa'))

def longestPalindromeElegantSolution(string1):
    if len(string1) <1:
        return ''
    start_index, end_index = 0,0
    for i in range(0, len(string1)):
        len1 = expand(string1, i, i)
        len2 = expand(string1,i,i+1)
        length = max(len1, len2)
        if length> end_index - start_index:
            start_index = i - int((length-1)/2)
            end_index = i + int(length/2)
    return string1[start_index: end_index + 1]

def expand(string1, start_index, end_index):
    left_index = start_index
    right_index = end_index
    str_length = len(string1)
    while left_index >= 0 and right_index < str_length:
        if string1[left_index] == string1[right_index]:
            left_index = left_index - 1
            right_index = right_index +1
        else:
            break
    return right_index - left_index -1

print(longestPalindromeElegantSolution('ababa'))



