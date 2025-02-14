
                                                    ##############################
                                                    # RGX 4.0 Main Engine Script #
                                                    # Written by Python          #
                                                    # Engine Ver : v1.12b        #
                                                    # Version date : 2019.10.09  #
                                                    # Made by kevin5871(sfcatz)  #
                                                    ############################## 





                                                    ## Code Starts From Here ##

# import part
import pygame
from pygame.locals import *
from tkinter import *
from tkinter import messagebox
import platform
import os
import threading
import multiprocessing 
import random
# CONST variable
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
pad_width = 1280
pad_height = 720
fps = 1000
'''
def note1_image() :
    global note1list
    while True :
        for x in note1list :
            appear_image('img/noteimage.png', gamepad, None, 215, x, 255, 2)
def note2_image() :
    global note2list
    while True :
        for x in note2list :
            appear_image('img/noteimage.png', gamepad, None, 430, x, 255, 2)
def note3_image() :
    global note3list
    while True :
        for x in note3list :
            appear_image('img/noteimage.png', gamepad, None, 640, x, 255, 2)
def note4_image() :
    global note4list
    while True :
        for x in note4list :
            appear_image('img/noteimage.png', gamepad, None, 855, x, 255, 2)
'''







def note1_image() :
    global note1list
    for x in note1list :
        appear_image('img/noteimage_normal.png', gamepad, None, 215, x, 255, 2)
        '''
        if 250 <= note1list[x] and note1list[x] <= 350 :
            appear_image('img/noteimage_miss2.png', gamepad, None, 215, note1list[x], 255, 2)
        elif 350 <= note1list[x] and note1list[x] <= 450 :
            appear_image('img/noteimage_good2.png', gamepad, None, 215, note1list[x], 255, 2)
        elif 450 <= note1list[x] and note1list[x] <= 550 :
            appear_image('img/noteimage_great2.png', gamepad, None, 215, note1list[x], 255, 2)
        elif 550 <= note1list[x] and note1list[x] <= 625 :
            appear_image('img/noteimage_perfect2.png', gamepad, None, 215, note1list[x], 255, 2)
        else :
            appear_image('img/noteimage_normal.png', gamepad, None, 215, note1list[x], 255, 2)
        '''
def note2_image() :
    global note2list
    for x in note2list :
        appear_image('img/noteimage_normal.png', gamepad, None, 430, x, 255, 2)
def note3_image() :
    global note3list
    for x in note3list :
        appear_image('img/noteimage_normal.png', gamepad, None, 640, x, 255, 2)
def note4_image() :
    global note4list
    for x in note4list :
        appear_image('img/noteimage_normal.png', gamepad, None, 855, x, 255, 2)

# Game
def noteimagemanage() :
    global note1list, note2list, note3list, note4list
    if(len(note1list) > 0) :
        note1_image()
    if(len(note2list) > 0) :
        note2_image()
    if(len(note3list) > 0) :
        note3_image()
    if(len(note4list) > 0) :
        note4_image()
'''
def noteimagemanage() :
    global note1list, note2list, note3list, note4list, trigger2
    if(trigger2 == 0) :
        t1.terminate()
        t2.terminate()
        t3.terminate()
        t4.terminate()
    t1 = threading.Thread(target=note1_image)
    t2 = threading.Thread(target=note2_image)
    t3 = threading.Thread(target=note3_image)
    t4 = threading.Thread(target=note4_image)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    trigger2 = 0
    pygame.time.delay(int(1000/fps))
    pygame.display.flip()
'''

def note1_control() :
    global note1list, speed, combo, max_combo, grade
    #note1list.append(0)
    if(len(note1list) > 0) :
        for x in range(0,len(note1list)) :
            note1list[x] += speed
        if(note1list[0] > 720) :
             del note1list[0]
             grade[0] += 1
             if(max_combo < combo) :
                 max_combo = combo
             combo = 0
        #del note1list[len(note1list) - 1]
def note2_control() :
    global note2list, speed, combo, max_combo, grade
    #note2list.append(0)
    if(len(note2list) > 0) :
        for x in range(0,len(note2list))  :
            note2list[x] += speed
        if(note2list[0] > 720) :
           del note2list[0]
           grade[0] += 1
           if(max_combo < combo) :
               max_combo = combo
           combo = 0
        #del note2list[len(note2list) - 1]
def note3_control() :
    global note3list, speed, combo, max_combo, grade
    #note3list.append(0)
    if(len(note3list) > 0) :
        for x in range(0,len(note3list))  :
            note3list[x] += speed
        if(note3list[0] > 720) :
            del note3list[0]
            grade[0] += 1
            if(max_combo < combo) :
                max_combo = combo
            combo = 0
                #break
        #del note3list[len(note3list) - 1]
def note4_control() :
    global note4list, speed, combo, max_combo, grade
    #note4list.append(0)
    if(len(note4list) > 0) :
        for x in range(0,len(note4list))  :
            note4list[x] += speed
        if(note4list[0] > 720) :
             del note4list[0]
             grade[0] += 1
             if(max_combo < combo) :
                 max_combo = combo
             combo = 0
                #break
        #del note4list[len(note4list) - 1]

