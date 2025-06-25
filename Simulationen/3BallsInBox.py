import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

class Ball:
    def __init__(self, x, y, radius, color, dx, dy):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = dx
        self.dy = dy

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off walls
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.dx = -self.dx
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.dy = -self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def check_collision(self, other):
        # Calculate distance between balls
        dist = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        if dist < self.radius + other.radius:
            # Simple elastic collision
            self.dx, other.dx = other.dx, self.dx
            self.dy, other.dy = other.dy, self.dy

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Ball Collision")

# create balls
ball1 = Ball(x=random.randint(50, WIDTH-50),
             y=random.randint(50, HEIGHT-50),
             radius=20, color=RED,
             dx=random.choice([-4, 4]), dy=random.choice([-4, 4]))

ball2 = Ball(x=random.randint(50, WIDTH-50),
             y=random.randint(50, HEIGHT-50),
             radius=20, color=BLUE,
             dx=random.choice([-4, 4]), dy=random.choice([-4, 4]))

ball3 = Ball(x=random.randint(50, WIDTH-50),
             y=random.randint(50, HEIGHT-50),
             radius=20, color=GREEN,
             dx=random.choice([-4, 4]), dy=random.choice([-4, 4]))

# Clock to control frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the balls
    ball1.move()
    ball2.move()
    ball3.move()

    # Check for collisions
    ball1.check_collision(ball2)
    ball1.check_collision(ball3)
    ball2.check_collision(ball3)

    # Draw everything
    screen.fill(BLACK)
    ball1.draw(screen)
    ball2.draw(screen)
    ball3.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

