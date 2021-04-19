import pygame

#------------------- SCREEN ----------------------------------------------------------------------------------------------------------------------------------------

pygame.init()

size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('TRON')

#------------------ VARIABLES------------------------------------------------------------------------------------------------------------------------------------------------------

FPS = 30
clock = pygame.time.Clock()

DARK_BLUE = (8, 27, 75)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
DARK_YELLOW = (170, 170, 3)
RED = (255, 0, 0)

yellow_direction = ''
yellow_x_change = 0
yellow_y_change = 0
yellow_x = 640
yellow_y = 640
yellow_stele_x = [yellow_x]
yellow_stele_y = [yellow_y]
red_direction = ''
red_x_change = 0
red_y_change = 0
red_x = 50
red_y = 50
red_stele_x = [red_x]
red_stele_y = [red_y]

title = pygame.font.Font(None, 100)

menu_title = title.render('TRON', True, WHITE)
menu_title_width, menu_title_height = title.size('TRON')

yellow_wins_title = title.render('YELLOW WINS', True, WHITE)
yellow_wins_title_width, yellow_wins_title_height = title.size('YELLOW WINS')

red_wins_title = title.render('RED WINS', True, WHITE)
red_wins_title_width, red_wins_title_height = title.size('RED WINS')

#------------------- CLASSES -----------------------------------------------------------------------------------------------------------------------------------------------

class Player():
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def draw_player(self, color, x, y):
        pygame.draw.rect(screen, color, [x, y, self.width, self.height])

    def draw__yellow_stele(self, color):
        for i in range(1, len(yellow_stele_x)):
            pygame.draw.rect(screen, color, [yellow_stele_x[i], yellow_stele_y[i], self.width, self.height])

    def draw__red_stele(self, color):
        for i in range(1, len(red_stele_x)):
            pygame.draw.rect(screen, color, [red_stele_x[i], red_stele_y[i], self.width, self.height])

class Button():
    def __init__(self):
        super().__init__()
    
    def draw_button(self, text_color, rect_color, x, y, width, height, text):
        btn_font = pygame.font.Font(None, 50)
        text_btn = btn_font.render(text, True, text_color)
        text_width, text_height = btn_font.size(text)
        pygame.draw.rect(screen, rect_color, [x, y, width, height])
        screen.blit(text_btn, (x + (width/2 - text_width/2), y + (height/2 - text_height/2)))

#------------------ FUNCTIONS ------------------------------------------------------------------------------------------------------------------------------------------------------

def update_menu():
    screen.fill(DARK_BLUE)
    screen.blit(menu_title, (((size[0] / 2) - (menu_title_width / 2)), 100))
    btn_play.draw_button(WHITE, BLACK, (size[0] / 2) - (200 / 2), 210, 200, 70, 'Play')
    btn_quit.draw_button(WHITE, BLACK, (size[0] / 2) - (200 / 2), 210 + 100, 200, 70, 'Quit')
    pygame.display.update()

def update_game():
    screen.fill(DARK_BLUE)
    draw_grid(70, 70, 700, 700, 5)
    yellow_player.draw_player(DARK_YELLOW, yellow_stele_x[0], yellow_stele_y[0])
    yellow_player.draw__yellow_stele(YELLOW)
    red_player.draw_player(RED, red_stele_x[0], red_stele_y[0])
    red_player.draw__red_stele(RED)
    pygame.display.update()

def update_yellow_wins():
    screen.fill(YELLOW)
    screen.blit(yellow_wins_title, (((size[0] / 2) - (yellow_wins_title_width / 2)), 100))
    btn_play.draw_button(WHITE, BLACK, (size[0] / 2) - (200 / 2), 210, 200, 70, 'Play')
    btn_quit.draw_button(WHITE, BLACK, (size[0] / 2) - (200 / 2), 210 + 100, 200, 70, 'Quit')
    pygame.display.update()