def notelistmanage() :
    global note1list, note2list, note3list, note4list
    if(len(note1list) > 0) :
        note1_control()
    if(len(note2list) > 0) :
        note2_control()
    if(len(note3list) > 0) :
        note3_control()
    if(len(note4list) > 0) :
        note4_control()

'''
def notelistdelete() :
    global note1list, note2list, note3list, note4list
    for x in range(0, len(note1list)) :
        if(note1list[x] < 720):
            print(x)
            del note1list[0:x]
            break
    for x in range(0, len(note2list)) :
        if(note2list[x] < 720):
            print(x)
            del note2list[0:x]
            break
    for x in range(0, len(note3list)) :
        if(note3list[x] < 720):
            print(x)
            del note3list[0:x]
            break
    for x in range(0, len(note4list)) :
        if(note4list[x] < 720):
            print(x)
            del note4list[0:x]
            break
'''
def scoreprint() :
    global score, combo, max_combo, max_score, percent
    percent = float(score / max_score * 100)
    text('SCORE','ttf/Bittypix-Countdown.ttf', 35, WHITE, 1200, 50)
    text("%05d"% score,'ttf/Bittypix-Countdown.ttf', 35, WHITE, 1200, 100)
    text('MAX_COMBO','ttf/Bittypix-Countdown.ttf', 20, WHITE, 1200, 150)
    text("%04d"% max_combo,'ttf/Bittypix-Countdown.ttf', 20, WHITE, 1230, 180)
    text('COMBO','ttf/Bittypix-Countdown.ttf', 20, WHITE, 1225, 220)
    text("%04d"% combo,'ttf/Bittypix-Countdown.ttf', 20, WHITE, 1230, 250)
    text("%.02f%%"% percent, 'ttf/Enchanted-Land.ttf', 45, WHITE, 1225, 650)

'''
if 250 <= note1list[x] and note1list[x] <= 350 :
            appear_image('img/noteimage_miss2.png', gamepad, None, 215, note1list[x], 255, 2)
        elif 350 <= note1list[x] and note1list[x] <= 450 :
            appear_image('img/noteimage_good2.png', gamepad, None, 215, note1list[x], 255, 2)
        elif 450 <= note1list[x] and note1list[x] <= 550 :
            appear_image('img/noteimage_great2.png', gamepad, None, 215, note1list[x], 255, 2)
        elif 550 <= note1list[x] and note1list[x] <= 625 :
            appear_image('img/noteimage_perfect2.png', gamepad, None, 215, note1list[x], 255, 2)
        else :
            appear_image('img/noteimage_normal.png', gamepad, None, 215, note1list[x], 255, 2)
'''
def note1clicked() :
    global note1list, max_combo, combo, grade, score
    for x in range(0, len(note1list)) :
        if(note1list[x] < 720):
            print(x)
            if not note1list[x] < 250 :
                if 250 <= note1list[x] and note1list[x] <= 350 :
                    grade[0] += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_miss2.png', gamepad, None, 215, note1list[x], 255, 1)
                elif 350 <= note1list[x] and note1list[x] <= 425 :
                    grade[1] += 1
                    score += 4
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_good2.png', gamepad, None, 215, note1list[x], 255, 1)
                elif 425 <= note1list[x] and note1list[x] <= 500 :
                    grade[2] += 1
                    score += 7
                    combo += 1
                    appear_image('img/noteimage_great2.png', gamepad, None, 215, note1list[x], 255, 1)
                elif 500 <= note1list[x] and note1list[x] <= 625 :
                    grade[3] += 1
                    score += 10
                    combo += 1
                    appear_image('img/noteimage_perfect2.png', gamepad, None, 215, note1list[x], 255, 1)
                else :
                    grade[0] += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_miss22.png', gamepad, None, 215, note1list[x], 255, 1)
            del note1list[0:x]
            break
    del note1list[0]
def note2clicked() :
    global note2list, max_combo, combo, grade, score
    for x in range(0, len(note2list)) :
        if(note2list[x] < 720):
            print(x)
            if not note2list[x] < 250 :
                if 250 <= note2list[x] and note2list[x] <= 350 :
                    grade[0] += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_miss2.png', gamepad, None, 430, note2list[x], 255, 1)
                elif 350 <= note2list[x] and note2list[x] <= 425 :
                    grade[1] += 1
                    score += 4
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_good2.png', gamepad, None, 430, note2list[x], 255, 1)
                elif 425 <= note2list[x] and note2list[x] <= 500 :
                    grade[2] += 1
                    score += 7
                    combo += 1
                    appear_image('img/noteimage_great2.png', gamepad, None, 430, note2list[x], 255, 1)
                elif 500 <= note2list[x] and note2list[x] <= 625 :
                    grade[3] += 1
                    score += 10
                    combo += 1
                    appear_image('img/noteimage_perfect2.png', gamepad, None, 430, note2list[x], 255, 1)
                else :
                    grade[0] += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    appear_image('img/noteimage_miss2.png', gamepad, None, 430, note2list[x], 255, 1)
                    combo = 0
            del note2list[0:x]
            break
    del note2list[0]
