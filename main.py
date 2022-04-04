from eventLoopHandlers.clickHandling import handleShoppingPageClick
from eventLoopHandlers.drawingUtils import *
from constants.game_constants import *
from classes.autominer import Autominer
from classes.clicker import Clicker
import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((app_width, app_height))

pygame.display.set_caption("super cool clicker")

"""event loop"""

def main_loop():
    clicker = Clicker()
    is_shopping = False
    game_running = True
    clock = pygame.time.Clock()
    while game_running:
        clicker.automine()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                clicker.click()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                is_shopping = not is_shopping
            if event.type == pygame.MOUSEBUTTONDOWN and is_shopping:
                handleShoppingPageClick(autominers_collection, clicker)
        gameDisplay.fill(white)
        if not is_shopping:
            gameDisplay.blit(pygame.transform.scale(pygame.image.load("images/img.png"),
                                                    (app_width, app_height + 110)), (0, -110))
            printTextCentred(gameDisplay, str(clicker.score), black, 20, app_width // 2 - 120)
        else:
            drawShoppingPage(gameDisplay, clicker)
        pygame.display.update()
        clock.tick(60)


main_loop()
pygame.quit()
quit()
