import core,pygame,easygui
from pygame.locals import *
pygame.init()
sc = pygame.display.set_mode((650, 650))
sc.fill((255, 255, 255))
pygame.display.set_caption("五子棋")
pygame.mixer.init()

board = pygame.image.load('img/board.png')
black = pygame.image.load('img/black.png')
white = pygame.image.load('img/white.png')
icon = pygame.image.load('img/icon.png')
bg = pygame.image.load('img/bg.png')
pygame.display.set_icon(icon)
color = 0
colorWarn = False

def handleEvent():
    global color,colorWarn
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            if not core.win and not core.warn:
                track1 = pygame.mixer.music.load('music/chessPlace.mp3')
                pygame.mixer.music.play()
            else:
                print(1)
            if not colorWarn:
                if color == 1:
                    color = 0
                else:
                    color = 1
            else:
                colorWarn = False
            x = int((event.pos[0]-55)/35)
            y = int((event.pos[1]-57)/35)
            core.chess(x,y,color)

sc.blit(bg,(0,0))
sc.blit(board,(50,50))

def chessPlace():
    global colorWarn
    for index, i in enumerate(core.list):
        if i[2] == 0:
            sc.blit(white,(i[0]*35+55,i[1]*35+57))
        if i[2] == 1:
            sc.blit(black,(i[0]*35+55,i[1]*35+57))
    if core.warn:
        track2 = pygame.mixer.music.load('music/warn.mp3')
        pygame.mixer.music.play()
        core.warn = False
        colorWarn = True

while True:
    handleEvent()
    chessPlace()
    pygame.display.update()
    if core.win:
        if core.winPlayer == 0:
            box = easygui.buttonbox("白方胜利！","结束",["关闭程序","重新开始"])
        if core.winPlayer == 1:
            box = easygui.buttonbox("黑方胜利！","结束",["关闭程序","重新开始"])
        if box == "关闭程序":
            pygame.quit()
        if box == "重新开始":
            sc.blit(board, (50, 50))
            color = 1
            core.init()