def note3clicked() :
    global note3list, max_combo, combo, grade, score
    for x in range(0, len(note3list)) :
        if(note3list[x] < 720):
            print(x)
            if not note3list[x] < 250 :
                if 250 <= note3list[x] and note3list[x] <= 350 :
                    grade[0] += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_miss2.png', gamepad, None, 640, note3list[x], 255, 1)
                elif 350 <= note3list[x] and note3list[x] <= 425 :
                    grade[1] += 1
                    score += 4
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_good2.png', gamepad, None, 640, note3list[x], 255, 1)
                elif 425 <= note3list[x] and note3list[x] <= 500 :
                    grade[2] += 1
                    score += 7
                    combo += 1
                    appear_image('img/noteimage_great2.png', gamepad, None, 640, note3list[x], 255, 1)
                elif 500 <= note3list[x] and note3list[x] <= 625 :
                    grade[3] += 1
                    score += 10 
                    combo += 1
                    appear_image('img/noteimage_perfect2.png', gamepad, None, 640, note3list[x], 255, 1)
                else :
                    grade[0] += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_miss2.png', gamepad, None, 640, note3list[x], 255, 1)
            del note3list[0:x]
            break
    del note3list[0]
def note4clicked() :
    global note4list, max_combo, combo, grade, score
    for x in range(0, len(note4list)) :
        if(note4list[x] < 720):
            print(x)
            if not note4list[x] < 250 :
                if 250 <= note4list[x] and note4list[x] <= 350 :
                    grade[0] += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_miss2.png', gamepad, None, 855, note4list[x], 255, 1)
                elif 350 <= note4list[x] and note4list[x] <= 425 :
                    grade[1] += 1
                    score += 4
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_good2.png', gamepad, None, 855, note4list[x], 255, 1)
                elif 425 <= note4list[x] and note4list[x] <= 500 :
                    grade[2] += 1
                    score += 7
                    combo += 1
                    appear_image('img/noteimage_great2.png', gamepad, None, 855, note4list[x], 255, 1)
                elif 500 <= note4list[x] and note4list[x] <= 625 :
                    grade[3] += 1
                    score += 10
                    combo += 1
                    appear_image('img/noteimage_perfect2.png', gamepad, None, 855, note4list[x], 255, 1)
                else :
                    grade[0] += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_miss2.png', gamepad, None, 855, note4list[x], 255, 1)
            del note4list[0:x]
            break
    del note4list[0]

def set() :
    notelistmanage()
    gamebackground1()
    noteimagemanage()
    scoreprint()


def startengine() :
    global timer, keylist, timelist, crashed, background, note1list, note2list, note3list, note4list, speed, trigger, trigger2, score, grade, combo, max_combo, max_score
    note1list, note2list, note3list, note4list = list(), list(), list(), list()
    grade = [0,0,0,0]
    combo = 0
    max_combo = 0
    cursor = 0
    start_time = pygame.time.get_ticks()
    speed = 50
    trigger2 = 1
    loop = 0
    gameend = 0
    score = 0
    max_score = 10 * len(keylist)
    while not crashed :
        #while (pygame.mixer.music.get_busy() or trigger == 0) and (cursor < len(keylist)-1 or cursor == len(keylist)-1 or gameend == 0):
        while (pygame.mixer.music.get_busy() or loop < 50) or (len(note1list)+len(note2list)+len(note3list)+len(note4list) > 0):
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    t1.terminate()
                    crashed = True
                    return
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_d :
                        t = threading.Thread(target=note1clicked)
                        t.start()
                    elif event.key == pygame.K_f :
                        t = threading.Thread(target=note2clicked)
                        t.start()
                    elif event.key == pygame.K_j :
                        t = threading.Thread(target=note3clicked)
                        t.start()
                    elif event.key == pygame.K_k :
                        t = threading.Thread(target=note4clicked)
                        t.start()
                    else :
                        pass
            loop += 1
            #score += 1
            #if(loop % 25 == 0) :
                #notelistdelete()
            timer = (pygame.time.get_ticks() - start_time) / 1000
            '''
            t1 = threading.Thread(target=notelistmanage)
            t2 = threading.Thread(target=gamebackground1)
            t3 = threading.Thread(target=noteimagemanage)
            t4 = threading.Thread(target=scoreprint)
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            '''
            '''
            notelistmanage()
            gamebackground1()
            noteimagemanage()
            scoreprint()
            '''
            t1 = threading.Thread(target=set)
            t1.start()
            note = keylist[cursor]
            if(platform.system() == 'Windows') :
                os.system('cls')
            else :
                os.system('clear')
            print("Cursor : " + str(cursor))
            print("Note : " + str(note))
            print(note1list)
            print(note2list)    
            print(note3list)
            print(note4list)
            print(grade)
            print("loop : "+str(loop))
            print("combo : "+str(combo))
            print("max_combo : "+str(max_combo))
            print("score : "+str(score))
            print(str(pygame.mixer.music.get_busy()))
            t1.join()
            pygame.time.delay(int(1000/fps))
            pygame.display.flip()
            try :
                if(timer == float(timelist[cursor]) or timer >= float(timelist[cursor])) :
                    if(note == '1') :
                        if not cursor+1 == len(keylist) :
                            note1list.append(0)
                    elif(note == '2') :
                        if not cursor+1 == len(keylist) :
                            note2list.append(0)
                    elif(note == '3') :
                        if not cursor+1 == len(keylist) :
                            note3list.append(0)
                    elif(note == '4') :
                        if not cursor+1 == len(keylist) :
                            note4list.append(0)
                    elif(note == '') :
                        pass
                    else :
                        error(11, "NoteSet Error!\nPlease Contact Developer : kevin587121@gmail.com")
                    if not cursor+1 == len(keylist) :
                        cursor += 1
                    if(pygame.mixer.music.get_busy() == False) :
                        gameend = 1
            except IndexError : 
                pass
                '''
                pygame.time.delay(int(1000/fps))
                pygame.display.flip()
                '''
        return
               

