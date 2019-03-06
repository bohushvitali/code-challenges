def solution(distance, falls):
    if len(falls) == 1 and falls[0] and distance == 1:
        return 0
    elif len(falls) < distance:
        return -1
    positions = set(range(1, distance + 1))
    for minute, pos in enumerate(falls):
        if pos in positions:
            positions.remove(pos)
            if not positions:
                return minute
    return -1