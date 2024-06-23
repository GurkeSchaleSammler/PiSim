import pygame
from organism import Organism
from ecosystem import Ecosystem

# Initialisiere Pygame
pygame.init()

# Setze die Dimensionen des Fensters
window = pygame.display.set_mode((1000, 1000))

# Farben definieren
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def draw_organism(window: pygame.Surface, organism: Organism) -> None:
    color = GREEN if organism.name == 'Kaninchen' else RED
    pygame.draw.circle(window, color, (organism.x, organism.y), 10)
    
    # Lebensleiste
    health_bar_width = 20  # Breite der Lebensleiste, gleich der doppelten Breite des Kreises
    health_bar_height = 5   # Höhe der Lebensleiste
    current_health_width = health_bar_width 
    
    # Zeichnen der Lebensleiste (Hintergrund in Rot)
    pygame.draw.rect(
        window, RED,
        (organism.x - health_bar_width // 2, organism.y - 15,
         health_bar_width, health_bar_height)
    )
    
    # Zeichnen der aktuellen Energie (in Grün)
    pygame.draw.rect(
        window, GREEN,
        (organism.x - health_bar_width // 2, organism.y - 15,
         current_health_width, health_bar_height)
    )
    
def main():
    clock = pygame.time.Clock()
    ecosystem = Ecosystem()
    ecosystem.add_organism(Organism('Kaninchen', 400, 300))
    ecosystem.add_organism(Organism('Fuchs', 200, 150))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(WHITE)

        for organism in ecosystem.organisms[:]:
            if not organism.live_one_day():
                ecosystem.organisms.remove(organism)
            else:
                draw_organism(window, organism)

        pygame.display.flip()
        clock.tick(300)  # Erhöhte Tick-Rate für schnellere Simulation

    pygame.quit()


if __name__ == '__main__':
    main()
