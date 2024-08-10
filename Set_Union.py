# Enter your code here. Read input from STDIN. Print output to STDOUT
n_english = int(input())
english = set(map(int, input().split()))
f_english = int(input())
french = set(map(int, input().split()))
print(len(english.union(french)))
