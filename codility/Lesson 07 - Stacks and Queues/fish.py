from itertools import izip

def solution(sizes, directions):
    stack = []

    escaped = 0

    for size, direction in izip(sizes, directions):
        if direction == 0:
            if stack:
                while stack and stack[-1] < size:
                    stack.pop()
                if not stack:
                    # OMG, that fish ate all the fishes going upstream!
                    escaped += 1
            else:
                escaped += 1
        else:
            stack.append(size)

    return len(stack) + escaped
