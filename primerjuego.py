import pygame
import sys
import time
import random

ancho = 800
alto = 600
jugador_size = 50
enemigo_size = 50
balas_size = 10
color_azul = (0, 0, 255)
color_rojo = (255, 0, 0)
color_verde = (0, 255, 0)
color_negro = (0, 0, 0)
jugador_pos = [ancho / 2, alto - jugador_size * 2]
bala_pos = [jugador_pos[0], jugador_pos[1]]
#enemigo_pos = [random.randint(0, ancho - enemigo_size), jugador_pos[1] - jugador_size*10]
enemigo_pos = [random.randint(0, ancho - enemigo_size), random.randint(0, alto / 2 - enemigo_size)]
enemigo_vida = 3
ventana = pygame.display.set_mode((ancho, alto))
timer = pygame.time.Clock()
#pygame.init()
def disparo(enemigo_pos, bala_pos):
	jx = jugador_pos[0]
	jy = jugador_pos[1]
	bx = bala_pos[0]
	by = bala_pos[1]
	ex = enemigo_pos[0]
	ey = enemigo_pos[1]
	if (bx >= ex and bx <(ex + enemigo_size)) or (ex >= bx and ex < (bx + balas_size)):
		if (by >= ey and by <(ey + enemigo_size)) or (ey >= by and ey < (by + balas_size)):
			return True
		return False
while True:
	for event in pygame.event.get():
		#print(event)
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			x = jugador_pos[0]
			y = jugador_pos[1]
			if event.key == pygame.K_RIGHT:
				x += jugador_size
			if event.key == pygame.K_LEFT:
				x -= jugador_size
			if event.key == pygame.K_DOWN:
				y += jugador_size
			if event.key == pygame.K_UP:
				y -= jugador_size

			jugador_pos[0] = x
			jugador_pos[1] = y
			if jugador_pos[0] < 0:
				jugador_pos[0] = ancho
			elif jugador_pos[0] == ancho:
				jugador_pos[0] = 0
			if jugador_pos[1] < 0:
				jugador_pos[1] = alto
			elif jugador_pos[1] == alto:
				jugador_pos[1] = 0


	if bala_pos[1] >= 0 and bala_pos[1] < alto:
		if disparo(enemigo_pos, bala_pos):
			print("disparo")
			enemigo_vida -= 1
			print(f"vida: {enemigo_vida}")
		bala_pos[1] -= 5
	else:
		bala_pos[0] = jugador_pos[0] + 22.5
		bala_pos[1] = jugador_pos[1] + 22.5

	#if bala_pos[0] == enemigo_pos[0]:
	#	if bala_pos[1] == enemigo_pos[1]:

	if enemigo_vida == 0:
		enemigo_pos[0] = random.randint(0, ancho - enemigo_size)
		enemigo_vida = 3
	#if enemigo_pos[1] >= 0 and enemigo_pos[1] < alto:
	#	enemigo_pos[1] += 10
	#else:
	#	enemigo_pos[0] = random.randint(0, ancho - enemigo_size)
	#	enemigo_pos[1] = jugador_pos[1] - jugador_size*10

	ventana.fill(color_negro)
			#pygame.draw.rect()
	pygame.draw.rect(ventana, color_rojo, (bala_pos[0], bala_pos[1], balas_size, balas_size))
	pygame.draw.rect(ventana, color_azul, (jugador_pos[0], jugador_pos[1], jugador_size, jugador_size))
	pygame.draw.rect(ventana, color_verde, (enemigo_pos[0], enemigo_pos[1], enemigo_size, enemigo_size))
	timer.tick(30)
	pygame.display.update()