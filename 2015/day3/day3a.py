data_list = []
with open("puzzle.txt") as f:
    data_list = list(f.read().strip())

visited_houses = set()
x, y = 0, 0

visited_houses.add((x, y))

for list in data_list:
    if list == "^":
        y += 1
    if list == "v":
        y -= 1
    if list == ">":
        x += 1
    if list == "<":
        x -= 1

    visited_houses.add((x, y))

print(len(visited_houses))
