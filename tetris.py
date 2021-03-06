import pygame, sys
from pygame.locals import * 
from random import randrange as rand 

DISPLAYSURF = pygame.display.set_mode((400,500))

cell_size = 18
cols = 10
rows = 22
maxfps = 30

#Colors
WHITE = (255, 255, 255)
GRAY = (185, 185, 185)
BLACK = (0, 0, 0)
RED = (155, 0, 0)
LIGHTRED = (175, 20, 20)
GREEN = (0, 155, 0)
LIGHTGREEN = (20, 175, 20)
BLUE = (0, 0, 155)
LIGHTBLUE = (20, 20, 175)
YELLOW = (155, 155, 0)
LIGHTYELLOW = (175, 175, 20)


# #Encoding of tetronimo shapes

# I_tetronimo = [[1, 1, 1, 1], 
# 				[[1], 
# 				 [1], 
# 				 [1], 
# 				 [1]]]

# O_tetronimo = [[2, 2], 
# 			   [2, 2]]

# T_tetronimo = [[[3, 3, 3], 
# 				[0, 3, 0]], 

# 				[[0, 3],
# 				 [3, 3],
# 				 [0, 3]], 

# 				[[3, 0], 
# 				 [3, 3], 
# 				 [3, 0]], 

# 				[[0, 3, 0], 
# 				 [3, 3, 3]]
# 				]

# S_tetronimo = [[[0, 4, 4], 
# 				 [4, 4, 0]], 

# 				[[4, 0], 
# 				  [4, 4], 
# 				  [0, 4]]
# 				  ]
# Z_tetronimo = [[[5, 5, 0], 
# 				[0, 5, 5]], 

# 				[0, 5], 
# 				[5, 5], 
# 				[5, 0]]

# J_tetronimo = [[[0, 6], 
# 				[0, 6], 
# 				[6, 6]], 

# 				[[6, 0, 0], 
# 				[6, 6, 6]], 

# 				[[7, 7], 
# 				[7, 0], 
# 				[7, 0]], 

# 				[[7, 7, 7], 
# 				[0, 0, 7]]	
# 				]

# L_tetronimo = [[[8, 0], 
# 				 [8, 0], 
# 				 [8, 8]], 

# 				 [[8, 8, 8], 
# 				 [8, 0, 0]], 

# 				 [[8, 8], 
# 				 [0, 8], 
# 				 [0, 8]], 

# 				 [[0, 0, 8], 
# 				 [8, 8, 8]]
# 				 ]


# tetronimos = [I_tetronimo, O_tetronimo, T_tetronimo, S_tetronimo, Z_tetronimo, J_tetronimo, L_tetronimo]


tetronimos = [
			[['I', 'I', 'I', 'I']], 

			[['O','O'],
			 ['O','O']], 

			[['T', 'T', 'T'], 
			[' ', 'T', ' ']], 

			[[' ', 'S', 'S'], 
			['S', 'S', ' ']], 

			[['Z', 'Z', ' '], 
			[' ', 'Z', 'Z']], 

			[['J', 'J', 'J'], 
			[' ', ' ', 'J']], 

			[['L', 'L', 'L'], 
			['L', ' ', ' ']]
]



class Tetris(object):
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Not Wumpus World')
		self.init_game()

	def init_game(self):
		width = 20
		height = 20 
		margin = 5 

		chosen_rand = rand(len(tetronimos))
		for i in range(len(tetronimos[chosen_rand])):
			for x in range(len(tetronimos[chosen_rand][i])):
				if tetronimos[chosen_rand][i][x] != ' ':
					pygame.draw.rect(DISPLAYSURF, BLUE, ((margin+width)*x+margin, (margin+height)*i+margin, width, height), 1)




	def run(self):
		while True:
			for event in pygame.event.get(): 
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				pygame.display.update()

#Goal 1:
#draw random block 


if __name__ == '__main__':
	App = Tetris()
	App.run()

