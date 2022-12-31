import pygame, sys, random

#player + collision + score
class Player:
	def __init__(self, display_surface, bar_list):
		global player_x, player_y

		self.display_surface = display_surface
		self.bar_list = bar_list

		player_x = 240
		player_y = 400

		self.x = player_x
		self.y = player_y
 
		self.pressed = False
		self.move_right = True    

		self.font = pygame.font.Font("grafik/GROBOLD.ttf",25)
		
		self.image = pygame.Surface((40, 40))
		self.image.fill((19, 212, 170))
		self.rect = self.image.get_rect(topleft = (self.x, self.y))
	
	def draw_player(self):
		self.rect = self.image.get_rect(topleft = (self.x, self.y))
		self.display_surface.blit(self.image,self.rect)

	def input(self):
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_SPACE] and self.pressed == False:
			self.pressed = True
			if self.move_right == True:
				self.move_right = False

			else:
				self.move_right = True

		elif not keys_pressed[pygame.K_SPACE]:
			self.pressed = False

	def move(self):
		if self.move_right == True and self.x <= 510:
			self.x += 2

		elif self.move_right == False and self.x >= 0:
			self.x -= 2

	def collision(self):
		global dead
		for bar in self.bar_list:
			if self.rect.colliderect(bar.rect) and not bar.black_x <= self.x <= bar.black_x + 160:
				dead = True

	def score(self):
		global score1
		for bar in self.bar_list:
			if bar.y == 441:
				score1 += 1

		text_surf = self.font.render(f"SCORE= {score1}",True,(255,255,255))
		text_rect = text_surf.get_rect(topleft = (10, 10))
		display_surface.blit(text_surf, text_rect)

	def update(self):
		global player_x, player_y
		player_x = self.x
		player_y = self.y

		self.collision()
		self.draw_player()
		self.input()
		self.move()
		self.score()
		
#bar
class Bar:
	def __init__(self, display_surface, bar_list):
		self.display_surface = display_surface
		self.bar_list = bar_list

		self.x = 0
		self.y = -60

		self.black_x = random.randrange(0, 350)
		self.black_y = -60

		self.image = pygame.Surface((550, 50))
		self.image.fill((255,255,255))
		self.rect = self.image.get_rect(topleft = (self.x, self.y))

	def draw_bar(self):
		self.rect = self.image.get_rect(topleft = (self.x, self.y))
		self.display_surface.blit(self.image,self.rect)
		
		pygame.draw.rect(self.display_surface, (0, 0, 0), [self.black_x, self.black_y, 200, 50])		

	def move(self):
		self.y += 1
		self.black_y += 1

	def update(self):
		self.draw_bar()
		self.move()

#end
class End:
	def __init__(self, display_surface, bar_list):
		self.display_surface = display_surface
		self.bar_list = bar_list

		self.hig_score_1 = 0
		self.end_loop = False

	def hig_score(self):
		global score1
		font = pygame.font.Font("grafik/GROBOLD.ttf",25)
		font1 = pygame.font.Font("grafik/GROBOLD.ttf",75)

		if self.hig_score_1 < score1:
			self.hig_score_1 = score1		
		
		text_surf = font.render(f"HIGH SCORE = {self.hig_score_1}",True,(255,255,255))
		text_rect = text_surf.get_rect(center = (275, 250))
		self.display_surface.blit(text_surf, text_rect)

		text_surf = font1.render(f"SCORE = {score1}",True,(255,255,255))
		text_rect = text_surf.get_rect(center = (275, 199))
		self.display_surface.blit(text_surf, text_rect)

	def restart(self):
		global dead, score1, player_x, player_y
		dead = False
		score1 = 0
		player_x = 240
		player_y = 400
		self.bar_list.clear()
		self.end_loop = False

	def restart_button(self):
		top_rect = pygame.Rect(140, 347, 269, 105)

		pos = pygame.mouse.get_pos()
		if top_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0]:
				self.restart()

		font = pygame.font.Font("grafik/GROBOLD.ttf",75)
		text_surf = font.render("restart",True,(255,255,255))
		text_rect = text_surf.get_rect(center = (275, 400))
		display_surface.blit(text_surf,(text_rect))
		pygame.draw.rect(self.display_surface,(255,255,255),text_rect.inflate(30,30), width = 10, border_radius = 5)

	def home(self):
		global dead, start
		top_rect = pygame.Rect(140, 472, 269, 105)

		pos = pygame.mouse.get_pos()
		if top_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0]:
				self.end_loop = False
				dead = False
				start = True

		font = pygame.font.Font("grafik/GROBOLD.ttf",75)
		text_surf = font.render("home",True,(255,255,255))
		text_rect = text_surf.get_rect(center = (275, 525))
		display_surface.blit(text_surf,(text_rect))
		pygame.draw.rect(self.display_surface,(255,255,255),text_rect.inflate(30,30), width = 10, border_radius = 5)

	def update(self):
		self.end_loop = True
		while self.end_loop:
			self.display_surface.fill((0,0,0))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.home()
			self.hig_score()
			self.restart_button()
			pygame.display.update()

