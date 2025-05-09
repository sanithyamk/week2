from collections import Counter

def are_anagrams(str1, str2):
    return Counter(str1) == Counter(str2)


print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world")) 
