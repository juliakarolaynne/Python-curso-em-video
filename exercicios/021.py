import pygame

# Inicializa o mixer de áudio do pygame
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load('arquivo.mp3')

# Reproduz o arquivo MP3
pygame.mixer.music.play()

# Mantém o programa em execução enquanto a música está sendo reproduzida
while pygame.mixer.music.get_busy():
    continue
