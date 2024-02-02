n = int(input())
sequences = []
while True:
    sequence = input()
    if sequence == "":
        break
    sequence = sequence.split()
    if n > 0:
        sequence_max = max(map(int, sequence))
        sequences.append(sequence_max)
        n -= 1
result = sorted(sequences, reverse=True)
result_string = ";".join(map(str, result))
print(result_string)
