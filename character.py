import pygame

class Character:
    """A class to represent a character in the game."""

    def __init__(self, ai_game):
        """Initialize the character and set it's starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the character png and it's rect.
        self.image = pygame.image.load('Assets/idle.gif')
        self.rect = self.image.get_rect()

        # Start each new character at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the character's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag; start with a character that's not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the character's position based on movement flags."""
        # Update the character's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.character_speed  # Move character right
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.character_speed  # Move character left

        # Update the rect object from the stored x value.
        self.rect.x = self.x

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)