import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1200, 900

Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ball class
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

            # Resolve overlap
            overlap = self.radius + other.radius - dist
            angle = math.atan2(other.y - self.y, other.x - self.x)
            self.x -= math.cos(angle) * overlap / 2
            self.y -= math.sin(angle) * overlap / 2
            other.x += math.cos(angle) * overlap / 2
            other.y += math.sin(angle) * overlap / 2

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gas Simulation")

# Create 50 small balls
balls = []
for _ in range(100):
    ball = Ball(x=random.randint(20, WIDTH-20),
                y=random.randint(20, HEIGHT-20),
                radius=10,
                color=(random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)),
                dx=random.choice([-3, -2, -1, 1, 2, 3]),
                dy=random.choice([-3, -2, -1, 1, 2, 3]))
    balls.append(ball)

# Clock to control frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the balls
    for ball in balls:
        ball.move()

    # Check for collisions between balls
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            balls[i].check_collision(balls[j])

    # Draw everything
    screen.fill(BLACK)
    for ball in balls:
        ball.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()