def readnote(num) :
    global keylist, timelist, musiclist
    keylist = open(os.path.join('Songs', musiclist[musicnum-1], 'keynote.txt'), 'r').read().split('\n')
    timelist = open(os.path.join('Songs', musiclist[musicnum-1], 'timenote.txt'), 'r').read().split('\n')
    
    print(keylist)
    print(timelist)

def error(num, message) : # Error message
    global crashed
    messagebox.showerror('Error!', 'An Error Occured.\nCode : '+ str(num) + '\n' + message)
    crashed = True

def soundstop() : # Sound Stop
    pygame.mixer.music.stop()

def appear_image(image, screen, background_color,x,y,alphaset, switch):  # Appear Image (image / convert(), transparency)
    image = pygame.image.load(image).convert()
    if switch == 0 :
        image.set_colorkey(WHITE)
        alpha = 0
        while alpha < alphaset :          
            alpha += 5
            image.set_alpha(alpha)
            pygame.display.update(screen.blit(image, (x,y))) 
            pygame.time.delay(5) 
        return
    elif switch == 1 :
        alpha = alphaset
        image.set_alpha(alpha)
        pygame.display.update(screen.blit(image, (x,y))) 
        pygame.time.delay(5) 
    elif switch == 2 :
        alpha = alphaset
        image.set_alpha(alpha)
        screen.blit(image, (x,y))
    else :
        error(7, 'ImageSwitchError!\nContact Developer : kevin587121@gmail.com')
        return 0

def back(): # Draw Background (background variable)
    global gamepad, background
    gamepad.blit(background,(0,0))
    pygame.display.update()


def soundplay(string, mode): # Play Sound (Repeat)
    if (not pygame.mixer.music.get_busy()) :
        soundObj = pygame.mixer.music.load(string)
        pygame.mixer.music.play(mode)

def selectsound(num): # Select Sound play
    global musiclist
    soundplay(os.path.join('Songs', musiclist[num-1], 'select.mp3'), -1)
def text(string, font, size, color, x, y) : # Text (font, size, color, x, y changable)
        font = pygame.font.Font(font, size)
        TextSurf, TextRect = text_objects(string, font, color)
        TextRect.center = (x, y)
        pygame.display.update(gamepad.blit(TextSurf, TextRect))

def selecttext(songname, producer, level, levelstat) : # Song Info text (Main Frame)
        text("Song Name : " + songname,'ttf/KaiGenGothicKR-Regular.ttf', 32, WHITE, 625, 550)
        text("Producer : " + producer,'ttf/KaiGenGothicKR-Regular.ttf', 32, WHITE, 625, 590)
        text("Level : " + str(level),'ttf/KaiGenGothicKR-Regular.ttf', 32, WHITE, 625, 630)
        if(levelstat == "easy") :
            text("(EASY)",'ttf/KaiGenGothicKR-Regular.ttf', 24, (135,206,235), 735, 632)
        elif(levelstat == "normal") :
            text("(NORMAL)",'ttf/KaiGenGothicKR-Regular.ttf', 24, GREEN, 750, 632)
        elif(levelstat == "hard") :
            text("(HARD)",'ttf/KaiGenGothicKR-Regular.ttf', 24, (255,140,0), 735, 632)
        elif(levelstat == "insane") :
            text("(INSANE)",'ttf/KaiGenGothicKR-Regular.ttf', 24, RED, 735, 632)
        elif(levelstat == "crazy") :
            text("(EASY)",'ttf/KaiGenGothicKR-Regular.ttf', 24, (148,0,211), 735, 632)
        else :
            text("(UNVALUED)",'ttf/KaiGenGothicKR-Regular.ttf', 24, (192,192,192), 765, 632)

