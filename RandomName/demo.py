import pygame


class MyClass:
    def __init__(self):
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound('music/bcg.wav')

    def play_sound(self):
        self.sound.play()


player = MyClass()
player.play_sound()
