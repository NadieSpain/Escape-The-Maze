from settings import *
from map import *
import sprite_object
import pygame as pg
import math



class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.rel = 0
        self.time_prev = pg.time.get_ticks()

    def check_game_over(self):
        if self.health <= 0:
            self.game.object_renderer.game_over()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()

        

    def single_fire_event(self, event):
        def Num(N):
            return int(N)+0.5

        if event.type == pg.MOUSEBUTTONDOWN:

            sprite_list=self.game.object_handler.sprite_list
            goals_list=self.game.object_handler.goals_list
            
            if event.button == 1:
                for i in sprite_list+goals_list:
                    if Num(i.x)==Num(self.x) and Num(i.y)==Num(self.y):
                        return
                self.game.object_handler.add_sprite(sprite_object.AnimatedSprite(self.game, pos=(Num(self.x),Num(self.y))))
            
            if event.button == 3:
                for i in sprite_list:
                    if Num(i.x)==Num(self.x) and Num(i.y)==Num(self.y):
                        self.game.object_handler.remove_sprite(i)
                        return
                for i in goals_list:
                    if Num(i.x)==Num(self.x) and Num(i.y)==Num(self.y):
                        self.game.object_handler.remove_goal(i)
                        self.game.sound.take_goal.play()
                        return

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos


        self.check_wall_collision(dx, dy)

        # if keys[pg.K_LEFT]:
        #     self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        # if keys[pg.K_RIGHT]:
        #     self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        
        pg.draw.line(self.game.screen, 'yellow', (self.x * 10, self.y * 10),
                    (self.x + (WIDTH/2) * math.cos(self.angle),
                     self.y + (HEIGHT/2) * math.sin(self.angle)), 2)
        
        pg.draw.circle(self.game.screen, 'green', (self.x * 10, self.y * 10), 6)

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_control()
    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)