#start
class Start_class:
	def __init__(self, display_surface):
		self.display_surface = display_surface
	#212 80/ 242 110 / 121 55

	def play_button(self):
		global start
		top_rect = pygame.Rect(154, 345, 242, 110)

		pos = pygame.mouse.get_pos()
		if top_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0]:
				self.end_loop = True
				start = False

		font = pygame.font.Font("grafik/GROBOLD.ttf",75)
		text_surf = font.render("PLAY",True,(255,255,255))
		text_rect = text_surf.get_rect(center = (275, 400))
		display_surface.blit(text_surf,(text_rect))
		pygame.draw.rect(self.display_surface,(255,255,255),text_rect.inflate(30,30), width = 10, border_radius = 5)

	def update(self):
		self.end_loop = False

		while self.end_loop == False:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.display_surface.fill((0,0,0))
			self.play_button()
			pygame.display.update()

#pause
class Pause:
	def __init__(self, display_surface):
		self.display_surface = display_surface

	def pause(self):
		global pause1
		top_rect = pygame.Rect(523, 10, 18, 26)

		pos = pygame.mouse.get_pos()
		if top_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0]:
				pause1 = True

		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_p]:
			pause1 = True

		font = pygame.font.Font("grafik/GROBOLD.ttf",25)
		text_surf = font.render("II",True,(255,255,255))
		text_rect = text_surf.get_rect(topleft = (523, 10))
		display_surface.blit(text_surf,(text_rect))

	def play(self):
		global pause1

		self.display_surface.fill((0,0,0))
		font = pygame.font.Font("grafik/GROBOLD.ttf",75)
		text_surf = font.render("PLAY",True,(255,255,255))
		text_rect = text_surf.get_rect(center = (275, 400))
		display_surface.blit(text_surf,(text_rect))
		pygame.draw.rect(self.display_surface,(255,255,255),text_rect.inflate(30,30), width = 10, border_radius = 5)
		pygame.display.update()

		loop_pause = True
		while loop_pause:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.K_p:
					pause1 = False
					loop_pause = False


			top_rect = pygame.Rect(154, 345, 242, 110)

			pos = pygame.mouse.get_pos()
			if top_rect.collidepoint(pos):
				if pygame.mouse.get_pressed()[0]:
					pause1 = False
					loop_pause = False
					pygame.time.set_timer(timer_bar, 2500)

	def update(self):
		global pause

		if pause1 == True:
			self.play()

		else:
			self.pause()

#particles player
class Particles:
	def __init__(self, display_surface, Particles_list):
		global player_x, player_y
		self.pos_x = player_x + 20
		self.pos_y = player_y + 20

		self.display_surface = display_surface
		self.particles_list = Particles_list

		self.radius = 15

	def move(self):
		self.pos_y += 1
		self.radius -= 0.05

		pygame.draw.circle(self.display_surface, ((19, 212, 170)), [self.pos_x, self.pos_y], int(self.radius))

	def delete(self):
		if self.radius <= 0:
			self.particles_list.remove(self)

	def update(self):
		self.move()
		self.delete()


pygame.init()
display_surface = pygame.display.set_mode((550, 800))
pygame.display.set_caption("EVADE THE BAR")

#bar list
bar_list = []
bar_list.append(Bar(display_surface, bar_list))

#make class
end = End(display_surface, bar_list)
player = Player(display_surface, bar_list)
start_class = Start_class(display_surface)
pause = Pause(display_surface)

#particels list
Particles_list = []
Particles_list.append(Particles(display_surface, Particles_list))

#global variable
dead = False
start = True
pause1 = False
score1 = 0

#timer_bar
timer_bar = pygame.event.custom_type()
pygame.time.set_timer(timer_bar, 2500)

#timer_particles
timer_particles = pygame.event.custom_type()
pygame.time.set_timer(timer_particles, 200)

#fps limit
clock = pygame.time.Clock()

while True:
	if start == True:
		start_class.update()
		pygame.time.set_timer(timer_bar, 2500)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == timer_bar:
			bar_list.append(Bar(display_surface, bar_list))
		if event.type == timer_particles:
			Particles_list.append(Particles(display_surface, Particles_list))

	display_surface.fill((0,0,0))

	if dead == True:
		end.update()
		pygame.time.set_timer(timer_bar, 2500)
		Particles_list = []
		bar_list.append(Bar(display_surface, bar_list))

	for item in bar_list:
		item.update()
		if item.y > 900:
			bar_list.remove(item)

	for item in Particles_list:
		item.update()

	pygame.draw.rect(display_surface, (0,0,0), (0, 0, 550, 50))
	pause.update()
	player.update()
	clock.tick(167)
	pygame.display.update()