import pygame as p
import Process
import Func

WIDTH = (80*9)+500
HEIGHT = 80*9
SQ_SIZE = 75.614
MAX_FPS = 15
IMAGES = {}
State = ""
whiteToMove = True

def LoadImage():
    pieces = ['wp', 'wK', 'wG', 'wS', 'wN', 'wL', 'wR', 'wB', 'bp', 'bK', 'bG', 'bS', 'bN', 'bL', 'bR', 'bB', 'wPS', 'wPN', 'wPL', 'wPR', 'bPS', 'bPN', 'bPL', 'bPR', 'bPB']
    for item in pieces:
        IMAGES[item] = p.transform.scale(p.image.load("img/" + item + ".png"),(70,104))
    IMAGES['bg'] = p.transform.scale(p.image.load("img/background.png"),(80*9,80*9))
    IMAGES['bhand'] = p.transform.scale(p.image.load("img/bhand.png"),(250,260))
    IMAGES['whand'] = p.transform.scale(p.image.load("img/whand.png"),(250,260))

def main():
    LoadImage()
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    logo = p.transform.scale(p.image.load('img/logo.png'),(32,32))
    p.display.set_icon(logo)
    p.display.set_caption('YuuShogi')
    clock = p.time.Clock()
    screen.fill(p.Color(218, 208, 162))
    game = Process.GameState()
    StartBtn = Func.Button()
    State = "Play"
    playerChoice = []
    i=0
    Running = True
    while (Running):
        for e in p.event.get():
            if e.type == p.QUIT:
                Running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = int((location[0]-20-250)//SQ_SIZE)
                row = int((location[1]-21)//SQ_SIZE)
                playerChoice.append([row,col])
                print(playerChoice)
                if(len(playerChoice) == 1):
                    if (game.board[playerChoice[0][0]][playerChoice[0][1]] == "--"):
                        playerChoice = []
                if (len(playerChoice) == 2):
                    if(playerChoice[0] == playerChoice[1]):
                        playerChoice = []
                    else:
                        game.board[playerChoice[1][0]][playerChoice[1][1]] = game.board[playerChoice[0][0]][playerChoice[0][1]]
                        game.board[playerChoice[0][0]][playerChoice[0][1]] = "--"
                        playerChoice = []

        DrawGame(screen,game)
        clock.tick(MAX_FPS)
        p.display.flip()

def DrawGame(screen,game):
    DrawBackGround(screen)
    DrawPieces(screen,game)

def DrawBackGround(screen):
    screen.blit(IMAGES['bg'],p.Rect(250,0,0,0))
    screen.blit(IMAGES['bhand'],p.Rect(970,460,0,0))
    screen.blit(IMAGES['whand'],p.Rect(0,0,0,0))

def DrawPieces(screen,game):
    for r in range(9):
        for c in range(9):
            piece = game.board[r][c]
            if piece != "--":
                if piece[0] == "w":
                    y=0
                else:
                    y=16
                screen.blit(IMAGES[piece],p.Rect(22+250+(c*SQ_SIZE),y+(r*SQ_SIZE),80,80))

if __name__ == "__main__":
    main()

