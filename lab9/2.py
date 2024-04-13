import pygame
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20
FONT_SIZE = 24
FONT = pygame.font.Font(None, FONT_SIZE)

# Define directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Define snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def turn(self, direction):
        if self.length > 1 and (direction[0] * -1, direction[1] * -1) == self.direction:
            return
        else:
            self.direction = direction

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * BLOCK_SIZE)) % SCREEN_WIDTH), (cur[1] + (y * BLOCK_SIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)

# Define food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.timer = 200  # Timer for disappearing food
        self.weight = random.randint(1, 5)  # Weight of the food

    def randomize_position(self):
        self.position = (random.randint(0, (SCREEN_WIDTH // BLOCK_SIZE - 1)) * BLOCK_SIZE, 
                         random.randint(0, (SCREEN_HEIGHT // BLOCK_SIZE - 1)) * BLOCK_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, BLACK, r, 1)

    def update_timer(self):
        self.timer -= 1
        if self.timer <= 0:
            self.position = (-BLOCK_SIZE, -BLOCK_SIZE)  # Move food off-screen to simulate disappearance

# Define main function
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    snake = Snake()
    foods = [Food() for _ in range(5)]  # Create a list of 5 foods

    score = 0
    level = 1
    FPS = 10

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.turn(UP)
                elif event.key == pygame.K_DOWN:
                    snake.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.turn(RIGHT)

        snake.move()

        # Check if snake eats any food
        for food in foods:
            if snake.get_head_position() == food.position:
                snake.length += food.weight  # Increase snake length based on food weight
                score += food.weight * 10  # Increase score based on food weight
                food.timer = 200  # Reset the timer for disappearing food
                food.randomize_position()  # Randomize the position of the food

        # Update timer for disappearing foods
        for food in foods:
            food.update_timer()

        screen.fill(WHITE)
        snake.draw(screen)
        for food in foods:
            food.draw(screen)

        # Display score and level
        score_text = FONT.render(f'Score: {score}', True, BLACK)
        level_text = FONT.render(f'Level: {level}', True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 10 + FONT_SIZE))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
