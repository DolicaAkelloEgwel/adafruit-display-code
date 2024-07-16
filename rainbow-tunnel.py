import board
import displayio
import framebufferio
import rgbmatrix
import adafruit_display_shapes.circle as c

# If there was a display before (protomatter, LCD, or E-paper), release it so
# we can create ours
displayio.release_displays()
matrix = rgbmatrix.RGBMatrix(
    width=64,
    height=32,
    bit_depth=4,
    rgb_pins=[
        board.MTX_R1,
        board.MTX_G1,
        board.MTX_B1,
        board.MTX_R2,
        board.MTX_G2,
        board.MTX_B2,
    ],
    addr_pins=[board.MTX_ADDRA, board.MTX_ADDRB, board.MTX_ADDRC, board.MTX_ADDRD],
    clock_pin=board.MTX_CLK,
    latch_pin=board.MTX_LAT,
    output_enable_pin=board.MTX_OE,
)
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

g = displayio.Group()

rainbow_colors = [
    16711680,  # Red
    16744192,  # Orange
    16776960,  # Yellow
    65280,  # Green
    65535,  # Cyan
    255,  # Blue
    16711935,  # Magenta
    9109759,  # Violet
]

for i in range(1, 9):
    circle = c.Circle(32, 16, i * 4, outline=rainbow_colors[i - 1], stroke=2)
    g.append(circle)

display.root_group = g

while True:
    for i in range(len(g)):
        r_old = g[i].r
        outline = g[i].outline
        new_c = c.Circle(32, 16, (r_old + 1) % 31 + 1, outline=outline, stroke=2)
        g[i] = new_c
    display.refresh()
