def PP_Ex3():
    import pygame
    import time
    import random

    # Inicialización de Pygame
    pygame.init()

    # Definición de colores
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    # Dimensiones de la pantalla
    dis_width = 600
    dis_height = 400

    # Tamaño del bloque
    block_size = 20

    # Frecuencia de actualización del juego
    clock = pygame.time.Clock()

    # Fuente para el texto
    font_style = pygame.font.SysFont(None, 50)
    score_font = pygame.font.SysFont(None, 35)

    # Cargar las imágenes
    background = pygame.image.load("/home/cicles/AO/background.jpg")
    game_over_background = pygame.image.load("/home/cicles/AO/final.jpg")
    apple_image = pygame.image.load("/home/cicles/AO/apple.png")
    snake_head_img = pygame.image.load("/home/cicles/AO/snake_head.png")
    snake_body_img = pygame.image.load("/home/cicles/AO/snake_body.jpg")

    # Escalar las imágenes al tamaño de la pantalla y bloques
    background = pygame.transform.scale(background, (dis_width, dis_height))
    game_over_background = pygame.transform.scale(game_over_background, (dis_width, dis_height))
    apple_image = pygame.transform.scale(apple_image, (block_size, block_size))
    snake_head_img = pygame.transform.scale(snake_head_img, (block_size, block_size))
    snake_body_img = pygame.transform.scale(snake_body_img, (block_size, block_size))

    def our_snake(block_size, snake_list):
        for i, pos in enumerate(snake_list):
            if i == len(snake_list) - 1:
                dis.blit(snake_head_img, (pos[0], pos[1]))
            else:
                dis.blit(snake_body_img, (pos[0], pos[1]))

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])

    def show_score(score):
        value = score_font.render("Score: " + str(score), True, black)
        dis.blit(value, [0, 0])

    def gameLoop():
        game_over = False
        game_close = False

        # Coordenadas iniciales de la serpiente
        x1 = dis_width / 2
        y1 = dis_height / 2

        # Cambio en las coordenadas de la serpiente
        x1_change = 0
        y1_change = 0

        # Longitud inicial de la serpiente
        snake_list = []
        length_of_snake = 1

        # Puntuación inicial
        score = 0

        # Posición aleatoria de la manzana
        foodx = round(random.randrange(0, dis_width - block_size) / 20.0) * 20.0
        foody = round(random.randrange(0, dis_height - block_size) / 20.0) * 20.0

        while not game_over:

            while game_close:
                dis.blit(game_over_background, (0, 0))
                message("Perdiste! Presiona Q para salir o C para jugar de nuevo", red)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -block_size
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = block_size
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -block_size
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = block_size
                        x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.blit(background, (0, 0))
            dis.blit(apple_image, (foodx, foody))
            snake_head = [x1, y1]
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            our_snake(block_size, snake_list)
            show_score(score)
            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - block_size) / 20.0) * 20.0
                foody = round(random.randrange(0, dis_height - block_size) / 20.0) * 20.0
                length_of_snake += 1
                score += 1

            clock.tick(10)

        pygame.quit()
        quit()

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game')
    
    gameLoop()
