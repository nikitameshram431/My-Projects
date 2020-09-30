import pygame
pygame.init()
white=(255,255,255)
black=(0,0,0)
dark_green=(0,100,0)
green=(0,200,0)
forest_green=(34,139,34)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)
display_width=590
display_height=505
import time
import random


gamedisplays=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Zombie Game")
clock=pygame.time.Clock()
human=pygame.image.load('human.jpg')
backgroundpic=pygame.image.load("download12.jpg")
black_strip=pygame.image.load("strips black.jpg")
white_strip=pygame.image.load("strips white.jpg")
intro_background=pygame.image.load("background (1).jpg")
instruction_background=pygame.image.load("background (2).jpg")
zombie_width=56
pause=False

def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(intro_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',50)
        TextSurf,TextRect=text_objects("ZOMBIE GAME",largetext)
        TextRect.center=(400,100)
        gamedisplays.blit(TextSurf,TextRect)
        button("START",100,470,150,50,green,bright_green,"play")
        button("QUIT",400,470,150,50,dark_green,bright_red,"quit")
        button("INSTRUCTION",250,470,150,50,forest_green,bright_blue,"intro")
        pygame.display.update()
        clock.tick(50)


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplays,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()


    else:
        pygame.draw.rect(gamedisplays,ic,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplays.blit(textsurf,textrect)


def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',50)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',30)
        textSurf,textRect=text_objects("Try to save yourself from the zombies",smalltext)
        textRect.center=((350),(200))
        TextSurf,TextRect=text_objects("INSTRUCTION",largetext)
        TextRect.center=((295),(100))
        gamedisplays.blit(TextSurf,TextRect)
        gamedisplays.blit(textSurf,textRect)
        stextSurf,stextRect=text_objects("ARROW LEFT : LEFT TURN",smalltext)
        stextRect.center=((150),(380))
        hTextSurf,hTextRect=text_objects("ARROW RIGHT : RIGHT TURN" ,smalltext)
        hTextRect.center=((150),(410))
        atextSurf,atextRect=text_objects("A : ACCELERATOR",smalltext)
        atextRect.center=((150),(440))
        rtextSurf,rtextRect=text_objects("B : BRAKE ",smalltext)
        rtextRect.center=((150),(470))
        ptextSurf,ptextRect=text_objects("P : PAUSE  ",smalltext)
        ptextRect.center=((150),(350))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((350),(300))
        gamedisplays.blit(sTextSurf,sTextRect)
        gamedisplays.blit(stextSurf,stextRect)
        gamedisplays.blit(hTextSurf,hTextRect)
        gamedisplays.blit(atextSurf,atextRect)
        gamedisplays.blit(rtextSurf,rtextRect)
        gamedisplays.blit(ptextSurf,ptextRect)
        button("BACK",400,400,150,50,forest_green,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)

def paused():
    global pause

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.blit(instruction_background,(0,0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("PAUSED",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            button("CONTINUE",110,450,150,50,green,bright_green,"unpause")
            button("RESTART",300,450,150,50,forest_green,bright_blue,"play")
            pygame.display.update()
            clock.tick(30)

def unpaused():
    global pause
    pause=False


def countdown_background():
    font=pygame.font.SysFont(None,25)
    x=(display_width*0.45)
    y=(display_height*0.8)
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(490,0))
    gamedisplays.blit(backgroundpic,(490,200))
    gamedisplays.blit(backgroundpic,(490,400))
    gamedisplays.blit(black_strip,(295,100))
    gamedisplays.blit(black_strip,(295,200))
    gamedisplays.blit(black_strip,(295,300))
    gamedisplays.blit(black_strip,(295,400))
    gamedisplays.blit(black_strip,(295,100))
    gamedisplays.blit(black_strip,(295,500))
    gamedisplays.blit(black_strip,(295,0))
    gamedisplays.blit(black_strip,(295,600))
    gamedisplays.blit(white_strip,(120,200))
    gamedisplays.blit(white_strip,(120,0))
    gamedisplays.blit(white_strip,(120,100))
    gamedisplays.blit(white_strip,(470,100))
    gamedisplays.blit(white_strip,(470,0))
    gamedisplays.blit(white_strip,(470,200))
    gamedisplays.blit(white_strip,(x,y))
    text=font.render("DODGED: 0",True, black)
    score=font.render("SCORE: 0",True,dark_green)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))
    button("PAUSE",650,0,150,50,forest_green,bright_blue,"pause")

def countdown():
    countdown=True

    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.fill(white)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("3",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(white)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("2",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(white)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("1",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(white)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("GO!!!",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()

def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load("human.jpg")
    elif obs==1:
        obs_pic=pygame.image.load("zombie2.jpg")
    elif obs==2:
        obs_pic=pygame.image.load("zombie3.jpg")
    elif obs==3:
        obs_pic=pygame.image.load("zombie4.jpg")
    elif obs==4:
        obs_pic=pygame.image.load("zombie5.jpg")
    elif obs==5:
        obs_pic=pygame.image.load("zombie6.jpg")
    elif obs==6:
        obs_pic=pygame.image.load("zombie7.jpg")
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))

def score_system(passed,score):
    font=pygame.font.SysFont(None,25)
    text=font.render("Passed"+str(passed),True,black)
    score=font.render("Score"+str(score),True,dark_green)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))


def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    message_display("YOU DIED")


def background():
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(490,0))
    gamedisplays.blit(backgroundpic,(490,200))
    gamedisplays.blit(backgroundpic,(490,400))
    gamedisplays.blit(black_strip,(295,0))
    gamedisplays.blit(black_strip,(295,100))
    gamedisplays.blit(black_strip,(295,200))
    gamedisplays.blit(black_strip,(295,300))
    gamedisplays.blit(black_strip,(295,400))
    gamedisplays.blit(black_strip,(295,500))
    gamedisplays.blit(white_strip,(120,0))
    gamedisplays.blit(white_strip,(120,100))
    gamedisplays.blit(white_strip,(120,200))
    gamedisplays.blit(white_strip,(470,0))
    gamedisplays.blit(white_strip,(470,100))
    gamedisplays.blit(white_strip,(470,200))

