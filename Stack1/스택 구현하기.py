stack = []
def push(item):
    stack.append(item)
    return

def pop():
    L = stack.pop()
    print(L)
    return

push(1)
push(2)
push(3)
pop()
pop()
pop()
