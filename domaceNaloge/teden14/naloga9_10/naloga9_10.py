import random
import sys, pygame

pygame.init()

size = width, height = 800, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Slalom v d-MOL-u")
black = 0, 0, 0

music = pygame.mixer.music.load("arcade.mp3")
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)
game_over_font = pygame.font.Font(None, 128)

# Sounds
jump_channel = pygame.mixer.Channel(1)
jump_sound = pygame.mixer.Sound("jump.mp3")
jump_sound.set_volume(0.4)
explosion_channel = pygame.mixer.Channel(2)
explosion_sound = pygame.mixer.Sound("explosion.mp3")
explosion_sound.set_volume(0.4)

kolesar = pygame.image.load("kolesar.png")

kolesar_rect = kolesar.get_rect()
kolesar_rect.bottom = 600
kolesar_rect.centerx = 400


ovire = []
znaki_mol = []
ovire_slike = ["bottle.png", "flowers.png", "grass.png", "mol.png", "scooter.png", "stones.png", "walker.png"]
ovire_counter = 0

lives = 3
points = 0
level = 0

game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    clock.tick(480)

    if game_over:
        continue

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
        ovire_counter = random.randint(30, 160 - 10 * level)
        slika = random.choice(ovire_slike)
        ovira = pygame.image.load(slika)
        ovira_rect = ovira.get_rect(top=0)
        ovira_rect.centerx = random.randint(0 + ovira_rect.width//2, width - ovira_rect.width//2)
        if slika == "mol.png":
            znaki_mol.append((ovira, ovira_rect))
        else:
            ovire.append((ovira, ovira_rect))

    # Premakni ovire
    for ovira, ovira_rect in ovire + znaki_mol:
        ovira_rect.y += 1 + level/10
    ovire = list(filter(lambda ovira: ovira[1].top <= height, ovire))
    znaki_mol = list(filter(lambda znak: znak[1].top <= height, znaki_mol))

    # -- Collision check --
    # Znak mol
    dotaknjen_znak = kolesar_rect.collideobjects(znaki_mol, key=lambda znak: znak[1])
    if dotaknjen_znak:
        znaki_mol.remove(dotaknjen_znak)
        points += 1
        jump_channel.play(jump_sound)
        novi_nivo = points // 5
        if novi_nivo <= 13:
            level = novi_nivo


    # Ovire
    dotaknjena_ovira = kolesar_rect.collideobjects(ovire, key=lambda ovira: ovira[1])
    if dotaknjena_ovira:
        ovire.remove(dotaknjena_ovira)
        lives -= 1
        explosion_channel.play(explosion_sound)

    # Nariši
    screen.fill(black)
    screen.blits(ovire, False)
    screen.blits(znaki_mol, False)
    screen.blit(kolesar, kolesar_rect)

    # Napiši text
    tocke_text = font.render(f"Tocke: {points}", False, (255, 255, 255))
    screen.blit(tocke_text, tocke_text.get_rect(centerx=width//6, top=10))
    nivo_text = font.render(f"Nivo: {level}", False, (255, 255, 255))
    screen.blit(nivo_text, nivo_text.get_rect(centerx=width//2, top=10))
    zivljenja_text = font.render(f"Zivljenja: {lives}", False, (255, 255, 255))
    screen.blit(zivljenja_text, zivljenja_text.get_rect(centerx=width*5//6, top=10))

    if lives == 0:
        game_over = True
        game_over_text = game_over_font.render("GAME OVER!", True, (255, 0, 0))
        screen.blit(game_over_text, game_over_text.get_rect(centerx=width // 2, centery=height // 2))
        pygame.mixer.music.stop()

    pygame.display.flip()

