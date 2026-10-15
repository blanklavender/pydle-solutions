r = range(5)
for x in r:
    for y in r:
        pydle(x, y, "",
              "red" if y<2 and x+y == 3
              else "white" if y in (2,4) and 0<x<4
              else "blue" if y<3
             else "")
        if y == 4 and x % 4 == 0:
              pydle(x, y, "🧊", "blue")
