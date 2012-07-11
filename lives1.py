import random
import pygame,sys
wt = 500
ht = 500
black=(0,0,0)
white=(255,255,255)
livcel = set()
dedcel = set()
screen = pygame.display.set_mode((wt,ht))
screen.fill(white)
def addcel(x, y):
	livcel.add((x, y))
	for x1, y1 in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,-1),(0,1),(1,0),(1,1)):
		if not (x+x1,x+y1) in livcel:	
			dedcel.add((x+x1,y+y1))
	pygame.draw.rect(screen,(0,0,0),(x*10,y*10,10,10))
for i in range((50*50)/2):
	x = random.randint(0,50)
	y = random.randint(0,50)
	addcel(x,y)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		else:
			if pygame.mouse.get_pressed()[0]:
				px, py = pygame.mouse.get_pos()
				nx, ny = px/c, py/c
				if (nx, ny) in livcel:
					dedcel.add((nx, ny))
					livcel.remove((nx, ny))
				else:	
					addcel(nx, ny)
					dedcel.discard((nx, ny))
	
		pygame.display.flip()
		for (x,y) in tuple(livcel):
			n = sum(((x+x1, y+y1) in livcel for (x1,y1) in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))))
			#if n not in (2, 3):
			if n > 3 or n < 2:
				livcel.remove((x, y))
				dedcel.add((x, y))
				pygame.draw.rect(screen,(255,255,255), (x*10, y*10, 10, 10))	
		for (x,y) in tuple(dedcel):
			n = sum(((x+x1,y+y1) in livcel for (x1,y1) in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))))
			if n == 3:
				addcel(x,y)
				dedcel.remove((x,y))
				livcel.add((x,y))	
		celset = ()
		lencelset = len(celset)
		i=0
		while i < lencelset:
			(x,y) = celset[i]
			if not any(((x+x1, y+y1) in livcel for (x1, y1) in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)))):
				dedcel.remove((x+x1, y+y1)) 
			i = i + 1
