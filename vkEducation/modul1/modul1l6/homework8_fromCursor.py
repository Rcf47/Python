n = int(input())
max_values = [max(map(int, input().split())) for _ in range(n)]
print(";".join(map(str, sorted(max_values, reverse=True))))
