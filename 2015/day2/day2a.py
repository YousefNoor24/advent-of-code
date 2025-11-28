data_list = []
total_sq_ft = 0

with open("puzzle.txt") as file:
    for line in file:
        data_list.append(line.strip())


for data in data_list:
    paper = data.split("x")
    l = int(paper[0])
    w = int(paper[1])
    h = int(paper[2])
    surface_area = (2*l*w) + (2*w*h) + (2*h*l)
    smallest_side = min(l*w, w*h, h*l) 

    total_sq_ft += (surface_area + smallest_side)

print(total_sq_ft)
