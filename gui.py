from ctypes import sizeof
import sys
from ListenedList import ListenedList
import pygame
import time
import random


class GUI:
    pygame.init()
    pygame.display.set_caption('Algorithm visualiser')

    def __init__(self, list, algorithm) -> None:
        # Algorithm to use
        self.algorithm = algorithm
        # Convert list to a Listened list, which calls list_sort_event() when an element is changed
        self.current_list = ListenedList(self)
        [self.current_list.append(x) for x in list]
        # Set various values for the UI
        self.screen_size = [960, 540]
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_size)
        self.item_count = len(list)
        self.max_value = max(list)
        self.gap = 5
        self.width = (self.screen_size[0]-self.item_count *
                      self.gap) / self.item_count

        self.__start_run()

    def get_rect(self, index, item):
        # rects are created with the top-left x and y coordinates, followed by height and width:
        width = self.width
        height = self.screen_size[1] * (item / self.max_value)
        topleft_x = index * self.gap + index * self.width
        topleft_y = self.screen_size[1] - height
        return pygame.Rect(topleft_x, topleft_y, width, height)

    def __draw(self):
        self.clock.tick(144)
        time.sleep(0.01)
        self.screen.fill((30, 30, 30))
        for index, item in enumerate(self.current_list):
            pygame.draw.rect(self.screen, (92, 28, 76),
                             self.get_rect(index, item))

        pygame.display.update()

    def list_sort_event(self):
        # time.sleep(0.05)
        # Need to handle events for the operating system
        # to consider it as running properly
        # Quit doesn't actally work, all the time is spent on drawing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
        self.__draw()

    def __start_run(self):
        self.running = True
        while(self.running):
            self.__key_event_handler()
            self.__draw()
            # Lower framerate when nothing is moving
            self.clock.tick(30)
        pygame.quit()

    def __key_event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.algorithm(self.current_list)
