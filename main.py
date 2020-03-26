# Imports and Boot

import pygame
pygame.init()

# Load

spritePack = {
    'simple': {
        'stayR': [pygame.image.load(f'sprite/cat/pack/sprite_cat_stay_r_{i}.png') for i in range(4)],
        'stayL': [pygame.image.load(f'sprite/cat/pack/sprite_cat_stay_l_{i}.png') for i in range(4)],
        'runR': [pygame.image.load(f'sprite/cat/pack/sprite_cat_run_r_{i}.png') for i in range(4)],
        'runL': [pygame.image.load(f'sprite/cat/pack/sprite_cat_run_l_{i}.png') for i in range(4)],
        'jumpR': [pygame.image.load(f'sprite/cat/pack/sprite_cat_jump_r_{i}.png') for i in range(4)],
        'jumpL': [pygame.image.load(f'sprite/cat/pack/sprite_cat_jump_l_{i}.png') for i in range(4)],
        'fallR': [pygame.image.load(f'sprite/cat/pack/sprite_cat_fall_r_{i}.png') for i in range(4)],
        'fallL': [pygame.image.load(f'sprite/cat/pack/sprite_cat_fall_l_{i}.png') for i in range(4)]
    },
    'super': {
        'stayR': [pygame.image.load(f'sprite/cat/pack/sprite_scat_stay_r_{i}.png') for i in range(4)],
        'stayL': [pygame.image.load(f'sprite/cat/pack/sprite_scat_stay_l_{i}.png') for i in range(4)],
        'runR': [pygame.image.load(f'sprite/cat/pack/sprite_scat_run_r_{i}.png') for i in range(4)],
        'runL': [pygame.image.load(f'sprite/cat/pack/sprite_scat_run_l_{i}.png') for i in range(4)],
        'jumpR': [pygame.image.load(f'sprite/cat/pack/sprite_scat_jump_r_{i}.png') for i in range(4)],
        'jumpL': [pygame.image.load(f'sprite/cat/pack/sprite_scat_jump_l_{i}.png') for i in range(4)],
        'fallR': [pygame.image.load(f'sprite/cat/pack/sprite_scat_fall_r_{i}.png') for i in range(4)],
        'fallL': [pygame.image.load(f'sprite/cat/pack/sprite_scat_fall_l_{i}.png') for i in range(4)]
    }
}

# Window

win_size = (640, 480)
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("The Game")
font = pygame.font.Font('freesansbold.ttf', 16)
clock = pygame.time.Clock()  # FPS

# Characther

class characther:
    # Position
    xPos, yPos = 100, 415
    
    # Stats
    isSuper = False
    inJump = False
    isFalling = False
    isRunnig = False
    faceDirection = 'RIGHT'
    stepCount = 0
    stayCount = 0
    jumpCount = 10  # Jump "force"
    speed = 20  # Move speed
    energy = 0
    coins = 0
    hp = 6
    lifes = 3
    
    # Color
    color = 255, 255, 255
    
    # Size
    size = w, h = 40, 65
    
    # New
    def _init_(self, x = xPos, y = yPos, w = size[0], h = size[1], s = speed):
        self.xPos = x
        self.yPos = y
        self.w = w
        self.h = h
        self.size = w, h
        self.speed = s
    
    # Gets
    def get_all(self):
        return self.xPos, self.yPos, self.w, self.h
    
    # Sets
    def set_color(self, c: tuple = ()):
        if len(c) == 3:
            self.color = c
        else:
            print('Isso num é uma cor!')
    
    def jump(self):
        self.inJump = True
    
    def left(self):
        self.isRunnig = True
        self.faceDirection = 'LEFT'
        self.walking_left()
    
    def step(self):
        if self.stepCount +1 >= 4:
            self.stepCount = 0
        else:
            self.stepCount += 1
    
    def right(self):
        self.isRunnig = True
        self.faceDirection = 'RIGHT'
        self.walking_right()
    
    def stay(self):
        self.isRunnig = False
        self.stepCount = 0
        if self.stayCount +1 >= 4:
            self.stayCount = 0
        else:
            self.stayCount += 1
    
    def super(self):
        self.isSuper = not self.isSuper
    
    # Move
    def walking_left(self, t=1):
        self.xPos -= self.speed * t
    
    def walking_right(self, t=1):
        self.xPos += self.speed * t
    '''
    def up(self, t=1):
        self.yPos -= self.speed * t
    
    def down(self, t=1):
        self.yPos += self.speed * t
    '''
    def jumping(self, c=10):
            if self.jumpCount >= -c:
                i = 1
                if self.jumpCount < 0:
                    i = -1
                    self.isFalling = True
                self.yPos -= int(i * self.jumpCount ** 2  / 2)  # In the pygame the possition is a integer number // No pygame a posição deve ser dada em inteiros
                self.jumpCount -= 1
            else:
                self.isFalling = False
                self.inJump = False
                self.jumpCount = c
                self.stayCount = 2  # The sprite 2 is perfect for final of fall


