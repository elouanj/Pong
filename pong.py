from pygame import *
from pygame.locals import *

pointv=0
pointp=0
init()

fenetre = display.set_mode((640, 480))
rectangle = Rect(40,190,12,100)
rectangle2 = Rect(595,190,12,100)
rectangle3 = Rect(310,230,20,20)
but = Rect(0,130,10,220)
but2 = Rect(628,130,10,220)
green = (0,255,0)
white = (255,255,255)
purple = (150,0,255)
vitessev = 2
vitesseh = 2
key.set_repeat(1,5)

font=font.Font(None, 50)

image = image.load("fond.jpg")
image = image.convert()

continu2=False
continu = True
while (continu):
	fenetre.fill(0)
	fenetre.blit(image, (0, 0))
	draw.rect(fenetre,green,rectangle)
	draw.rect(fenetre,purple,rectangle2)
	draw.rect(fenetre,white,rectangle3)
	draw.rect(fenetre,white,but)
	draw.rect(fenetre,white,but2)
	fenetre.blit(font.render(str(pointp),1,purple), (610, 10))
	fenetre.blit(font.render(str(pointv),1,green), (10, 10))
	if pointp == 5:
		fenetre.blit(font.render("Le violet gagne !",1,purple), (190, 240))
		continu = False
		continu2=True
	if pointv == 5:
		fenetre.blit(font.render("Le vert gagne !",1,green), (200, 240))
		continu = False
		continu2=True
	display.flip()
	for p_event in event.get():
		if p_event.type == QUIT:
			continu = False
		if p_event.type == KEYDOWN:
			if p_event.key == K_UP:
				rectangle2.y -= 5
			if p_event.key == K_DOWN:
				rectangle2.y += 5
			if p_event.key == K_z:
				rectangle.y -= 5
			if p_event.key == K_s:
				rectangle.y += 5
	
	rectangle3.x += vitesseh
	rectangle3.y += vitessev
	if rectangle3.x >= 620 or rectangle3.x <= 0 or rectangle3.x <= rectangle.x+12 and rectangle3.y+20 > rectangle.y and rectangle3.y < rectangle.y+100 or rectangle3.x+20 >= rectangle2.x and rectangle3.y+20 > rectangle2.y and rectangle3.y < rectangle2.y+100:
		vitesseh = -vitesseh
	if rectangle3.y >= 460 or rectangle3.y <= 0:
		vitessev = -vitessev
	if rectangle3.x <= 0 and rectangle3.y < 350 and rectangle3.y > 130:
		pointp += 1
	if rectangle3.x >= 620 and rectangle3.y < 350 and rectangle3.y > 130:
		pointv += 1
		
while (continu2):
	for p_event in event.get():
		if p_event.type == QUIT:
			continu2 = False
