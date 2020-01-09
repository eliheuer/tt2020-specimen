# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
# macOS only for now... help me port it!?

from drawBot import *
import math

# [W]IDTH,[H]EIGHT,[M]ARGIN
W, H, M = 1024, 1024, 32

# GRID
def grid():
    stroke(1,0,0)
    strokeWidth(1)
    fill(None)
    rect(M + M, M + M, W - (4 * M), H - (4 * M))
    stpX, stpY = 0, 0
    incX, incY = M, M
    for x in range(20):
        polygon(((M + M) + stpX, M + M), ((M + M) + stpX, H - (M + M)))
        stpX += incX
    for y in range(28):
        polygon((M + M, (M + M) + stpY), (W - (M + M), (M + M) + stpY))
        stpY += incY


# NEW PAGE
def new_page():
    newPage(W, H)
    fill(0.8)
    rect(-8, -8, W + 8, H + 8)


# MAIN
new_page()
# grid()  # Toggle for grid/UV-map view
fill(0)
stroke(None)
fontSize(M)

font("TT2020StyleB-Regular.ttf")

text("  _______________   ____ ___   ____  ", M+(M*1), M*30)
text(" /_  __/_  __/__ \ / __ \__ \ / __ \\", M+(M*1), M*29)
text("  / /   / /  __/ // / / /_/ // / / / ", M+(M*1), M*28)
text(" / /   / /  / __// /_/ / __// /_/ /  ", M+(M*1), M*27)
text("/_/   /_/  /____/\____/____/\____/   ", M+(M*1), M*26)
text("Style B                              ", M+(M*1), M*25)
text("                                     ", M+(M*1), M*24)
text("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi  ", M+(M*1), M*23)
text("jklmnopqrstuvwxyz1234567890~`!@#$%^  ", M+(M*1), M*22)
text("&*()-_+={}[]|\:;\"'<>,.?/            ", M+(M*1), M*21)

font("TT2020StyleB-Italic.ttf")

text("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi  ", M+(M*1), M*19)
text("jklmnopqrstuvwxyz1234567890~`!@#$%^  ", M+(M*1), M*18)
text("&*()-_+={}[]|\:;\"'<>,.?/            ", M+(M*1), M*17)
text("                                     ", M+(M*1), M*16)
text("                                     ", M+(M*1), M*15)
text("                                     ", M+(M*1), M*14)

print("Done")
saveImage("texture-map-a.png")