def update_red_wins():
    screen.fill(RED)
    screen.blit(red_wins_title, (((size[0] / 2) - (red_wins_title_width / 2)), 100))
    btn_play.draw_button(WHITE, BLACK, (size[0] / 2) - (200 / 2), 210, 200, 70, 'Play')
    btn_quit.draw_button(WHITE, BLACK, (size[0] / 2) - (200 / 2), 210 + 100, 200, 70, 'Quit')
    pygame.display.update()

def draw_grid(rect_width, rect_height, screen_width, screen_height, line_size):
    for i in range(rect_width, screen_width, rect_width):
        pygame.draw.line(screen, BLACK, (i, 0), (i, 700), line_size)

    for i in range(rect_height, screen_height, rect_height):
        pygame.draw.line(screen, BLACK, (0, i), (700, i), line_size)

#------------------ GAME LOOP-----------------------------------------------------------------------------------------------------------------------------------------------

yellow_player = Player(10, 10)
red_player = Player(10, 10)
btn_play = Button()
btn_quit = Button()

run = True
menu = True
play = False
yellow_wins = False
red_wins = False
while run:
    while menu:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x >= (size[0] / 2) - (200 / 2) and mouse_x <= ((size[0] / 2) - (200 / 2)) + 200:
                    if mouse_y >= 210 and mouse_y <= 210 + 70:
                        menu = False
                        play = True

                if mouse_x >= (size[0] / 2) - (200 / 2) and mouse_x <= ((size[0] / 2) - (200 / 2)) + 200:
                    if mouse_y >= 310 and mouse_y <= 310 + 70:
                        menu = False
                        run = False

        update_menu()

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and yellow_direction != 'DOWN':
                    yellow_direction = 'UP'

                if event.key == pygame.K_DOWN and yellow_direction != 'UP':
                    yellow_direction = 'DOWN'

                if event.key == pygame.K_RIGHT and yellow_direction != 'LEFT':
                    yellow_direction = 'RIGHT'

                if event.key == pygame.K_LEFT and yellow_direction != 'RIGHT':
                    yellow_direction = 'LEFT'

                if event.key == pygame.K_w and red_direction != 'DOWN':
                    red_direction = 'UP'

                if event.key == pygame.K_s and red_direction != 'UP':
                    red_direction = 'DOWN'

                if event.key == pygame.K_d and red_direction != 'LEFT':
                    red_direction = 'RIGHT'

                if event.key == pygame.K_a and red_direction != 'RIGHT':
                    red_direction = 'LEFT'

        if yellow_direction == 'UP':
            yellow_x_change = 0
            yellow_y_change = -yellow_player.height

        if yellow_direction == 'DOWN':
            yellow_x_change = 0
            yellow_y_change = yellow_player.height

        if yellow_direction == 'RIGHT':
            yellow_x_change = yellow_player.width
            yellow_y_change = 0

        if yellow_direction == 'LEFT':
            yellow_x_change = -yellow_player.width
            yellow_y_change = 0

        if red_direction == 'UP':
            red_x_change = 0
            red_y_change = -red_player.height

        if red_direction == 'DOWN':
            red_x_change = 0
            red_y_change = red_player.height

        if red_direction == 'RIGHT':
            red_x_change = red_player.width
            red_y_change = 0
    
        if red_direction == 'LEFT':
            red_x_change = -red_player.width
            red_y_change = 0

        yellow_x += yellow_x_change
        yellow_y += yellow_y_change

        red_x += red_x_change
        red_y += red_y_change

        if yellow_direction != '':
            yellow_stele_x.insert(0, yellow_x)
            yellow_stele_y.insert(0, yellow_y)

        if red_direction != '':
            red_stele_x.insert(0, red_x)
            red_stele_y.insert(0, red_y)

        if yellow_stele_x[0] < 0 or yellow_stele_x[0] > size[0] or yellow_stele_y[0] < 0 or yellow_stele_y[0] > size[1]:
            play = False
<<<<<<< HEAD
            red_wins = True
=======
            run = False
>>>>>>> 03a848fb33f760d8adf062c831ac91b695b33a88
            print('amarillo pierde')

        if red_stele_x[0] < 0 or red_stele_x[0] > size[0] or red_stele_y[0] < 0 or red_stele_y[0] > size[1]:
            play = False
