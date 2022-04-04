import pygame
from constants.game_constants import *
from classes.autominer import Autominer
autominers_collection = [Autominer(1, 25, "common autominer", randomCollor()),
                         Autominer(5, 50, "cooler autominer", randomCollor()),
                         Autominer(15, 100, "pretty good autominer", randomCollor()),
                         Autominer(25, 250, "really great autominer", randomCollor()),
                         Autominer(50, 350, "extremely good autominer", randomCollor())]


def printTextCentred(display, text, color, font_size, pos_x=app_width // 2, pos_y=app_height // 2):
    """отрисовка текста относительно центральной точки"""
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(text, True, color, white)
    text_rect = text.get_rect()
    text_rect.center = (pos_x, pos_y)
    display.blit(text, text_rect)


def printText(display, text, color, font_size, pos_x, pos_y):
    '''отрисовка текста'''
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(text, True, color, white)
    text_rect = text.get_rect()
    text_rect.x = pos_x
    text_rect.y = pos_y
    display.blit(text, text_rect)


def drawRectangle(display, color, pos_x, pos_y, width, height):
    pygame.draw.rect(display, color, (pos_x, pos_y, width, height))


def drawShoppingPage(display, clicker):
    display.blit(pygame.image.load("images/morshuReversed.png"), (0, 0))
    display.blit(pygame.image.load("images/morshuReversed.png"), (0, app_height - 300))
    display.blit(pygame.image.load("images/morshu.png"), (app_width - 300, 0))
    display.blit(pygame.image.load("images/morshu.png"), (app_width - 300, app_height - 300))
    display.blit(pygame.image.load("images/cutePanda.png"), (app_width // 4, app_height - 400))
    printTextCentred(display, "Shopping page", black, 80, app_width // 2, app_height // 6)
    printTextCentred(display, str(clicker.score), black, 30, app_width // 2, app_height // 6 + 100)
    drawRectangle(display,randomCollor(), app_width // 3 + 85, app_height // 3,400,90)
    printText(display, "increase one click score", black, 30, app_width // 3 + 110, app_height // 3 + 10)
    printText(display, "cost 50", black, 30, app_width // 3 + 230, app_height // 3 + 50)
    width = app_width // len(autominers_collection)
    for i in range(len(autominers_collection)):
        drawRectangle(display, randomCollor(), width * (i), app_height // 2 - 30,
                      len(autominers_collection[i].name * 20), 120)
        printText(display, autominers_collection[i].name, black, 20, width * (i) + 50, app_height // 2)
        printText(display,
                  "cost " + str(autominers_collection[i].cost) + " speed " + str(autominers_collection[i].speed)
                  , black, 30, width * (i) + len(autominers_collection[i].name) * 2, app_height // 2 + 30)
