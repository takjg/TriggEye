# Copyright (c) 2019 Tak Jaga
# Released under the Apache License, Version 2.0
# https://github.com/takjg/TriggEye/blob/master/LICENSE

from math import sqrt
from sys  import argv, stdin
from time import perf_counter

def getArgs():
    interval = float(argv[1]) # minimum trigger interval (seconds)
    margin   =   int(argv[2]) # margin for error (millimeters)
    return (interval, margin)

def main(interval, margin):
    line = stdin.readline()
    idx  = parse(line)
    while line:
        line = stdin.readline()
        row = line.split(', ')
        detect(idx, row, interval, margin)

def parse(header):
    names = header.split(', ')
    n = len(names)
    z = zip(names, range(n))
    return dict(z)

def get(idx, row, name):
    i = idx[name]
    return row[i]

last = 0

def detect(idx, row, interval, margin):
    d0 = diff(idx, row, 0)
    d1 = diff(idx, row, 1)
    if d0 < margin or d1 < margin:
        global last
        now = perf_counter()
        if now - last > interval:
            frame = get(idx, row, 'frame')
            print(f'{frame} {d0} {d1}', flush=True)
        last = now

def diff(idx, row, lr):
    g = gaze(idx, row, lr)
    e =  eye(idx, row, lr)
    d = distance(e)
    a = add(e, mul(g, d))
    return int(distance(a))

# cf. https://github.com/TadasBaltrusaitis/OpenFace/wiki/Output-Format
def gaze(idx, row, lr):
    def g(c):
        return float(get(idx, row, f'gaze_{lr}_{c}'))
    return (g('x'), g('y'), g('z'))

def eye(idx, row, lr):
    i = 20 if lr == 0 else 48
    def e(c):
        sum = 0
        for j in range(i, i + 8):
            sum += float(get(idx, row, f'eye_lmk_{c}_{j}'))
        return sum / 8
    return (e('X'), e('Y'), e('Z'))

def distance(v):
    (x, y, z) = v
    return sqrt(x * x + y * y + z * z)

def mul(v, n):
    (x, y, z) = v
    return (x * n, y * n, z * n)

def add(v, u):
    (x0, y0, z0) = v
    (x1, y1, z1) = u
    return (x0 + x1, y0 + y1, z0 + z1)

if __name__ == '__main__':
    main(*getArgs())
