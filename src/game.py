import pygame
import sys
import TictactoeMain as game
import time

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600

# Set the dimensions of the board
BOARD_SIZE = 3
CELL_SIZE = 100

# Set the position of the board within the screen
BOARD_X = (SCREEN_WIDTH - BOARD_SIZE * CELL_SIZE) // 2
BOARD_Y = (SCREEN_HEIGHT - BOARD_SIZE * CELL_SIZE) // 2

# Set the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Tic Tac Toe Game")

# Create a game instance
game_instance = game.TictactoeMain()

# Create a font object
def textPrint(content):
    pygame.font.init()
    font = pygame.font.SysFont('Lucida Console', 20)
    text = font.render(content, True, (255, 255, 255))
    textpos = text.get_rect(centerx=screen.get_width() / 2, y=500)
    screen.blit(text, textpos)

# Function to handle Pygame events
def handle_eventsHuman():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the click
            pos = pygame.mouse.get_pos()
            # Convert the position to a cell index
            cell_x = (pos[0] - BOARD_X) // CELL_SIZE
            cell_y = (pos[1] - BOARD_Y) // CELL_SIZE
            # Make a move at the clicked position
            if cell_x >= 0 and cell_x < BOARD_SIZE and cell_y >= 0 and cell_y < BOARD_SIZE:
                position = cell_y * BOARD_SIZE + cell_x + 1
                game_instance.playerMove(game_instance.BOARD, position)
                if not game_instance.terminalState(game_instance.BOARD):
                    print("hello")
                    game_instance.computerMove(game_instance.BOARD)
            else: 
                return 
                

def handle_eventsComp():
    if not game_instance.terminalState(game_instance.BOARD):
        game_instance.computerMove(game_instance.BOARD)
    else:
        return
    
             
# Draw the board
def draw_board():
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLACK, (BOARD_X, BOARD_Y, BOARD_SIZE * CELL_SIZE, BOARD_SIZE * CELL_SIZE), 2)
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, WHITE, (BOARD_X, BOARD_Y + i*CELL_SIZE), (BOARD_X + BOARD_SIZE * CELL_SIZE, BOARD_Y + i*CELL_SIZE), 2)
        pygame.draw.line(screen, WHITE, (BOARD_X + i*CELL_SIZE, BOARD_Y), (BOARD_X + i*CELL_SIZE, BOARD_Y + BOARD_SIZE * CELL_SIZE), 2)

# Draw the game pieces
def draw_pieces():
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            position = y * BOARD_SIZE + x + 1
            row, col = game_instance.getPosition(position)
            if game_instance.BOARD[row][col] == game_instance.HUMAN:
                pygame.draw.line(screen, WHITE, (BOARD_X + x*CELL_SIZE + 20, BOARD_Y + y*CELL_SIZE + 20), (BOARD_X + (x+1)*CELL_SIZE - 20, BOARD_Y + (y+1)*CELL_SIZE - 20), 5)
                pygame.draw.line(screen, WHITE, (BOARD_X + (x+1)*CELL_SIZE - 20, BOARD_Y + y*CELL_SIZE + 20), (BOARD_X + x*CELL_SIZE + 20, BOARD_Y + (y+1)*CELL_SIZE - 20), 5)
            elif game_instance.BOARD[row][col] == game_instance.COMP:
                pygame.draw.circle(screen, WHITE, (BOARD_X + x*CELL_SIZE + CELL_SIZE//2, BOARD_Y + y*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//2 - 20, 5)

# Main game loop
gameRunning = True

text = "Welcome to this game of Tic Tac Toe!"
while gameRunning:
    handle_eventsHuman()
    draw_board()
    draw_pieces()
    textPrint(text)
    pygame.display.flip()

    
    # Check if the game is over
    if game_instance.terminalState(game_instance.BOARD):
        winner = game_instance.declareWinner(game_instance.BOARD)
        if winner == game_instance.HUMAN:
            text = "You win!"

        elif winner == game_instance.COMP:
            text = "Computer wins!"

        else:
            text = "It's a tie!"