def selectimg(num): #Song Info Image / Arrows
    global musiclist
    appear_image(os.path.join('Songs', musiclist[num - 1], 'select.png'), gamepad, None, 300, 100, 255, 1)
    infotext = open(os.path.join('Songs', musiclist[musicnum-1], 'info.txt'), 'r').read().split('\n')
    selecttext(str(infotext[0]), str(infotext[1]), int(infotext[2]), str(infotext[3]))
    # Arrows
    imageload = pygame.image.load('img/rightarrow.png').convert_alpha()
    a,b,x,y = imageload.get_rect()
    imageload = pygame.transform.scale(imageload, (x*2, y*2))
    pygame.display.update(gamepad.blit(imageload, (1075, 200)))
    imageload2 = pygame.image.load('img/leftarrow.png').convert_alpha()
    a,b,x,y = imageload2.get_rect()
    imageload2 = pygame.transform.scale(imageload2, (x*2, y*2))
    pygame.display.update(gamepad.blit(imageload2, (75, 200)))

def gamebackground1() :
    global musicnum, musiclist
    gamepad.fill(BLACK)

    if(os.path.exists(os.path.join('Songs', musiclist[musicnum-1], 'background.jpg'))) :
        background = pygame.image.load(os.path.join('Songs', musiclist[musicnum-1], 'background.jpg'))
    elif (os.path.exists(os.path.join('Songs', musiclist[musicnum-1], 'background.png'))) :
        background = pygame.image.load(os.path.join('Songs', musiclist[musicnum-1], 'background.png'))
    else :
        error(9, 'BackgroundImageError!\nPlease Contact Developer : kevin587121@gmail.com')
    gamepad.blit(background,(0,0))
    appear_image('img/notepagenew2.png', gamepad, None, 0, 0, 150, 2)

def gamebackground2() :
    global musicnum, musiclist
    gamepad.fill(BLACK)

    if(os.path.exists(os.path.join('Songs', musiclist[musicnum-1], 'background.jpg'))) :
        background = pygame.image.load(os.path.join('Songs', musiclist[musicnum-1], 'background.jpg'))
    elif (os.path.exists(os.path.join('Songs', musiclist[musicnum-1], 'background.png'))) :
        background = pygame.image.load(os.path.join('Songs', musiclist[musicnum-1], 'background.png'))
    else :
        error(9, 'BackgroundImageError!\nPlease Contact Developer : kevin587121@gmail.com')
    gamepad.blit(background,(0,0))
    appear_image('img/notepagenew2.png', gamepad, None, 0, 0, 150, 2)


