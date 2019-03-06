import sys

def solution(A):
    min_price = sys.maxsize
    max_profit = 0
    for a in A:
        min_price = min([min_price, a])
        max_profit = max([max_profit, a - min_price])
    return max_profit