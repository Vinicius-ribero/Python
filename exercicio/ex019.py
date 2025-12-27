import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo MP3 (certifique-se de que o arquivo esteja na mesma pasta)
pygame.mixer.music.load('seu_arquivo.mp3')

# Reproduz o áudio
pygame.mixer.music.play()

# Mantém o programa rodando enquanto a música toca
input('Tocando música... Pressione ENTER para parar.')