# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int, input().split()))
b = int(input())
isSuperset = True
for _ in range(b):
    s = set(map(int, input().split()))
    if not a.issuperset(s):
        isSuperset = False
        break
print(isSuperset)