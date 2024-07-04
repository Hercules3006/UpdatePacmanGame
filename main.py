import pygame , sys
from button import Button
import Super_hard 
import Easy
import Hard
import normal  
pygame.init()
click_sound = pygame.mixer.Sound("assets/munch_2.wav")

SCREEN_WIDTH=448
SCREEN_HEIGHT=535

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PACMAN")

BG = pygame.image.load("assets/Background_pacman.png")
BG_width,BG_height = BG.get_size()
scale_x_BG= (SCREEN_WIDTH/BG_width)
scale_y_BG= (SCREEN_HEIGHT/BG_height)*0.75
scaled_image_BG = pygame.transform.scale(BG, (int(BG_width * scale_x_BG), int(BG_height * scale_y_BG)))
bestScore_easy = 0
bestScore_normal = 0
bestScore_hard = 0
bestScore_Super_hard = 0
score_Super_hard = 0
score_Hard = 0
score_normal = 0
score_Easy = 0
pacman_screen_play = pygame.image.load("assets/pacman_screen.jpg")
pacman_screen_play_width,pacman_screen_play_height =pacman_screen_play.get_size()
scale_x_P= (SCREEN_WIDTH/pacman_screen_play_width)*0.68
scale_y_P= (SCREEN_HEIGHT/pacman_screen_play_height)*0.48
scaled_image_pacman = pygame.transform.scale(pacman_screen_play, (int(pacman_screen_play_width * scale_x_P), int(pacman_screen_play_height * scale_y_P)))
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    global bestScore_easy, bestScore_normal, bestScore_hard, bestScore_Super_hard
    global score_Super_hard, score_Hard, score_normal, score_Easy
    while True:
        SCREEN.fill("black")
        SCREEN.blit(scaled_image_pacman,(165,150))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        # #PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        # EASY_MODE=get_font(45).render("EASY_MODE",True,"white")
        # EASY_RECT=EASY_MODE.get_rect(center=(640,100))
        # SCREEN.blit(EASY_MODE,EASY_RECT)
        # V? 4 CH? Ð? GAME 
        #easy 
        EASY_BUTTON = Button(image=None, pos=(215, 35), 
                            text_input="EASY_MODE", font=get_font(25), base_color="White", hovering_color="Green")
        EASY_BUTTON.changeColor(PLAY_MOUSE_POS)
        EASY_BUTTON.update(SCREEN)
        #normal
        NORMAL_BUTTON = Button(image=None, pos=(215, 90), 
                            text_input="NORMAL_MODE", font=get_font(25), base_color="White", hovering_color="Green")
        NORMAL_BUTTON.changeColor(PLAY_MOUSE_POS)
        NORMAL_BUTTON.update(SCREEN)
        #hard
        HARD_BUTTON = Button(image=None, pos=(215, 145), 
                            text_input="HARD_MODE", font=get_font(25), base_color="White", hovering_color="Green")
        HARD_BUTTON.changeColor(PLAY_MOUSE_POS)
        HARD_BUTTON.update(SCREEN)
        #super_hard 
        SUPER_HARD_BUTTON = Button(image=None, pos=(215, 200), 
                            text_input="SUPER_HARD_MODE", font=get_font(25), base_color="White", hovering_color="Green")
        SUPER_HARD_BUTTON.changeColor(PLAY_MOUSE_POS)
        SUPER_HARD_BUTTON.update(SCREEN)
        PLAY_BACK = Button(image=None, pos=(30, 515), 
                            text_input="BACK", font=get_font(10), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play() 
                if EASY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    Easy.reset()
                    easy_mode()
                    score_Easy = Easy.getScore()
                if NORMAL_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    normal.reset()
                    normal_mode()
                    score_normal = normal.getScore()
                if HARD_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    Hard.reset()
                    hard_mode()
                    score_Hard = Hard.getScore()
                if SUPER_HARD_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    Super_hard.reset()
                    super_hard_mode()
                    score_Super_hard = Super_hard.getScore()
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def easy_mode():
    global bestScore_easy, bestScore_normal, bestScore_hard, bestScore_Super_hard
    global score_Super_hard, score_Hard, score_normal, score_Easy
    while True:
        EASY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(scaled_image_pacman,(165,100))
        EASY_BACK = Button(image=None, pos=(30, 515), 
                            text_input="BACK", font=get_font(10), base_color="White", hovering_color="Green")
        Easy.main()
        score_Easy = Easy.getScore()
        EASY_BACK.changeColor(EASY_MOUSE_POS)
        EASY_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BACK.checkForInput(EASY_MOUSE_POS):
                    Score(1) 
        pygame.display.update()
def normal_mode():
    global bestScore_easy, bestScore_normal, bestScore_hard, bestScore_Super_hard
    global score_Super_hard, score_Hard, score_normal, score_Easy
    while True:
        NORMAL_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(scaled_image_pacman,(165,100))

        NORMAL_BACK = Button(image=None, pos=(30, 515), 
                            text_input="BACK", font=get_font(10), base_color="White", hovering_color="Green")
        normal.main()
        score_normal = normal.getScore()
        NORMAL_BACK.changeColor(NORMAL_MOUSE_POS)
        NORMAL_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NORMAL_BACK.checkForInput(NORMAL_MOUSE_POS):
                    Score(2) 
        pygame.display.update()
def hard_mode():
    global bestScore_easy, bestScore_normal, bestScore_hard, bestScore_Super_hard
    global score_Super_hard, score_Hard, score_normal, score_Easy
    while True:
        HARD_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(scaled_image_pacman,(165,100))

        HARD_BACK = Button(image=None, pos=(30, 515), 
                            text_input="BACK", font=get_font(10), base_color="White", hovering_color="Green")
        Hard.main()
        score_Hard = Hard.getScore()
        HARD_BACK.changeColor(HARD_MOUSE_POS)
        HARD_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play() 
                if HARD_BACK.checkForInput(HARD_MOUSE_POS):
                    Score(3) 
        pygame.display.update()
def super_hard_mode():
    global bestScore_easy, bestScore_normal, bestScore_hard, bestScore_Super_hard
    global score_Super_hard, score_Hard, score_normal, score_Easy
    while True:  
        SUPER_HARD_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(scaled_image_pacman,(165,100))
        

        #cn_kho.pygame.quit()
        SUPER_HARD_BACK = Button(image=None, pos=(30, 515), 
                            text_input="BACK", font=get_font(10), base_color="White", hovering_color="Green")
        Super_hard.main()
        score_Super_hard = Super_hard.getScore()
        SUPER_HARD_BACK.changeColor(SUPER_HARD_MOUSE_POS)
        SUPER_HARD_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play() 
                if SUPER_HARD_BACK.checkForInput(SUPER_HARD_MOUSE_POS):
                    # play()
                    Score(4)     
        pygame.display.update()

def drawString(name, xPos, yPos):
    font = pygame.font.Font("res/font/font.ttf", 10)
    text = font.render(name, False, (255, 255, 255))
    SCREEN.blit(text, (xPos, yPos))

def Score(check):
    global bestScore_easy, bestScore_normal, bestScore_hard, bestScore_Super_hard
    global score_Super_hard, score_Hard, score_normal, score_Easy
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(scaled_image_pacman,(165,150))
        if(score_Super_hard > bestScore_Super_hard):
            bestScore_Super_hard = score_Super_hard
        
        s = "SCORE " 
        ok = 0
        if check == 1:
            if(score_Easy > bestScore_easy):
                bestScore_easy = score_Easy
                tmp = Button(image=None, pos=(215, 60), 
                            text_input="Congratulations on creating a new record !!!", font=get_font(15), base_color="yellow", hovering_color="Green")
                tmp.changeColor(PLAY_MOUSE_POS)
                tmp.update(SCREEN)
                ok = 1
            s = s + "EASY: " + str(score_Easy)
        elif check == 2:
            if(score_normal > bestScore_normal):
                bestScore_normal = score_normal
                tmp = Button(image=None, pos=(215, 160), 
                            text_input="Congratulations on creating a new record !!!", font=get_font(15), base_color="yellow", hovering_color="Green")
                tmp.changeColor(PLAY_MOUSE_POS)
                tmp.update(SCREEN)
                ok = 1
            s += "NORMAL: " + str(score_normal)
        elif check == 3:
            if(score_Hard > bestScore_hard):
                bestScore_hard = score_Hard
                tmp = Button(image=None, pos=(215, 160), 
                            text_input="Congratulations on creating a new record !!!", font=get_font(15), base_color="yellow", hovering_color="Green")
                tmp.changeColor(PLAY_MOUSE_POS)
                tmp.update(SCREEN)
                ok = 1
            s += "HARD: " + str(score_Hard)
        else: 
            if(score_Super_hard > bestScore_Super_hard):
                bestScore_Super_hard = score_Super_hard
                tmp = Button(image=None, pos=(215, 160), 
                            text_input="Congratulations on creating a new record !!!", font=get_font(15), base_color="yellow", hovering_color="Green")
                tmp.changeColor(PLAY_MOUSE_POS)
                tmp.update(SCREEN)
                ok = 1
            s += "SUPER HARD: " + str(score_Super_hard)
        cur_score = Button(image=None, pos=(215, 35), 
                            text_input=s , font=get_font(10), base_color="pink", hovering_color="Green")
        cur_score.changeColor(PLAY_MOUSE_POS)
        cur_score.update(SCREEN)
        #H.
        KY_LUC = Button(image=None, pos=(215, 100), 
                            text_input="BEST SCORE" , font=get_font(20), base_color="pink", hovering_color="Green")
        KY_LUC.changeColor(PLAY_MOUSE_POS)
        KY_LUC.update(SCREEN)

        EASY = Button(image=None, pos=(215, 125), 
                            text_input="EASY: " + str(bestScore_easy) , font=get_font(15), base_color="pink", hovering_color="Green")
        EASY.changeColor(PLAY_MOUSE_POS)
        EASY.update(SCREEN)

        NORMAL = Button(image=None, pos=(215, 150), 
                            text_input="NORMAL: " + str(bestScore_normal) , font=get_font(15), base_color="pink", hovering_color="Green")
        NORMAL.changeColor(PLAY_MOUSE_POS)
        NORMAL.update(SCREEN)

        HARD = Button(image=None, pos=(215, 175), 
                            text_input="HARD: " + str(bestScore_hard) , font=get_font(15), base_color="pink", hovering_color="Green")
        HARD.changeColor(PLAY_MOUSE_POS)
        HARD.update(SCREEN)

        SUPER_HARD = Button(image=None, pos=(215, 200), 
                            text_input="SUPER HARD: " + str(bestScore_Super_hard) , font=get_font(15), base_color="pink", hovering_color="Green")
        SUPER_HARD.changeColor(PLAY_MOUSE_POS)
        SUPER_HARD.update(SCREEN)
        if(ok == 1):
            tmp = Button(image=None, pos=(215, 160), 
                            text_input="Congratulations on creating a new record !!!", font=get_font(15), base_color="yellow", hovering_color="Green")
            tmp.changeColor(PLAY_MOUSE_POS)
            tmp.update(SCREEN)
        PLAY_BACK = Button(image=None, pos=(30, 515), 
                            text_input="BACK", font=get_font(10), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    play()

        pygame.display.update()

def rule():
    while True:
        RULE_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(scaled_image_pacman,(165,100))
        
        
        text1="+  In Pac-Man, players control the main character, Pac-Man, a yellow,"
        text4=" round character, to eat all the dots (referred to as 'dots') in a maze."
        text2="+  The goal is to eat all the dots in the maze while avoiding"
        text5=" being pursued by four ghosts (Inky, Pinky, Blinky, and Clyde)."
        text3="+  Players can also eat 'Power Pellets' to temporarily weaken "
        text6="the ghosts and turn the tables by chasing them instead."
    

        RULE_TEXT1 = get_font(6).render(text1, True, "white")
        RULE_RECT1 = RULE_TEXT1.get_rect(center=(215, 80))
        SCREEN.blit(RULE_TEXT1, RULE_RECT1)

        RULE_TEXT4 = get_font(6).render(text4, True, "white")
        RULE_RECT4 = RULE_TEXT4.get_rect(center=(215, 100))
        SCREEN.blit(RULE_TEXT4, RULE_RECT4)

        RULE_TEXT2 = get_font(6).render(text2, True, "white")
        RULE_RECT2 = RULE_TEXT2.get_rect(center=(215, 115))
        SCREEN.blit(RULE_TEXT2, RULE_RECT2)

        RULE_TEXT5 = get_font(6).render(text5, True, "white")
        RULE_RECT5 = RULE_TEXT5.get_rect(center=(215, 130))
        SCREEN.blit(RULE_TEXT5, RULE_RECT5)

        RULE_TEXT3 = get_font(6).render(text3, True, "white")
        RULE_RECT3 = RULE_TEXT3.get_rect(center=(215, 145))
        SCREEN.blit(RULE_TEXT3, RULE_RECT3)

        RULE_TEXT6 = get_font(6).render(text6, True, "white")
        RULE_RECT6 = RULE_TEXT6.get_rect(center=(215, 160))
        SCREEN.blit(RULE_TEXT6, RULE_RECT6)

        RULE_BACK = Button(image=None, pos=(70, 515), 
                            text_input="BACK", font=get_font(10), base_color="white", hovering_color="Green")

        RULE_BACK.changeColor(RULE_MOUSE_POS)
        RULE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play() 
                if RULE_BACK.checkForInput(RULE_MOUSE_POS):
                    main_menu()

        pygame.display.update()
corner_rect = pygame.Rect(0, SCREEN_HEIGHT-30, 50, 50)  # Ví dụ: góc trên bên trái với kích thước 200x200

# Màu bạn muốn đổ
corner_color = (0, 0, 0)  # Màu đen
def main_menu():
    while True:
        SCREEN.blit(scaled_image_BG, (0, 0))
        pygame.draw.rect(SCREEN, corner_color, corner_rect)
        MENU_MOUSE_POS = pygame.mouse.get_pos()



        PLAY_BUTTON = Button(image=None, pos=(225, 315), 
                            text_input="PLAY", font=get_font(25), base_color="#FF0000", hovering_color="White")
        RULE_BUTTON = Button(image=None, pos=(225, 365), 
                            text_input="RULES", font=get_font(25), base_color="#FF0000", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(225, 415), 
                            text_input="QUIT", font=get_font(25), base_color="#FF0000", hovering_color="White")



        for button in [PLAY_BUTTON, RULE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play() 
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if RULE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    rule()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()