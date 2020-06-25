def pre_order(node):
    print(node, end="")
    if bucket[node][0] != ".":
        pre_order(bucket[node][0])
    if bucket[node][1] != ".":
        pre_order(bucket[node][1])


def in_order(node):
    if bucket[node][0] != ".":
        in_order(bucket[node][0])
    print(node, end="")
    if bucket[node][1] != ".":
        in_order(bucket[node][1])


def post_order(node):
    if bucket[node][0] != ".":
        post_order(bucket[node][0])
    if bucket[node][1] != ".":
        post_order(bucket[node][1])
    print(node, end="")


n = int(input())
bucket = {}
for _ in range(n):
    root, l, r = input().split()
    bucket[root] = [l, r]


pre_order("A")
print()
in_order("A")
print()
post_order("A")
