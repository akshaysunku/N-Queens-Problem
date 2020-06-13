import pygame
import sys


def draw(node, stop, delay):  
    pygame.init()
    paused = False
    resume = True
    
    while resume:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # Pausing
                    paused = not paused
                
        if not paused:            
            if stop == 0:
            # Define some colors
                BLACK = (0, 0, 0)
                WHITE = (255, 255, 255)
                RED = (255, 0, 0)
                 
                # This sets the WIDTH and HEIGHT of each grid location
                WIDTH = 50
                HEIGHT = 50
                 
                # This sets the margin between each cell
                MARGIN = 5
                 
                # Create a 2 dimensional array. A two dimensional array is simply a list of lists.
                GRIDSIZE = len(node.state)
                grid = []
                for row in range(GRIDSIZE):
                    # Add an empty array that will hold each cell in this row
                    grid.append([])
                    for column in range(GRIDSIZE):
                        grid[row].append(0)  # Append a cell
                 
                # Initialize pygame
                pygame.init()
                 
                # Set the HEIGHT and WIDTH of the screen
                WINDOW_SIZE = [50*(GRIDSIZE+1), 50*(GRIDSIZE+1)]
                screen = pygame.display.set_mode(WINDOW_SIZE)
                 
                # Set title of screen
                pygame.display.set_caption("N-queens simulation")
                 
                # Set the screen background
                screen.fill(BLACK)
            
                # Draw the grid
                for row in range(GRIDSIZE):
                    for column in range(GRIDSIZE):
                        pygame.draw.rect(screen,   
                                         WHITE,
                                         [(MARGIN + WIDTH) * column + MARGIN,
                                          (MARGIN + HEIGHT) * row + MARGIN,
                                          WIDTH,
                                          HEIGHT])
                        
                for idx in range(len(node.state)):
                    if node.state[idx] != None:
                        row = node.state[idx]
                        column = idx
                        
                        for i in range(GRIDSIZE):
                            pygame.draw.rect(screen,   
                                     RED,
                                     [(MARGIN + WIDTH) * i + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])
                            
                        
                        for i in range(GRIDSIZE):
                            pygame.draw.rect(screen,   
                                     RED,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * i + MARGIN,
                                      WIDTH,
                                      HEIGHT])
                        
                        for i in range(GRIDSIZE):
                            if (row+i) < GRIDSIZE and (column+i) < GRIDSIZE:
                                pygame.draw.rect(screen,   
                                         RED,
                                         [(MARGIN + WIDTH) * (column+i) + MARGIN,
                                          (MARGIN + HEIGHT) * (row+i) + MARGIN,
                                          WIDTH,
                                          HEIGHT])
            
                        for i in range(GRIDSIZE):
                            if (row-i) >= 0 and (column+i) < GRIDSIZE:
                                pygame.draw.rect(screen,   
                                         RED,
                                         [(MARGIN + WIDTH) * (column+i) + MARGIN,
                                          (MARGIN + HEIGHT) * (row-i) + MARGIN,
                                          WIDTH,
                                          HEIGHT])
            
                        font = pygame.font.SysFont("comicsansms", 36)
                        text = font.render("Q", True, (0,0,0))
                        screen.blit(text, ((MARGIN + HEIGHT) * column + (3*MARGIN), (MARGIN + HEIGHT) * row + MARGIN))
                        
                        
                # Update the screen
                pygame.display.flip()
                pygame.time.wait(delay) 
                
                resume = False
                
            elif stop == 1:
                # on exit.
                pygame.quit()
                sys.exit("End of simulation")