import math
import random
import cocos
import cocos.euclid as eu
import cocos.particle_systems as ps


def truncate(vector, m):
    magnitude = abs(vector)
    if magnitude > m:
        vector *= m / magnitude
    return vector


class Actor(cocos.cocosnode.CocosNode):
    def __init__(self, x, y):
        super(Actor, self).__init__()
        self.position = (x, y)
        self.velocity = eu.Vector2(0, 0)
        self.wander_angle = 0
        self.circle_distance = 50
        self.circle_radius = 10
        self.angle_change = math.pi / 4
        self.max_velocity = 50
        self.add(ps.Sun())
        self.schedule(self.update)
        

    def update(self, dt):
        # 정규화를 해준다. 값의 크기에 따라서 영향을 받지 않기 위해서 이다.
        circle_center = self.velocity.normalized() * self.circle_distance
        # 현재 각도에 따라서 dy dx를 구해준다.
        dx = math.cos(self.wander_angle)
        dy = math.sin(self.wander_angle)
        # 이동할 위치의 가중치를 구한다.
        displacement = eu.Vector2(dx, dy) * self.circle_radius
        # 랜덤 값의 위치로 이동한다. -0.5~0.5 사이 값을 가진다. 
        self.wander_angle += (random.random() - 0.5) * self.angle_change
        # 이동할 위치와 현재의 중심 위치를 더한 값을 구하고 정규화한다.
        self.velocity += circle_center + displacement
        self.velocity = truncate(self.velocity, self.max_velocity)
        # 위치를 dt값과 속력을 곱한 값을 위치로 넣는다.
        self.position += self.velocity * dt
        self.position = (self.x % 640, self.y % 480)


class MainLayer(cocos.layer.Layer):
    def __init__(self):
        super(MainLayer, self).__init__()
        self.actor = Actor(320, 240)
        self.add(self.actor)


if __name__ == '__main__':
    cocos.director.director.init(caption='Steering Behaviors')
    scene = cocos.scene.Scene(MainLayer())
    cocos.director.director.run(scene)
