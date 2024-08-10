# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())  
A = input().split()  
B = input().split()  

word_indices = defaultdict(list)  

for i, word in enumerate(A):
    word_indices[word].append(i + 1)  

for word in B:
    if word in word_indices:
        print(' '.join(map(str, word_indices[word])))  
    else:
        print(-1)
