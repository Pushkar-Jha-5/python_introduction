#task based on discard(),remove() & pop()
# Number of elements in the set
n = int(input())

# Initial set elements
s = set(map(int, input().split()))

# Number of operations
num_ops = int(input())

# Perform each operation
for _ in range(num_ops):
    cmd = input().split()
    
    if cmd[0] == "pop":
        s.pop()
    elif cmd[0] == "remove":
        try:
            s.remove(int(cmd[1]))
        except KeyError:
            pass
    elif cmd[0] == "discard":
        s.discard(int(cmd[1]))

# Output the sum of the remaining set elements
print(sum(s))
