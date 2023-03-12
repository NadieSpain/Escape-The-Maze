from sprite_object import *
import map 
import settings 
import random 


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite

        self.goals_list=[]

        for i in range(5):
            x,y=random.randrange(1,settings.NVoxelX,2)+0.5,random.randrange(1,settings.NVoxelY,2)+0.5
            self.add_goal(AnimatedSprite(self.game, path=self.anim_sprite_path + 'red_light/0.png', pos=(x,y)))


    
    def check_win(self):
        if self.goals_list==[]:
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()
            for i in range(5):
                x,y=random.randrange(1,settings.NVoxelX,2)+0.5,random.randrange(1,settings.NVoxelY,2)+0.5
                self.add_goal(AnimatedSprite(self.game, path=self.anim_sprite_path + 'red_light/0.png', pos=(x,y)))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [sprite.update() for sprite in self.goals_list]
        self.check_win()


    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
    def remove_sprite(self,sprite):
        self.sprite_list.remove(sprite)

    def add_goal(self,sprite):
        self.goals_list.append(sprite)
    def remove_goal(self,sprite):
        self.goals_list.remove(sprite)

