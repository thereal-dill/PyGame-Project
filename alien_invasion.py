import sys
import pygame


from settings import Settings
from character import Character

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.character = Character(self)
        pygame.display.set_caption("Alien Invasion")
        

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.character.update()
            self._update_screen()
            self.clock.tick(60)  # Limit the frame rate to 60 FPS


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.character.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.character.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.character.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.character.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.character.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()