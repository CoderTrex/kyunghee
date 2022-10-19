import cocos
import cocos.actions as ac
if __name__ == '__main__':
    cocos.director.director.init(caption='Actions 101')
    layer = cocos.layer.Layer()
    sprite = cocos.sprite.Sprite('tank.png', position=(200, 200))
    sprite.do(ac.MoveTo((250, 300), 3))
    layer.add(sprite)
    scene = cocos.scene.Scene(layer)
    cocos.director.director.run(scene)

#sprite.do(ac.MoveTo((250, 300), 3))
sprite.do(ac.JumpTo((500, 200), 100, 5, 3)) 
#position, height, jumps, duration
#sprite.do(ac.RotateTo(90, 2))
#sprite.do(ac.ScaleTo(2, 2))
#sprite.do(ac.FadeIn(3))
#sprite.do(ac.Delay(2)+ac.MoveTo((250, 300), 3))
#sprite.do(ac.Blink(10, 2)) # times, duration



ac.MoveBy((80, 0), 3) + ac.Delay(3) + ac.CallFunc(sprite.kill)
ac.MoveBy((80, 0), 3) | ac.RotateBy(90, 2)
ac.MoveBy((80, 0), 3) | ac.RotateBy(90, 2) + ac.CallFunc(sprite.kill)


class Hit(ac.IntervalAction):
    def init(self, duration=0.5):
        self.duration = duration
    def update(self, t):
        self.target.color = (255, 255 * t, 255 * t)