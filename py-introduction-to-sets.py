def average(array):
    # your code goes here
    h = set(arr)
    return f"{sum(h) / len(h):.3f}"
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
