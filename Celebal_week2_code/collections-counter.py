#calculate the total earned amount
from collections import Counter

n = int(input())  # Number of items
items = list(map(int, input().split()))

# Count frequencies of items
item_counts = Counter(items)

m = int(input())  # Number of unique item-price entries
item_prices = {}

for _ in range(m):
    item, price = map(int, input().split())
    item_prices[item] = price

total_cost = 0
for item, count in item_counts.items():
    total_cost += count * item_prices.get(item, 0)

print(total_cost)