def runGame(): # Main Script
    global gamepad, clock, scenenum, background, lastscene, musicnum, imgnum, crashed, keylist, timelist, trigger, musiclist, grade, percent, maxmax_combo
    crashed = False
    #scenenum = 8
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # X Button
                crashed = True
            elif event.type == pygame.KEYDOWN : # Key Pressed
                if event.key == pygame.K_RETURN : # Enter
                    if scenenum == 1 :
                        lastscene = 1
                        scenenum = 2
                    elif scenenum == 4 :
                        lastscene = 5
                        scenenum = 2
                    else :
                        pass
                elif event.key == pygame.K_RIGHT : # Right Key
                    if scenenum == 4 :
                        if(musicnum == MUSIC_MAXNUM) :
                            musicnum = 1
                        elif(musicnum > MUSIC_MAXNUM) :
                            error(5, 'SelectCursorOverflowed!\nPlease Contact Developer : kevin5871@gmail.com')
                            crashed == True
                        else :
                            musicnum += 1
                        lastscene = 1
                        scenenum = 2
                elif event.key == pygame.K_LEFT : # Left Key
                    if scenenum == 4 :
                        if(musicnum == 1) :
                            musicnum = MUSIC_MAXNUM
                        elif(musicnum < 1) :
                            error(5, 'SelectCursorOverflowed!\nPlease Contact Developer : kevin5871@gmail.com')
                            crashed == True
                        else :
                            musicnum -= 1
                        lastscene = 1
                        scenenum = 2
                elif event.key == pygame.K_SPACE : #Space
                    if scenenum == 10 :
                        pygame.time.delay(1000)
                        lastscene = 1
                        scenenum = 2
            elif event.type == pygame.MOUSEBUTTONDOWN : # Mouse Clicked
                if event.button == 1 : # Left Button Clicked
                    if scenenum == 4 :
                        x,y = pygame.mouse.get_pos()
                        if 0 < x and x < 150 :
                            if(musicnum == 1) :
                                musicnum = MUSIC_MAXNUM
                            elif(musicnum < 1) :
                                error(5, 'SelectCursorOverflowed!\nPlease Contact Developer : kevin5871@gmail.com')
                                crashed == True
                            else :
                                musicnum -= 1
                            lastscene = 1
                            scenenum = 2
                        elif 1115 < x and x < pad_width :
                            if(musicnum == MUSIC_MAXNUM) :
                                musicnum = 1
                            elif(musicnum > MUSIC_MAXNUM) :
                                error(5, 'SelectCursorOverflowed!\nPlease Contact Developer : kevin5871@gmail.com')
                                crashed == True
                            else :
                                musicnum += 1
                            lastscene = 1
                            scenenum = 2
                        elif 299 < x and x < 976 and 107 < y and y < 498 :
                            lastscene = 5
                            scenenum = 2
        if(scenenum == 1) :
            soundplay('music/RGX Intro.mp3', -1)
            if(imgnum == 0) :
                imgnum += 1
                appear_image('img/mainbar.png', gamepad, None, 0, 550, 50, 0)
            else :
                imageload = pygame.image.load('img/mainbar_text.png').convert_alpha()
                imageload.set_alpha(150)
                pygame.display.update(gamepad.blit(imageload, (0, 550)))
        elif(scenenum == 0) :
            error(1, 'ScenenumError! Please Contact Developer : kevin587121@gmail.com')
            crashed = True
        elif(scenenum == 2) :
            soundstop()
            if(lastscene == 0) :
                gamepad.fill(WHITE)
                background = pygame.image.load('img/main.png')
                back()
                scenenum = 1
            elif(lastscene == 1) :
                gamepad.fill(WHITE)
                background = pygame.image.load('img/selectmain.jpg')
                back()
                scenenum = 3
            elif(lastscene == 3) :
                gamebackground2()
                scenenum = 6
            elif(lastscene == 5) :
                gamepad.fill(BLACK)
                scenenum = 5
            elif(lastscene == 6) :
                gamepad.fill(BLACK)
            else :
                error(3, 'UnexpectedAccesspoint\nPlease Contact Developer : kevin587121@gmail.com')
                crashed = True
        elif(scenenum == 3) :
            if(musicnum == 0) :
                error(2, 'UnexpectedAccesspoin.\nPlease Contact Developer : kevin587121@gmail.com')
            else :
                selectsound(musicnum)
                selectimg(musicnum)
                scenenum = 4
        elif(scenenum == 4) :
            readycountdown = 4
        elif(scenenum == 5) :
            if readycountdown == 4 :
                for x in range(0,10,1) :
                    text('SELECTED!!!', 'ttf/Rosbed.ttf', 100, BLUE, 675, 250)
                    text('Please Wait...', 'ttf/Rosbed.ttf', 100, WHITE, 675, 360)
                    pygame.time.wait(50)
                    text('SELECTED!!!', 'ttf/Rosbed.ttf', 100, (255,255,0), 675, 250)
                    text('Please Wait...', 'ttf/Rosbed.ttf', 100, WHITE, 675, 360)
                    pygame.time.wait(50)
                readycountdown -= 1
            elif not readycountdown < 1 :
                appear_image('img/blackscreen.png', gamepad, None, 0, 0, 255, 1)
                text(str(readycountdown), 'ttf/Klavika-Regular.ttf', 150, WHITE, 650, 325)
                readycountdown -= 1
                lastnum = 5
                scenenum = 2
                pygame.time.wait(1000)
                continue
            elif readycountdown == 0 :
                text('GO!!!', 'ttf/Klavika-Regular.ttf', 150, WHITE, 650, 325)
                pygame.time.wait(1500)
                readycountdown -= 1
            else :
                lastscene = 3
                scenenum = 2
        elif(scenenum == 6) :
            pygame.display.flip()
            readnote(musicnum)
            trigger = 0
            t = threading.Thread(target=music)
            t.start()
            startengine()
            trigger = 1
            scenenum = 7
        elif(scenenum == 7) :
            t.join()
            #pass
            if(platform.system() == 'Windows') :
                os.system('cls')
            else :
                os.system('clear')
            print("Engine Successfully Ended")
            scenenum = 8
        elif(scenenum == 8) :
            pygame.time.delay(2000)
            gamepad.fill(WHITE)
            imsi = random.randrange(1,5)
            #imsi = 4
            if(imsi == 1):
                appear_image('img/resultpage1.png',gamepad,None,0,0,255,0)
                s = pygame.Surface((300,350))  
                s.set_alpha(128)                
                s.fill((0,0,0))           
                pygame.display.update(gamepad.blit(s, (900,325)))
            elif(imsi == 2):
                appear_image('img/resultpage2.jpg',gamepad,None,0,0,255,0)
                s = pygame.Surface((300,350))  
                s.set_alpha(128)                
                s.fill((0,0,0))           
                pygame.display.update(gamepad.blit(s, (275,50)))
            elif(imsi == 3) :
                appear_image('img/resultpage3.jpg',gamepad,None,0,0,255,0)
                s = pygame.Surface((300,350))  
                s.set_alpha(128)                
                s.fill((0,0,0))           
                pygame.display.update(gamepad.blit(s, (700,50)))
            else :
                appear_image('img/resultpage4.png',gamepad,None,0,0,255,0)
                s = pygame.Surface((300,350))  
                s.set_alpha(128)                
                s.fill((0,0,0))           
                pygame.display.update(gamepad.blit(s, (950,50)))
            scenenum = 9
        elif(scenenum == 9) :
            #grade = [123,456,789,101]
            #score = 99999
            #max_combo = 9999
            #percent = 90.0
            if(imsi == 1):
                text('result', 'ttf/AmazOOSTROVv.2.ttf',60,WHITE,1050,375)
                text('PERFECT', 'ttf/Long_Shot.ttf', 40, (204,51,255),1000,450)
                text(str(grade[3]), 'ttf/Long_Shot.ttf', 40, WHITE, 1125,450)
                text('GREAT', 'ttf/Long_Shot.ttf', 40, (0,102,255),1000,495)
                text(str(grade[2]), 'ttf/Long_Shot.ttf', 40, WHITE, 1125,495)
                text('GOOD', 'ttf/Long_Shot.ttf', 40, GREEN,1000,535)
                text(str(grade[1]), 'ttf/Long_Shot.ttf', 40, WHITE, 1125,535)
                text('MISS', 'ttf/Long_Shot.ttf', 40, RED,1000,575)
                text(str(grade[0]), 'ttf/Long_Shot.ttf', 40, WHITE, 1125,575)
                text('MAX COMBO', 'ttf/Long_Shot.ttf', 20, WHITE,950,615)
                text(str(max_combo), 'ttf/Long_Shot.ttf', 35, WHITE, 950,645)
                text('SCORE', 'ttf/Long_Shot.ttf', 20, WHITE,1050,615)
                text(str(score), 'ttf/Long_Shot.ttf', 35, WHITE, 1050,645)
                text('GRADE', 'ttf/Long_Shot.ttf', 20, WHITE,1150,615)
                if(90.0 <= percent) :
                    text('A', 'ttf/Long_Shot.ttf', 40, (255,255,0), 1150,645)
                elif(80.0 <= percent and percent < 90.0) :
                    text('B', 'ttf/Long_Shot.ttf',40, GREEN, 1150,645)
                elif(70.0 <= percent and percent < 80.0) :
                    text('C', 'ttf/Long_Shot.ttf', 40, (255,153,0), 1150,645)
                elif(60.0 <= percent and percent < 70.0) :
                    text('D', 'ttf/Long_Shot.ttf', 40, (153,102,21), 1150,645)
                else :
                    text('F', 'ttf/Long_Shot.ttf', 40, RED, 1125,645)
            elif(imsi == 2) :
                text('result', 'ttf/AmazOOSTROVv.2.ttf',60,WHITE,425,100)
                text('PERFECT', 'ttf/Long_Shot.ttf', 40, (204,51,255),375,175)
                text(str(grade[3]), 'ttf/Long_Shot.ttf', 40, WHITE, 500,175)
                text('GREAT', 'ttf/Long_Shot.ttf', 40, (0,102,255),375,215)
                text(str(grade[2]), 'ttf/Long_Shot.ttf', 40, WHITE, 500,215)
                text('GOOD', 'ttf/Long_Shot.ttf', 40, GREEN,375,255)
                text(str(grade[1]), 'ttf/Long_Shot.ttf', 40, WHITE, 500,255)
                text('MISS', 'ttf/Long_Shot.ttf', 40, RED,375,295)
                text(str(grade[0]), 'ttf/Long_Shot.ttf', 40, WHITE, 500,295)
                text('MAX COMBO', 'ttf/Long_Shot.ttf', 20, WHITE,325,335)
                text(str(max_combo), 'ttf/Long_Shot.ttf', 35, WHITE, 325,365)
                text('SCORE', 'ttf/Long_Shot.ttf', 20, WHITE,425,335)
                text(str(score), 'ttf/Long_Shot.ttf', 35, WHITE, 425,365)
                text('GRADE', 'ttf/Long_Shot.ttf', 20, WHITE,525,335)
                if(90.0 <= percent) :
                    text('A', 'ttf/Long_Shot.ttf', 40, (255,255,0), 525,365)
                elif(80.0 <= percent and percent < 90.0) :
                    text('B', 'ttf/Long_Shot.ttf',40, GREEN, 525,365)
                elif(70.0 <= percent and percent < 80.0) :
                    text('C', 'ttf/Long_Shot.ttf', 40, (255,153,0), 525,365)
                elif(60.0 <= percent and percent < 70.0) :
                    text('D', 'ttf/Long_Shot.ttf', 40, (153,102,21), 525,365)
                else :
                    text('F', 'ttf/Long_Shot.ttf', 40, RED, 525,365)
            elif(imsi == 3) :
                #text('result', 'ttf/AmazOOSTROVv.2.ttf',60,(235,150,165),850,100)
                text('result', 'ttf/AmazOOSTROVv.2.ttf',60,WHITE,850,100)
                text('PERFECT', 'ttf/Long_Shot.ttf', 40, (204,51,255),800,175)
                text(str(grade[3]), 'ttf/Long_Shot.ttf', 40, WHITE, 925,175)
                text('GREAT', 'ttf/Long_Shot.ttf', 40, BLUE,800,215)
                text(str(grade[2]), 'ttf/Long_Shot.ttf', 40, WHITE, 925,215)
                text('GOOD', 'ttf/Long_Shot.ttf', 40, GREEN,800,255)
                text(str(grade[1]), 'ttf/Long_Shot.ttf', 40, WHITE, 925,255)
                text('MISS', 'ttf/Long_Shot.ttf', 40, RED,800,295)
                text(str(grade[0]), 'ttf/Long_Shot.ttf', 40, WHITE, 925,295)
                text('MAX COMBO', 'ttf/Long_Shot.ttf', 20, WHITE,750,335)
                text(str(max_combo), 'ttf/Long_Shot.ttf', 35, WHITE, 750,365)
                text('SCORE', 'ttf/Long_Shot.ttf', 20, WHITE,850,335)
                text(str(score), 'ttf/Long_Shot.ttf', 35, WHITE, 850,365)
                text('GRADE', 'ttf/Long_Shot.ttf', 20, WHITE,950,335)
                if(90.0 <= percent) :
                    text('A', 'ttf/Long_Shot.ttf', 40, (255,255,0), 950,365)
                elif(80.0 <= percent and percent < 90.0) :
                    text('B', 'ttf/Long_Shot.ttf',40, GREEN, 950,365)
                elif(70.0 <= percent and percent < 80.0) :
                    text('C', 'ttf/Long_Shot.ttf', 40, (255,153,0), 950,365)
                elif(60.0 <= percent and percent < 70.0) :
                    text('D', 'ttf/Long_Shot.ttf', 40, (153,102,21), 950,365)
                else :
                    text('F', 'ttf/Long_Shot.ttf', 40, RED, 950,365)
            else :
                text('result', 'ttf/AmazOOSTROVv.2.ttf',60,WHITE,1100,100)
                text('PERFECT', 'ttf/Long_Shot.ttf', 40, (204,51,255),1050,175)
                text(str(grade[3]), 'ttf/Long_Shot.ttf', 40, WHITE, 1175,175)
                text('GREAT', 'ttf/Long_Shot.ttf', 40, BLUE,1050,215)
                text(str(grade[2]), 'ttf/Long_Shot.ttf', 40, WHITE, 1175,215)
                text('GOOD', 'ttf/Long_Shot.ttf', 40, GREEN,1050,255)
                text(str(grade[1]), 'ttf/Long_Shot.ttf', 40, WHITE, 1175,255)
                text('MISS', 'ttf/Long_Shot.ttf', 40, RED,1050,295)
                text(str(grade[0]), 'ttf/Long_Shot.ttf', 40, WHITE, 1175,295)
                text('MAX COMBO', 'ttf/Long_Shot.ttf', 20, WHITE,1000,335)
                text(str(max_combo), 'ttf/Long_Shot.ttf', 35, WHITE, 1000,365)
                text('SCORE', 'ttf/Long_Shot.ttf', 20, WHITE,1100,335)
                text(str(score), 'ttf/Long_Shot.ttf', 35, WHITE, 1100,365)
                text('GRADE', 'ttf/Long_Shot.ttf', 20, WHITE,1200,335)
                if(90.0 <= percent) :
                    text('A', 'ttf/Long_Shot.ttf', 40, (255,255,0), 1200,365)
                elif(80.0 <= percent and percent < 90.0) :
                    text('B', 'ttf/Long_Shot.ttf',40, GREEN, 1200,365)
                elif(70.0 <= percent and percent < 80.0) :
                    text('C', 'ttf/Long_Shot.ttf', 40, (255,153,0), 1200,365)
                elif(60.0 <= percent and percent < 70.0) :
                    text('D', 'ttf/Long_Shot.ttf', 40, (153,102,21), 1200,365)
                else :
                    text('F', 'ttf/Long_Shot.ttf', 40, RED, 1200,365)
            text('Space Key to Return', 'ttf/KaiGenGothicKR-Regular.ttf', 30, WHITE, 1125, 700)
            scenenum = 10
        elif(scenenum == 10) :
            pass
        else :
            error(0, 'UnexpectedAccesspoint\nPlease Contact Developer : kevin587121@gmail.com')
            crashed = True
        clock.tick(fps)
    pygame.quit()

