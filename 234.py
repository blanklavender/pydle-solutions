r = range(5)
for x in r:
    for y in r:
        pydle(x, y, 
              "🟡" if (x,y) == (1,3) else ""
              , 
              "green" if y==4
              else "white" if (x,y) == (4,0)
              else "red" if x in (3,4) and y in (0,1)
              else "white" if x<2 or x>2
             else "")
