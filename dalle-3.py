import streamlit as st
import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 600, 400
FPS = 60

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Paramètres de la balle
ball_speed = [3, 3]
ball_radius = 10

# Paramètres de la raquette
paddle_width, paddle_height = 100, 10
paddle_speed = 5

# Configuration du jeu
def casse_briques():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Casse-Briques")

    ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, ball_radius, ball_radius)
    paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - 30, paddle_width, paddle_height)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Mouvement de la raquette
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.move_ip(-paddle_speed, 0)
        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.move_ip(paddle_speed, 0)

        # Mouvement de la balle
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # Rebonds
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed[0] = -ball_speed[0]
        if ball.top <= 0 or ball.colliderect(paddle):
            ball_speed[1] = -ball_speed[1]
        if ball.bottom >= HEIGHT:
            running = False  # La balle est perdue

        # Dessiner les éléments
        screen.fill(BLACK)
        pygame.draw.ellipse(screen, BLUE, ball)
        pygame.draw.rect(screen, WHITE, paddle)
        pygame.display.flip()

        clock.tick(FPS)

# Interface Streamlit
st.title("Jeu Casse-Briques")
if st.button("Lancer le jeu"):
    casse_briques()