def music() : 
    global musicnum, musiclist
    imsi = open(os.path.join('Songs', musiclist[musicnum-1], 'info.txt'), 'r').read().split('\n')
    pygame.time.delay(int(imsi[4])) #### MUSIC SYNC ####
    soundplay(os.path.join('Songs', musiclist[musicnum-1], 'song.mp3'), 1)

def initGame(): # Initiation
    global gamepad, clock, background, scenenum, imgnum, lastscene, musicnum, notea_group
    lastscene = 0
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('RGX 4.0')
    imgnum = 0
    clock = pygame.time.Clock()
    Tk().wm_withdraw()
    musicnum = 1

def text_objects(text, font, color): # Text Fragment (Used in GameIntro())
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def Gameintro(): # Game Intro
    global scenenum
    scenenum = 0
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()      
        gamepad.fill(WHITE)
        largeText = pygame.font.Font('ttf/picoblack.ttf',115)
        TextSurf, TextRect = text_objects("Made By kevin5871", largeText, BLACK)
        TextRect.center = ((pad_width/2),(pad_height/2))
        gamepad.blit(TextSurf, TextRect)

        pygame.display.update()
        pygame.time.delay(2000)
        lastscene = 0
        scenenum = 2
        return
def search(dir) :
    global musiclist
    musiclist = list()
    musiclist = os.listdir(dir)
    print(musiclist)
pygame.init()

if __name__ == "__main__" :
    initGame() # Init
    search('Songs')
    MUSIC_MAXNUM = len(musiclist)
    Gameintro() # Intro Page
    runGame() # Game Start