# Set characters

cat = characther()


# Game

def debugging():
    stats = [
        font.render("Jump: " + str(cat.inJump), True, (0, 255, 0)), 
        font.render("Fall: " + str(cat.isFalling), True, (0, 255, 0)), 
        font.render("Run: " + str(cat.isRunnig), True, (0, 255, 0)),
        font.render("Dir: " + cat.faceDirection, True, (0, 255, 0)),
        font.render("Step Run: " + str(cat.stepCount), True, (0, 255, 0)),
        font.render("Step Jump: " + str(cat.jumpCount), True, (0, 255, 0)),
        font.render("Step Stay: " + str(cat.stayCount), True, (0, 255, 0)),
        ]
    for i, text in enumerate(stats):
        screen.blit(text, ((win_size[0] - text.get_width()), i*(text.get_height() + 10)))


def redrawGameWindow():
    
    sprite_mode, sprite_act, sprite_index = 'simple', str(), int()
    if cat.isSuper:
        sprite_mode = 'super'
    if cat.inJump:
        if cat.isFalling:
            sprite_act = 'fall' + cat.faceDirection[0]
            sprite_index = int(cat.jumpCount % 4)
        else:
            sprite_act = 'jump' + cat.faceDirection[0]
            sprite_index = int(cat.jumpCount % 4)
    elif cat.isRunnig:
            sprite_act = 'run' + cat.faceDirection[0]
            sprite_index = cat.stepCount
    else:
        sprite_act = 'stay' + cat.faceDirection[0]
        sprite_index = cat.stayCount
    
    screen.fill((255, 255, 255))
    screen.blit(pygame.transform.scale(spritePack[sprite_mode][sprite_act][sprite_index], cat.size), (cat.xPos, cat.yPos - 4))  # "-4" por convenção do sprite
    
    # pygame.draw.rect(screen, cat.color, cat.get_all())
    debugging()
    pygame.display.update()


runGame = True
while runGame:
    
    clock.tick(9) # FPS
    
    # bye bye
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
    
    # movement
    keys = pygame.key.get_pressed()
    
    if (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and not (keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):  # Xor Logic Gate: True if just one is True
        if keys[pygame.K_LEFT]:
            cat.step()
            if cat.xPos > 0:
                cat.left()
    
        elif keys[pygame.K_RIGHT]:
            cat.step()
            if cat.xPos + cat.w < win_size[0]:
                cat.right()    
    elif not cat.inJump:
        cat.stay()
    
    if not cat.inJump:
        ''' climbing
        if keys[pygame.K_UP] and cat.yPos > 0:
            if cat.yPos <= 5:
                cat.up(5/cat.speed)
            else:
                cat.up()
    
        if keys[pygame.K_DOWN] and cat.yPos + cat.h < win_size[1]:
            if cat.yPos <= 5:
                cat.down(5/cat.speed)
            else:
                cat.down()
        '''
        if keys[pygame.K_SPACE]:
            cat.jump()
            cat.jumping()
    else:
        cat.jumping()
    
    if keys[pygame.K_RSHIFT]:
        cat.super()
    
    # Render
    
    redrawGameWindow()

pygame.quit()
