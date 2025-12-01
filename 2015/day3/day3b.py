data_list = []
with open("puzzle.txt") as f:
    data_list = list(f.read().strip())

visited_houses = set()
santa_x, santa_y = 0, 0
robo_x, robo_y = 0, 0

visited_houses.add((santa_x, santa_y))

for i, list in enumerate(data_list):
    if i % 2 == 0:
        if list == "^":
            santa_y += 1
        if list == "v":
            santa_y -= 1
        if list == ">":
            santa_x += 1
        if list == "<":
            santa_x -= 1
        visited_houses.add((santa_x, santa_y))
    else:
        if list == "^":
            robo_y += 1
        if list == "v":
            robo_y -= 1
        if list == ">":
            robo_x += 1
        if list == "<":
            robo_x -= 1
        visited_houses.add((robo_x, robo_y))


print(len(visited_houses))
