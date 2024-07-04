import pygame
import os,random,time,math,sys


width = 1200
height = 800
fps = 30
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
tank_image = pygame.image.load("tank\m_unnamed.png").convert_alpha()
enemy_tank_image = pygame.image.load("tank\i.png").convert_alpha()
second_tank_image = pygame.image.load("tank\\i2.png").convert_alpha()
x = 500
y = 300
acid_image = pygame.image.load("tank\m_acid_texture_300px.png").convert_alpha()
flag_image = pygame.image.load("tank\\flag.png").convert_alpha()
bullet_image = pygame.image.load("tank\\bullet.png").convert_alpha()
my_font = pygame.font.SysFont("Times New Roman",30)
pygame.display.set_caption("Tank Online")
score = 0
life_of_enemy = 5
life_of_enemy_tank = 5
life_of_second = 5 

all_sprites = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
speed_of_tank = 5


class Tank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = tank_image
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (width /2 , 600)
        self.angle = 0

        
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keys = pygame.key.get_pressed()
            #TODO ROTATION
        if keys[pygame.K_RIGHT]:
            self.speedx += 5
            self.angle -= 5
            self.rotate()
        if keys[pygame.K_LEFT]:
            self.speedx -= 5
            self.angle += 5
            self.rotate()
        if keys[pygame.K_UP]:
            self.speedy -= speed_of_tank
        if keys[pygame.K_DOWN]:
            self.speedy += speed_of_tank


        
        self.rect.x += self.speedx
        self.rect.y += self.speedy


        if self.rect.right >= width:
            self.rect.right = width
        
        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= height:
            self.rect.bottom = height

    
    
    
    #TODO ROTATION
    def rotate(self):
        self.image = pygame.transform.rotate(self.original_image,self.angle)
        self.rect = self.image.get_rect(center =self.rect.center)


class AcidObj(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = acid_image
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, 282)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((width,30))
        self.image.fill((192,192,192))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0,200)

class Flag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = flag_image
        self.rect = self.image.get_rect()
        self.rect.center = (400,400)


class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):
        self.rect.y -= 10
        if self.rect.bottom <= 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = tank_image
        self.orig_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (200, 450)
        self.directionx = 1
        self.directiony = 0


    def movement(self):
        self.rect.x += 5 * self.directionx
        self.rect.y += 5 * self.directiony

        if self.rect.right >= width:
            self.rect.right = width
            self.directionx = 0
            self.directiony = 1


        if self.rect.bottom >= height:
            self.rect.bottom = height
            self.directionx = -1
            self.directiony = 0

        
        if self.rect.left < 0:
            self.rect.left = 0
            self.directionx = 0
            self.directiony = -1


        if self.rect.top <= 0:
            self.rect.top = 0
            self.directionx = 1
            self.directiony += 0

        
        



tank = Tank()
acid = AcidObj()
secondAcid = AcidObj()
obstacle = Obstacle()
flag = Flag()
enemy = Enemy()
enemy_tank = Enemy()
second_enemy_tank = Enemy()


secondAcid.rect.bottomleft = (1100,282)
all_sprites.add(tank)
all_sprites.add(acid)
all_sprites.add(obstacle)
all_sprites.add(enemy)
all_sprites.add(secondAcid)
all_sprites.add(flag)
running = True
angle = 0
 


#TODO Добавление кнопки
my_text = pygame.font.SysFont("Times New Roman",20)
button_surface = pygame.Surface((150,50))
button_text = my_text.render("Start the game",True,(0,0,0))
text_rect = button_text.get_rect(center = (button_surface.get_width() / 2 , button_surface.get_height() /2))
button_rect = pygame.Rect(500,200,600,400)

#TODO Добавление 2ой кнопки
quit_button = pygame.Surface((150,50))
quit_text = my_text.render("Quit the game",True,(0,0,0))
quit_text_rect = quit_text.get_rect(center = (quit_button.get_width() /2,quit_button.get_height() / 2))
quit_button_rect = pygame.Rect(500,600,600,400)



