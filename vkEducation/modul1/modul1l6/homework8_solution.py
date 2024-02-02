n = int(input("Введите количество записей: "))
sequences = []
for _ in range(n):
    sequence = input("Введите последовательность: ").split()
    max_value = max(map(int, sequence))
    sequences.append(max_value)

while True:
    sequence = input("Введите последовательность или нажмите Enter для завершения: ")
    if sequence == "":
        break
    max_value = max(map(int, sequence.split()))
    sequences.append(max_value)

result = sorted(sequences, reverse=True)
result_str = ";".join(map(str, result))
print("Максимальные значения:", result_str)
