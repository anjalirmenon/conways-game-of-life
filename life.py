import random
import pygame,sys

wt = 600
ht = 600
black=(0,0,0)
white=(255,255,255)

screen = pygame.display.set_mode((wt,ht))
screen.fill(black)
#for i in range((50*50)/2):
#	x = random.randint(0,50)
#	y = random.randint(0,50)
#	pygame.draw.rect(screen,(255,255,255),(x*10,y*10,10,10))
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	for i in range((50*50)/2):
		x = random.randint(0,50)
		y = random.randint(0,50)
	pygame.draw.rect(screen,(255,255,255),(x*10,y*10,10,10))
	pygame.display.flip()	
	
