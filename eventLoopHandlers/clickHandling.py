import pygame
from constants.game_constants import *
def handleShoppingPageClick(autominers_collection,clicker):
    """обработка клика на страничке магазина"""
    mouse_position = pygame.mouse.get_pos()
    if abs(app_height // 2 - 50 - mouse_position[1]) and abs(app_width // 2 - mouse_position[0]) < 190:
        if clicker.score >= 50:
            clicker.increaseOneClickCost(1)
            clicker.increaseScore(-50)

    if abs(app_height // 2 - mouse_position[1]) < 80:
        minerIndex = mouse_position[0] // (app_width // len(autominers_collection))
        miner = autominers_collection[minerIndex]
        if clicker.score >= miner.cost:
            clicker.increaseAutomineSpeed(miner.speed)
            clicker.increaseScore(-miner.cost)

    pygame.display.update()