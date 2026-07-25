# A string s consisting of only uppercase English letters.
# An integer k.
# You can change at most k characters into any other uppercase letter.
# Return the length of the longest substring that can be made of the same character.

def replacement(s,k):
    count={}
    left,max_freq,answer=0,0,0
    for right in range(len(s)):
        count[s[right]]=count.get(s[right],0)+1
        max_freq = max(max_freq,count[s[right]])
        while (right-left+1)-max_freq>k:
            count[s[left]] -=1
            left +=1
        answer=max(answer,right-left+1)
    return answer




s=input("enter string UPPERCASE letter : ")
k=int(input("enter no. of replacement you need: "))
print(replacement(s,k))