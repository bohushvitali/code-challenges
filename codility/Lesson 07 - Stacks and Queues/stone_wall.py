def solution(heights):
    stack = []
    blocks = 0

    for height in heights:
        while stack and stack[-1] > height:
            stack.pop()

        if not stack or stack[-1] < height:
            stack.append(height)
            blocks += 1

    return blocks