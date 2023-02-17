from manim import *
import numpy as np
import os

def play(n_edges=[3,4,12], vols=[0,-2,-6]):
    class Polybeat(Scene):
        def construct(self):
            dr = .16
            colors = ['#ff7473','#ffc952','#47b8e0']
            N = len(n_edges)
            op = .4
            T = 1.8
            sounds = ['kick_drum','open_conga','low_bongo']
            dirname = os.path.dirname(__file__)
            sounds = [os.path.join(dirname,'sounds',s) for s in sounds]
            trs = np.linspace(2.5,3.8,N)

            circs = [
                Circle(radius=r).rotate(PI/2)
                for r in trs
            ]

            ps = [
                [i/n for i in range(n)] 
                for n in n_edges
            ]
            vs = [
                [circs[i].point_from_proportion(p) for p in ps[i]]
                for i in range(N)
            ]
            geoms = [Polygon(*v).set_stroke(colors[i],14,op) for i,v in enumerate(vs)]

            dots = []
            for i in range(N):
                dots.append(
                    Dot([0,3.5,0], dr*1.5, color=colors[i]).set_opacity(1)
                )
                dots[-1]._i = i
                dots[-1]._n = n_edges[i]
                dots[-1]._ps = ps[i]
                dots[-1]._p = .9999
                dots[-1]._g = geoms[i]
                dots[-1]._on = False

            def update_dot(d, dt):
                if d._on:
                    d.set_opacity(1)
                    strop = d._g.get_stroke_opacity()
                    if strop > op:
                        d._g.set_stroke(opacity=strop-dt*2)
                    else:
                        d._g.set_stroke(opacity=op)

                    d.move_to(d._g.point_from_proportion(d._p))
                    next_p = (d._p + dt/T) % 1
                    for p in d._ps:
                        if (d._p<=p and next_p>=p) or (next_p < d._p):
                            self.add_sound(sounds[d._i], 0, vols[d._i])
                            geoms[d._i].set_stroke(opacity=1)
                            break
                    d._p = next_p
                else:
                    d.set_opacity(0)
                    d._g.set_stroke(opacity=0)
                    d._p = .9999
            for d in dots[::-1]: 
                d.add_updater(update_dot)

            def play(i0,i1,i2):
                dots[i0]._on = True
                self.wait(T)
                dots[i1]._on = True
                self.wait(T*2)
                dots[i2]._on = True

                self.wait(T*7)

                dots[i0]._on = False
                self.wait(T*2)
                dots[i1]._on = False
                self.wait(T)
                dots[i2]._on = False
                dots[i2].update(0)

            self.wait(.5)
            self.add(*geoms[::-1], *dots[::-1])
            dots[0]._on = True
            self.wait(T)
            dots[0]._on = False
            dots[1]._on = True
            self.wait(T)
            dots[1]._on = False
            dots[2]._on = True
            self.wait(T)
            dots[2]._on = False
            dots[2].update(0)

            play(2,1,0)
            self.remove(*geoms[::-1], *dots[::-1])
            self.wait(.5)
    pb = Polybeat()
    pb.render(preview=True)