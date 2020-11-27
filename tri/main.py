import random, time, os
import pygame
from pygame import mixer



def tri2(liste):
	for i in range(len(liste)):
		index=0
		for l in range(len(liste)):
			if liste[i]<liste[l]:
				t=liste[l]
				liste[l]=liste[i]
				liste[i]=t
		print(liste)
	return liste





def tri(liste):
	for i in range(len(liste)-1):
		if liste[i]>liste[i+1]:
			t=liste[i]
			liste[i]=liste[i+1]
			liste[i+1]=t
	return liste, t



def tri3(liste, etape):
	...




def general_sort(liste):
	cp=0
	t=time.time()
	while sorted(liste)!=liste:
		liste=tri(liste)
		#liste=tri2(liste)
		cp+=1
	print(time.time()-t)
	print(cp)







def get_liste(long):
	l=[]
	'''
	for i in range(long):
		t=random.randint(100,1000)
		if t not in l:
			l.append(t)
		else:
			i-=1
	return l
	'''
	"""
	t=[i for i in range(long)]
	random.shuffle(t)
	return(t)"""
	return [random.randint(100,1000) for i in range (long)]


def get_graph(liste):
	graphique=[['|' for i in range(l)] for l in range(len(liste))]

	print(graphique)
	return graphique



def is_sort(liste):
	if sorted(liste)==liste:
		return True
	else:
		return False





pygame.mixer.init() 
pygame.init()



screen= pygame.display.set_mode((1800,1000))
pygame.display.set_caption('tri')
run=True


fond=pygame.font.Font('freesansbold.ttf', 100)
fond_pti=pygame.font.Font('freesansbold.ttf', 17)


mixer.music.load('son.ogg')


liste=get_liste(1300)
comp=0



while run:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	screen.fill((0, 0, 0))

	if not is_sort(liste):
		mixer.music.play()
		comp+=len(liste)
		liste, lst=tri(liste)
		#print(liste)

	for i in range(len(liste)):
		pygame.draw.line(screen, (255,0,0), (i+50, 1000), (i+50, 1000-liste[i]))

	pygame.draw.line(screen, (255,0,0), (1380, 1000), (1380, 1000-lst))

	blt_comp= fond.render(str(comp),True, (255,255,255))
	screen.blit(blt_comp,(1400,500))

	#len_liste= fond.render(str(len(liste)),True, (255,0,0))
	#screen.blit(len_liste,(1400,100))


	sbl= fond_pti.render(str(liste[0: 50]),True, (255,255,255))
	screen.blit(sbl,(0,0))

	pygame.display.update()

#liste=get_liste(3000)


#sort(liste)








