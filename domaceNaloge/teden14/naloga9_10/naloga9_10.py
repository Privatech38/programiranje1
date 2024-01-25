import random
import sys, pygame

pygame.init()

size = width, height = 800, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Slalom v d-MOL-u")
black = 0, 0, 0

music = pygame.mixer.music.load("arcade.mp3")
pygame.mixer.music.play(-1)

kolesar = pygame.image.load("kolesar.png")

kolesar_rect = kolesar.get_rect()
kolesar_rect.bottom = 600
kolesar_rect.centerx = 400

clock = pygame.time.Clock()

ovire = []
ovire_slike = ["bottle.png", "flowers.png", "grass.png", "mol.png", "scooter.png", "stones.png", "walker.png"]
ovire_counter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    clock.tick(480)

    # Premik kolesarja
    keys = pygame.key.get_pressed()

    kolesar_rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
    if kolesar_rect.centerx < 20:
        kolesar_rect.centerx = 20
    if kolesar_rect.centerx > width - 20:
        kolesar_rect.centerx = width - 20

    # -- Ovire --
    # Usvtari oviro
    ovire_counter -= 1
    if ovire_counter <= 0:
        ovire_counter = random.randint(30, 150)
        ovira = pygame.image.load(random.choice(ovire_slike))
        ovira_rect = ovira.get_rect()
        ovira_rect.top = 0
        ovira_rect.centerx = random.randint(0 + ovira_rect.width, width - ovira_rect.width)
        ovire.append((ovira, ovira_rect))

    # Premakni ovire
    for ovira, ovira_rect in ovire:
        ovira_rect.y += 1
    ovire = list(filter(lambda ovira: ovira[1].top <= height, ovire))


    # Collision check

    # Nariši
    screen.fill(black)
    screen.blit(kolesar, kolesar_rect)
    screen.blits(ovire, False)
    pygame.display.flip()