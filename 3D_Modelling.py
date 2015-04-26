from visual import *

box(pos=(0,5,0), length=50, height=2, width=1, make_trail=True)
box(pos=(-10,5,0), length=50, height=2, width=1, axis = (50,0,150))
box(pos=(10,5,0), length=50, height=2, width=1, axis = (50,0,150))
box(pos=(0,7,-3), length=5, height=5, width=6, color = (0,1,0), axis = (50,0,0), make_trail=True)
box(pos=(0,5,0), length=5, height=2, width=1, up=(9,0.5,0.5))

lamp = local_light(pos=(10,10,10), color=color.yellow)
sphere(pos=(10,40,10), radius=2, color=color.yellow)

box(pos=(50,5,50), color=color.blue)
label(pos=(50,5,50), text='Bakery',  xoffset=20,
    yoffset=12, space=2,
    height=10, border=0,
    font='sans')

box(pos=(80,-5,-20), color=color.blue)
label(pos=(80,-5,-20), text='Bakery',  xoffset=20,
    yoffset=12, space=2,
    height=10, border=0,
    font='sans')

box(pos=(112,5,80), color=color.blue)
label(pos=(112,5,80), text='Disco',  xoffset=20,
    yoffset=12, space=2,
    height=10, border=0,
    font='sans')





