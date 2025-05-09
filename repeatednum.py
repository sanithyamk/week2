from collections import Counter

def most_frequent(lst):
    count = Counter(lst)
    return count.most_common(1)[0][0]

data = [1, 3, 2, 1, 4, 1, 3, 3, 3]
print(most_frequent(data))  #3
