list = []
win = False
winPlayer = -1
warn = False
for y in range(0,15):
    for x in range(0,15):
        list.append([x,y,-1])
print("---init finished---")

def chess(x,y,color):
    global list,win,winPlayer,warn
    if win:
        print("it's over.")
        return
    a = int(x)
    b = int(y)
    c = int(color)
    for index,i in enumerate(list):
        if a == i[0] and b == i[1] and i[2] == -1:
            list.remove([a,b,i[2]])
            list.insert(index,[a,b,c])
            #print(list)
            break
        elif index == 224:
            warn = True
            print(warn)
    for index,i in enumerate(list):
        if i[2] != -1:
            try:
                if list[index][2] == list[index+1][2] == list[index+2][2] == list[index+3][2] == list[index+4][2] or\
                   list[index][2] == list[index+15][2] == list[index+30][2] == list[index+45][2] == list[index+60][2] or\
                   list[index][2] == list[index+16][2] == list[index+32][2] == list[index+48][2] == list[index+64][2] or\
                   list[index][2] == list[index+14][2] == list[index+28][2] == list[index+42][2] == list[index+56][2]:
                    win = True
                    winPlayer = list[index][2]
            except:
                pass

def init():
    global list,win,winPlayer
    list = []
    win = False
    winPlayer = -1
    for y in range(0, 15):
        for x in range(0, 15):
            list.append([x, y, -1])
    print("---init finished---")


def test():
    return "sssss"
