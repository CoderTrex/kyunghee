import cocos
import cocos.euclid as eu
import cocos.particle_systems as ps

class ActorExplosion(ps.ParticleSystem):
    # 파티클 입자의 개수
    total_particles = 400
    duration = 0.1
    gravity = eu.Point2(0, 0)
    #  시작하는 angle 90도임 -> angle_var로 360도 적용시켜서 모두 구현
    angle = 90.0
    angle_var = 360.0
    speed = 40.0
    speed_var = 20.0
    life = 3.0
    life_var = 1.5
    emission_rate = total_particles / duration
    # RGBA (A : 투명도) 범위는 0부터 1까지
    start_color_var = ps.Color(0.0, 0.0, 0.0, 0.2)
    end_color = ps.Color(0.0, 0.0, 0.0, 1.0)
    end_color_var = ps.Color(0.0, 0.0, 0.0, 0.0)
    size = 15.0
    size_var = 10.0
    blend_additive = True

    def __init__(self, pos, color):
        super(ActorExplosion, self).__init__()
        self.position = pos
        self.start_color = color

class mainLayer(cocos.layer.Layer):
    def __init__(self):
        super(mainLayer, self).__init__()
        particles = ActorExplosion((200, 100), (1, 0, 0, 1))
        particles.position(200, 100)
        self.add(particles)
        
if __name__ == "__main__":
    cocos.director.director.init(caption = "kldkdkd")
    scene = cocos.scene.Scene(mainLayer())
    cocos.director.director.run(scene)