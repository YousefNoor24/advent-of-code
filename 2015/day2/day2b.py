data_list = []
total_ribbon_ft = 0

with open("puzzle.txt") as file:
    for line in file:
        data_list.append(line.strip())


for data in data_list:
    paper = data.split("x")
    l = int(paper[0])
    w = int(paper[1])
    h = int(paper[2])
    a, b, _ = sorted([l, w, h])

    wrap = (a*2) + (b*2)
    bow = l*w*h

    total_ribbon_ft += (wrap + bow)


print(total_ribbon_ft)
