def make_subtotal_node(tree):
    bucket = []
    stack = []
    for t in tree:
        if t == "0":
            stack.append(0)
        else:
            a = 1
            while True:
                if stack[-1] == 0:
                    break
                a += stack.pop()
            stack[-1] = a
            bucket.append(a)
    bucket.append(sum(stack))
    return bucket


for t in range(1, int(input())+1):
    subtotal_of_nodes_A = make_subtotal_node(input())
    subtotal_of_nodes_B = make_subtotal_node(input())

    print('01'[sorted(subtotal_of_nodes_A) == sorted(subtotal_of_nodes_B)])



