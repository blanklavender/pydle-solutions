# Pydle #230
# ⬛⬜⬛⬛⬛
# ⬜⬛⬛⬛⬛
# ⬛⬜⬛⬛⬛
# ⬜⬛⬛⬛⬛
# 🟥⬜⬜🟨🟨

# Attempts: 18
# Characters: 215/250
# https://pydle.net/

r = range(5)
for x in r:
    for y in r:
        pydle(x, y, "", "black")
        if x>2 and y == 4:
            pydle(x, y, "", "yellow")
        elif x == 0 and y == 4:
            pydle(x, y, "", "red")
        elif y%2 == 0 and x == 1 or y%2 != 0 and x == 0 or y == 4:
            pydle(x, y, "", "white")
        elif x == 4 and y == 0:
            pydle(x, y, "😷", "black")
