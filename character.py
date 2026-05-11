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

        # Movement flag; start with a character that's not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the character's position based on movement flags."""
        if self.moving_right:
            self.rect.x += 2  # Move character right
        if self.moving_left:
            self.rect.x -= 2  # Move character left

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)