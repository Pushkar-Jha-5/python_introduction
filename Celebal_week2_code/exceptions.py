#implementing exception handling
# Read number of test cases
n = int(input())

for _ in range(n):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except Exception as e:
        print("Error Code:", e)
