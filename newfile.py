# Import the pygame library and initialise the game engine
import pygame
from random import randint
pygame.init()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
class Ball(pygame.sprite.Sprite):
   # This class represents a ball. It derives from the "Sprite" class in Pygame.

   def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       super().__init__()

       # Pass in the color of the ball, its width and height.
       # Set the background color and set it to be transparent
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       self.velocity = [randint(4, 8), randint(-8, 8)]

       # Fetch the rectangle object that has the dimensions of the image.
       self.rect = self.image.get_rect()

   def update(self):
       self.rect.x += self.velocity[0]
       self.rect.y += self.velocity[1]

   def bounce(self):
       self.velocity[0] = -self.velocity[0]
       self.velocity[1] = randint(-8, 8)


class Paddle(pygame.sprite.Sprite):
   # This class represents a paddle. It derives from the "Sprite" class in Pygame.

   def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       super().__init__()

       # Pass in the color of the Paddle, its width and height.
       # Set the background color and set it to be transparent
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image.
       self.rect = self.image.get_rect()

   def moveUp(self, pixels):
       self.rect.y -= pixels
       # Check that you are not going too far (off the screen)
       if self.rect.y < 0:
           self.rect.y = 0

   def moveDown(self, pixels):
       self.rect.y += pixels
       # Check that you are not going too far (off the screen)
       if self.rect.y > 400:
           self.rect.y = 400


# Open a new window
size = (1000, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Add the 2 paddles and the ball to the list of objects
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
print("Hello")
while(True):
    s = 1