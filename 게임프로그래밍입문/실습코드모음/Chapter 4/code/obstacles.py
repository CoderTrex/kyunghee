import cocos
import cocos.euclid as eu
import cocos.particle_systems as ps


def truncate(vector, m):
    magnitude = abs(vector)
    if magnitude > m:
        vector *= m / magnitude
    return vector


class Obstacle(cocos.cocosnode.CocosNode):
    instances = []
    
    def __init__(self, x, y, r):
        super(Obstacle, self).__init__()
        self.position = (x, y)
        self.radius = r
        particles = ps.Sun()
        particles.size = r * 2
        particles.start_color = ps.Color(0.0, 0.7, 0.0, 1.0)
        self.add(particles)
        self.instances.append(self)


class Actor(cocos.cocosnode.CocosNode):
    def __init__(self, x, y):
        super(Actor, self).__init__()
        self.position = (x, y)
        self.velocity = eu.Vector2(0, 0)
        self.speed = 2
        self.max_velocity = 300
        self.max_force = 10
        self.target = None
        self.max_ahead = 200
        self.max_avoid_force = 300
        self.add(ps.Sun())
        self.schedule(self.update)

    def update(self, dt):
        # 타겟이 없으면 움직이지 않는다.
        if self.target is None:
            return
        # 타겟과 현재의 x, y값을 토대로 움직인다.
        distance = self.target - eu.Vector2(self.x, self.y)
        # 움직여야 하는 곳의 위치 및 방향을 구한다.
        steering = distance * self.speed - self.velocity
        # 피해야 하는 힘을 준다.
        steering += self.avoid_force()
        # 정규화
        steering = truncate(steering, self.max_force) 
        self.velocity = truncate(self.velocity + steering, self.max_velocity)
        # 위치 갱신
        self.position += self.velocity * dt

    def avoid_force(self):
        avoid = eu.Vector2(0, 0)
        # 최대 속도를 곱해주고 최대 속력으로 나누어 준다. -> 이동해야 하는 방향
        ahead = self.velocity * self.max_ahead / self.max_velocity
        # 내적을 해준다.
        l = ahead.dot(ahead)
        if l == 0:
            return avoid
        closest, closest_dist = None, None
        for obj in Obstacle.instances:
            # 방해물 위치와 자신의 위치를 빼서 백터를 구한다
            w = eu.Vector2(obj.x - self.x, obj.y - self.y)
            # w의 내적을 구한다.
            t = ahead.dot(w)
            # 만약 이것이 0과 1사이의 값이면
            if 0 < t < l:
                # 내적값과 속력을 곱한 값, 즉 새롭게 갱신되어 이동해야 하는 값과 현재 위치를 더한다. 
                proj = self.position + ahead * t / l
                # 이것을 방해물 위치와 빼주고 절대값을 씌워 거리를 구한다.
                dist = abs(obj.position - proj)
                
                # 자신과의 거리가 방해물의 반지름(영향권) 
                # and 가장 가까운 거리보다 더 작은 위치로 갱신이 되면 영향권을 바꾼다. (closet is none 은 초기값)
                if (dist < obj.radius) and (closest is None or dist < closest_dist):
                    closest, closest_dist = obj.position, dist
        
        # 가장 가까운 방해물이 없다면 그냥 곱한다.
        if closest is not None:
            avoid = self.position + ahead - closest
            avoid = avoid.normalized() * self.max_avoid_force
        return avoid


class MainLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(MainLayer, self).__init__()
        self.add(Obstacle(200, 200, 40))
        self.add(Obstacle(240, 350, 50))
        self.add(Obstacle(500, 300, 50))
        self.actor = Actor(320, 240)
        self.add(self.actor)

    def on_mouse_motion(self, x, y, dx, dy):
        self.actor.target = eu.Vector2(x, y)


if __name__ == '__main__':
    cocos.director.director.init(caption='Steering Behaviors')
    scene = cocos.scene.Scene(MainLayer())
    cocos.director.director.run(scene)
