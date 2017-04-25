import pygame, sys
from pygame.locals import * 

# pygame.init()
DISPLAYSURF = pygame.display.set_mode((1000,1000))
# pygame.display.set_caption('Not Wumpus World')

# width = 20
# height = 20 
# margin = 5 


# for column in range(0, 10):
# 	#(screen, color, [x, y, width, height], line_thickness)
# 	pygame.draw.rect(DISPLAYSURF, (0,0,255), 
# 		((margin+width)*column+margin,(margin+height),width,height), 1)

class Tetris(object):
	def __init__(self):
		pygame.init()
		DISPLAYSURF = pygame.display.set_mode((1000,1000))
		pygame.display.set_caption('Not Wumpus World')
		self.init_game()

	def init_game(self):
		width = 20
		height = 20 
		margin = 5 


		for column in range(0, 10):
			#(screen, color, [x, y, width, height], line_thickness)
			pygame.draw.rect(DISPLAYSURF, (0,0,255), 
				((margin+width)*column+margin,(margin+height),width,height), 1)

	def run(self):
		while True:
			for event in pygame.event.get(): 
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				pygame.display.update()


# while True:
# 	for event in pygame.event.get(): 
# 		if event.type == QUIT:
# 			pygame.quit()
# 			sys.exit()
# 		pygame.display.update()

if __name__ == '__main__':
	App = Tetris()
	App.run()

