r = range(5)
for x in r:
    for y in r:
        pydle(x, y, "", "black" if (x,y) == (0,0) or (x,y) == (4,2)
              else "white" if y<3
              else "blue" if y>2 and x+y==4 or y>2 and x+y==6
              else "")   
        if y==2 and x%2 != 0:
            pydle(x, y,"⚡","white")
        
