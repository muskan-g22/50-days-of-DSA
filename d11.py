# Given a string s, find the length of the longest substring without repeating characters.

def longestSubstring(s):
    max_length = 0
    char_set = set()
    left = 0
    for right in range (len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left +=1
        char_set.add(s[right])
        max_length = max( max_length , right -left +1)
    return max_length

strr=input("enter a string : ")
print("length of longest substring without repeating character is ",longestSubstring(strr))
