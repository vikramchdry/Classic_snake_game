import pygame
from utils import Config
from Snake import Snake
from Apple import Apple
#display_width = 400
#display_height = 400
#display = pygame.display.set_mode((display_width,display_height))


class Game:

	def __init__(self,display):

		self.display = display
		self.score = 0


	def game_loop(self):


		clock = pygame.time.Clock()
		snake = Snake(self.display)
		apple = Apple(self.display)
		x_movement = 0
		y_movement = 0
		self.score = 0



		while True:



			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				#print(event)
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						x_movement = -Config['snake']['speed']
						y_movement = 0
					elif event.key == pygame.K_RIGHT:
						x_movement = Config['snake']['speed']
						y_movement = 0
					elif event.key == pygame.K_DOWN:
						y_movement = Config['snake']['speed']
						x_movement = 0
					elif event.key == pygame.K_UP:
						y_movement = -Config['snake']['speed']
						x_movement = 0

				"""if event.type == pygame.KEYUP:
					if event.key == pygame.K_UP:
						y_movement = 0
						x_movement = 0
					elif event.key == pygame.K_DOWN:
						y_movement = 0
						x_movement = 0
					elif event.key == pygame.K_RIGHT:
						x_movement =0
						y_movement = 0
					elif event.key == pygame.K_LEFT:
						x_movement = 0
						y_movement = 0
						"""




			self.display.fill(Config['colors']['green'])
			pygame.draw.rect(self.display, Config['colors']['black'],
				[Config['game']['bumper_size'],
				Config['game']['bumper_size'],
				Config['game']['height'] - Config['game']['bumper_size']*2 ,Config['game']['width'] - Config['game']['bumper_size'] *3])
			
			apple_rect = apple.draw()
			snake.move(x_movement,y_movement)
			snake_rect = snake.draw()
			snake.draw_body()

			#collision

			bumper_x = Config['game']['width'] - Config['game']['bumper_size']
			bumper_y = Config['game']['height'] - Config['game']['bumper_size']

			if (snake.x_pos <Config['game']['bumper_size'] or snake.y_pos <Config['game']['bumper_size'] or 
				snake.x_pos + Config['snake']['width'] > bumper_x or snake.y_pos + Config['snake']['height'] > bumper_y ): self.game_loop()



			if apple_rect.colliderect(snake_rect):
				apple.appleDisplay()
				self.score += 1
				snake.eat()


			if len(snake.body) >= 1:
				for cell in snake.body:
					if snake.x_pos == cell[0] and snake.y_pos == cell[1]:self.game_loop()


			pygame.font.init()
			font = pygame.font.Font('./Now-Regular.otf', 28)
			score_text = 'Score: {}'.format(self.score)
			score = font.render(score_text, True, Config['colors']['white'])
			title = font.render('snake - Vikram', True, Config['colors']['white'])
			title_rect = title.get_rect(center=(Config['game']['width'] / 2,Config['game']['bumper_size'] / 2))
			score_rect = score.get_rect(center=(500/2,Config['game']['height'] - Config['game']['bumper_size'] / 2))
			self.display.blit(score, score_rect)
            #self.display.blit(title, title_rect)
			



			pygame.display.update()
			clock.tick(Config['game']['fps'])

		

		




			

