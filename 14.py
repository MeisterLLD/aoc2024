i = 0
robots = { }
with open('14','r') as f:
    for ligne in f.read().splitlines():
        p, v = ligne.split(' ')
        p1, p2 = map(int, p.strip('p=').split(','))
        v1, v2 = map(int, v.strip('v=').split(','))
        robots[i] = [(p1,p2), (v1,v2)]
        i += 1

n, m = 101, 103

def updaterobots(howlong):
    for i in range(len(robots)):
        p1, p2 = robots[i][0]
        v1, v2 = robots[i][1]
        robots[i][0] = (p1+howlong*v1) % n, (p2+howlong*v2) % m

def safetyfactor(robots):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for (p1, p2), _ in robots.values():
        if p1 < n//2 and p2 < m//2:
            q1 += 1
        if p1 < n//2 and p2 > m//2:
            q2 += 1
        if p1 > n//2 and p2 < m//2:
            q3 += 1
        if p1 > n//2 and p2 > m//2:
            q4 += 1
    return q1*q2*q3*q4

updaterobots(100)
print('Part 1 :', safetyfactor(robots))

## P2
i = 0
robots = { }
with open('14','r') as f:
    for ligne in f.read().splitlines():
        p, v = ligne.split(' ')
        p1, p2 = map(int, p.strip('p=').split(','))
        v1, v2 = map(int, v.strip('v=').split(','))
        robots[i] = [(p1,p2), (v1,v2)]
        i += 1

i = 0
while True:
    i += 1
    updaterobots(1)
    liste = [robots[i][0] for i in range(len(robots))]
    ensemble = set(liste)
    # on parie sur le fait que la frame du sapin est la seule injective
    if len(liste) == len(ensemble):
        break

print('Part 2 :', i)

## Animation for fun
## Animation for fun
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
#
# updaterobots(7000)
#
# fig = plt.figure()
# xs = [robots[j][0][0] for j in range(len(robots))]
# ys = [103-robots[j][0][1] for j in range(len(robots))]
# dessin, = plt.plot(xs, ys, 'k.')
# plt.title(7000)
#
# def animate(i):
#     updaterobots(1)
#     plt.title(i+7001)
#     xs = [robots[j][0][0] for j in range(len(robots))]
#     ys = [103-robots[j][0][1] for j in range(len(robots))]
#     dessin.set_data(xs, ys)
#     return dessin,
#
#
# ani = animation.FuncAnimation(fig, animate, frames=100,
#                               interval=200, blit=False, repeat=False)
# # saving to m4 using ffmpeg writer
# writervideo = animation.FFMpegWriter(fps=5)
# ani.save('tree.mp4', writer=writervideo)
# ani.event_source.stop()
# del ani
# plt.close()