def car(x,y):
    gamedisplays.blit(human,(x,y))

def game_loop():
    global pause
    x=(display_width*0.45)
    y=(display_height*0.8)
    x_change=0
    obstacle_speed=9
    obs=0
    y_change=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-750
    obs_width=56
    obs_height=125
    passed=0
    level=0
    score=0
    y2=7
    fps=120

    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_a:
                    obstacle_speed+=2
                if event.key==pygame.K_b:
                    obstacle_speed-=2
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0

        x+=x_change
        pause=True
        gamedisplays.fill(white)

        rel_y=y2%backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic,(0,rel_y-backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic,(490,rel_y-backgroundpic.get_rect().width))
        if rel_y<590:
            gamedisplays.blit(backgroundpic,(0,rel_y))
            gamedisplays.blit(backgroundpic,(490,rel_y))
            gamedisplays.blit(black_strip,(295,rel_y))
            gamedisplays.blit(black_strip,(295,rel_y+100))
            gamedisplays.blit(black_strip,(295,rel_y+200))
            gamedisplays.blit(black_strip,(295,rel_y+300))
            gamedisplays.blit(black_strip,(295,rel_y+400))
            gamedisplays.blit(black_strip,(295,rel_y+500))
            gamedisplays.blit(black_strip,(295,rel_y-100))
            gamedisplays.blit(white_strip,(120,rel_y-200))
            gamedisplays.blit(white_strip,(120,rel_y+20))
            gamedisplays.blit(white_strip,(120,rel_y+30))
            gamedisplays.blit(white_strip,(470,rel_y-100))
            gamedisplays.blit(white_strip,(470,rel_y+20))
            gamedisplays.blit(white_strip,(470,rel_y+30))

        y2+=obstacle_speed




        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x,y)
        score_system(passed,score)
        if x>480-zombie_width or x<110:
            crash()
        if x>display_width-(zombie_width+110) or x<110:
            crash()
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,7)
            passed=passed+1
            score=passed*10
            if int(passed)%10==0:
                level=level+1
                obstacle_speed+2
                largetext=pygame.font.Font("freesansbold.ttf",80)
                textsurf,textrect=text_objects("LEVEL"+str(level),largetext)
                textrect.center=((display_width/2),(display_height/2))
                gamedisplays.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(3)


        if y<obs_starty+obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x+zombie_width > obs_startx and x+zombie_width < obs_startx+obs_width:
                crash()
        button("Pause",450,0,150,50,forest_green,bright_blue,"pause")
        pygame.display.update()
        clock.tick(60)
intro_loop()
game_loop()
pygame.quit()
quit()