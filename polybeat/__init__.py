from manim import *
import numpy as np
import os
    
config.disable_caching = True

def play(
    rhythms=[3,4,6,12],
    custom_order=None,
    colors=[RED,YELLOW,BLUE,GREEN],
    sounds=['kick_drum','open_conga','side_stick','low_bongo'],
    volumes=[0,-2,-6,-4],
    cycle_time=1.8,
    dot_radius=0.16,
    width_range=[2.5,3.5],
    preview=True,
):
    class Polybeat(Scene):
        def construct(self):
            dr = dot_radius
            N = len(rhythms)
            op = .4
            T = cycle_time
            trs = np.linspace(*width_range,N)
            defaut_dir = os.path.dirname(__file__)
            defaut_sounds = [os.path.join(defaut_dir,'sounds',s) for s in sounds]
            if custom_order:
                idx=custom_order
            else:
                idx=list(range(N))[::-1]

            circs = [
                Circle(radius=r).rotate(PI/2)
                for r in trs
            ]

            ps = [
                [i/n for i in range(n)] 
                for n in rhythms
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
                dots[-1]._n = rhythms[i]
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
                            try:
                                self.add_sound(defaut_sounds[d._i], 0, volumes[d._i])
                            except:
                                self.add_sound(sounds[d._i], 0, volumes[d._i])
                            geoms[d._i].set_stroke(opacity=1)
                            break
                    d._p = next_p
                else:
                    d.set_opacity(0)
                    d._g.set_stroke(opacity=0)
                    d._p = .9999
            for d in dots[::-1]: 
                d.add_updater(update_dot)

            def play(*idx):
                for i in idx:
                    dots[i]._on = True
                    if i==idx[0]:
                        self.wait(T)
                    else: 
                        self.wait(2*T)
                self.wait(5*T)
                for i in idx:
                    dots[i]._on = False
                    if i==idx[-1]:
                        dots[i]._on = False
                        dots[i].update(0)
                    elif i==idx[-2]:
                        dots[i]._on = False
                        self.wait(T)
                    else:
                        dots[i]._on = False
                        self.wait(T*2)
            self.wait(.5)
            self.add(*geoms[::-1], *dots[::-1])
            for i in range(N):
                I = idx[i]
                if i==0:
                    dots[I]._on = True
                    self.wait(T)
                else:
                    dots[idx[i-1]]._on = False
                    dots[I]._on = True
                    self.wait(T)
                if i==N-1:
                    dots[I]._on = False
                    dots[I].update(0)
            play(*idx[::-1])
            self.remove(*geoms[::-1], *dots[::-1])
            self.wait(.5)

    pb = Polybeat()
    pb.render(preview=preview)

if __name__ == '__main__':
    play(custom_order=[0,1,3,2], sounds=['sounds/kick_drum','sounds/open_conga','sounds/side_stick','sounds/low_bongo'], preview=False)