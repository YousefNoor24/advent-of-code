data_list = []
floor_num = 0

with open("day1.txt", "r") as f:
    for line in f:
        processed_line = list(line.strip())
        data_list = processed_line

for floor in data_list:
    if floor == '(':
        floor_num += 1
    if floor == ')':
        floor_num -= 1

print(f"Floor Number: {floor_num}")


