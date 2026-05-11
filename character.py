import pygame

class Character:
    """A class to represent a character in the game."""

    def __init__(self, ai_game):
        """Initialize the character and set it's starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the character png and it's rect.
        self.image = pygame.image.load('Assets/idle.gif')
        self.rect = self.image.get_rect()

        # Start each new character at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)