#TODO Начальный экран и кастомизация кнопки
main_menu = False
while (main_menu == False):
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                main_menu = True
        

    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface,(127,127,212),(1,1,148,48))
    else:
        pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)
    
        #TODO BUTTON'S
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
                


    if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(quit_button,(192,192,192),(1,1,148,48))
    else:
        pygame.draw.rect(quit_button, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(quit_button, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(quit_button, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(quit_button, (0, 100, 0), (1, 48, 148, 10), 2)
    
    
    button_surface.blit(button_text,text_rect)
    screen.blit(button_surface,(button_rect.x,button_rect.y))

    quit_button.blit(quit_text,quit_text_rect)
    screen.blit(quit_button,(quit_button_rect.x,quit_button_rect.y))
    pygame.display.flip()
    pygame.display.update()

    


paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet(tank.rect.centerx, tank.rect.top)
            all_sprites.add(bullet)
            bullet_group.add(bullet)
            pygame.mixer.music.load("tank\\movie_1.mp3")
            pygame.mixer.music.set_volume(1.1)
            pygame.mixer.music.play(1)
        
        
        #TODO Проверка на паузу
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
    


    all_sprites.update()
    if not paused:



        #Столкновение
        if pygame.sprite.collide_rect(tank,acid) or pygame.sprite.collide_rect(tank,secondAcid):
            time.sleep(1)
            running = False
        
        #Столкновение
        if pygame.sprite.collide_rect(tank,enemy) or pygame.sprite.collide_rect(tank,enemy_tank) or pygame.sprite.collide_rect(tank,second_enemy_tank):
            time.sleep(1)
            running = False

        randomNumberH = random.randint(300,height)
        randomNumberW = random.randint(1,width)
        rand_tank_h = random.randint(300,height)
        rand_tank_w = random.randint(1,width)
        
        #Столкновение
        if pygame.sprite.collide_rect(tank,flag):
            flag.rect.center = tank.rect.center
            if pygame.sprite.collide_rect(flag,obstacle):
                score +=1
                tank.rect.bottomright = (rand_tank_w,rand_tank_h)
                flag.rect.center = (randomNumberW, randomNumberH)
        

        random_enemy_w = random.randint(1,1100)
        random_enemy_h = random.randint(300,700)
        
       
       #Проверка на попадание пулей в танков
        
        if pygame.sprite.spritecollide(enemy,bullet_group,True):
            life_of_enemy -= 1
            if life_of_enemy == 0:
                enemy.rect.bottomleft = (random_enemy_w,random_enemy_h)
                score += 5
                life_of_enemy = 5
        
        #Столкновение
        if pygame.sprite.spritecollide(enemy_tank,bullet_group,True):
            life_of_enemy_tank -= 1
            if life_of_enemy_tank == 0:
                enemy_tank.rect.topleft = (10,10)
                score += 5
                life_of_enemy_tank = 5

        #Столкновение
        if pygame.sprite.spritecollide(second_enemy_tank,bullet_group,True):
            life_of_second -= 1
            if life_of_second == 0:
                second_enemy_tank.rect.center = (width,height)
                score += 5
                life_of_second = 5
        

        #* Передвижение танка самостоятельный
        enemy_tank.rect.x += 5
        enemy_tank.rect.y += 5
        
        #TODO Проверка на выход с рамки
        if enemy_tank.rect.y >= height:
            enemy_tank.rect.y = 0
        if enemy_tank.rect.x >= width:
            enemy_tank.rect.x = 0


        second_enemy_tank.rect.y += 10
        second_enemy_tank.rect.x += 10

        
        if second_enemy_tank.rect.x >= width:
            second_enemy_tank.rect.x = 0
        if second_enemy_tank.rect.y >= height:
            second_enemy_tank.rect.y = 0


        if score >= 100:
            print("Grats,you won the game")
            time.sleep(2)
            running = False


        enemy.movement()
        score_text = my_font.render(f"Score: {score}",True,(255,255,255))

        screen.fill((0,0,0))
        all_sprites.draw(screen)
        screen.blit(score_text,(10,10))
        screen.blit(enemy_tank_image,enemy_tank)
        screen.blit(second_tank_image,second_enemy_tank)

    else:
        screen.fill((192,192,192))
        text = my_font.render("Paused",True,(0,0,0))
        screen.blit(text,(width / 2 , height / 2))
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()

