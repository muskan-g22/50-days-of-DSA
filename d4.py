# Given two strings s and t, return True if t is an anagram of s, otherwise return False.

def isanagram(s,t):
    if len(s)!=len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char,0)+1
    for char in t:
        if char not in count:
            return False
        count[char] -=1
        if count[char] <0:
            return 0
    return True

char1= input("enter first string : ")
char2= input("enter other string : ")
print(isanagram(char1,char2))