<<<<<<< HEAD
            yellow_wins = True
=======
            run = False
>>>>>>> 03a848fb33f760d8adf062c831ac91b695b33a88
            print('rojo pierde')

        for i in range(1, len(yellow_stele_x)):
            if yellow_stele_x[0] == yellow_stele_x[i] and yellow_stele_y[0] == yellow_stele_y[i]:
                play = False
<<<<<<< HEAD
                red_wins = True
=======
                run = False
>>>>>>> 03a848fb33f760d8adf062c831ac91b695b33a88
                print('amarillo pierde')
            
            if red_stele_x[0] == yellow_stele_x[i] and red_stele_y[0] == yellow_stele_y[i]:
                play = False
<<<<<<< HEAD
                yellow_wins = True
=======
                run = False
>>>>>>> 03a848fb33f760d8adf062c831ac91b695b33a88
                print('red pierde')

        for i in range(1, len(red_stele_x)):
            if red_stele_x[0] == red_stele_x[i] and red_stele_y[0] == red_stele_y[i]:
                play = False
<<<<<<< HEAD
                yellow_wins = True
=======
                run = False
>>>>>>> 03a848fb33f760d8adf062c831ac91b695b33a88
                print('red pierde')

            if yellow_stele_x[0] == red_stele_x[i] and yellow_stele_y[0] == red_stele_y[i]:
                play = False
<<<<<<< HEAD
                red_wins = True
=======
                run = False
>>>>>>> 03a848fb33f760d8adf062c831ac91b695b33a88
                print('amarillo pierde')

        update_game()
        clock.tick(FPS)

    while yellow_wins:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                yellow_wins = False
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x >= (size[0] / 2) - (200 / 2) and mouse_x <= ((size[0] / 2) - (200 / 2)) + 200:
                    if mouse_y >= 210 and mouse_y <= 210 + 70:
                        yellow_stele_x.clear()
                        yellow_stele_y.clear()
                        red_stele_x.clear()
                        red_stele_y.clear()
                        yellow_direction = ''
                        yellow_x_change = 0
                        yellow_y_change = 0
                        yellow_x = 640
                        yellow_y = 640
                        yellow_stele_x = [yellow_x]
                        yellow_stele_y = [yellow_y]
                        red_direction = ''
                        red_x_change = 0
                        red_y_change = 0
                        red_x = 50
                        red_y = 50
                        red_stele_x = [red_x]
                        red_stele_y = [red_y]

                        yellow_wins = False
                        play = True

                if mouse_x >= (size[0] / 2) - (200 / 2) and mouse_x <= ((size[0] / 2) - (200 / 2)) + 200:
                    if mouse_y >= 310 and mouse_y <= 310 + 70:
                        yellow_wins = False
                        run = False

        update_yellow_wins()

    while red_wins:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                red_wins = False
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x >= (size[0] / 2) - (200 / 2) and mouse_x <= ((size[0] / 2) - (200 / 2)) + 200:
                    if mouse_y >= 210 and mouse_y <= 210 + 70:
                        yellow_stele_x.clear()
                        yellow_stele_y.clear()
                        red_stele_x.clear()
                        red_stele_y.clear()
                        yellow_direction = ''
                        yellow_x_change = 0
                        yellow_y_change = 0
                        yellow_x = 640
                        yellow_y = 640
                        yellow_stele_x = [yellow_x]
                        yellow_stele_y = [yellow_y]
                        red_direction = ''
                        red_x_change = 0
                        red_y_change = 0
                        red_x = 50
                        red_y = 50
                        red_stele_x = [red_x]
                        red_stele_y = [red_y]

                        red_wins = False
                        play = True

                if mouse_x >= (size[0] / 2) - (200 / 2) and mouse_x <= ((size[0] / 2) - (200 / 2)) + 200:
                    if mouse_y >= 310 and mouse_y <= 310 + 70:
                        red_wins = False
                        run = False

        update_red_wins()

pygame.quit()