from classes.vertex_class import *

def bfs(g,vertKey):
    s = g.getVertex(vertKey)
    s.setDistance(0)
    s.setPred(None)
    s.setColor('grey')
    Q = Queue()
    Q.enqueue(s)
    while (Q.size() > 0):
        w = Q.dequeue()
        for v in w.getAdj():
            if (v.getColor() == 'white'):
                v.setColor('grey')
                v.setDistance(w.getDistance() + )
                v.setPred(w)
                Q.enqueue(v)
        w.setColor('black')
