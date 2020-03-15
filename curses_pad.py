import curses
import random

pad_height = 100
pad_width = 100

window_topleft_y = 3
window_topleft_x = 5
window_bottomright_y = window_topleft_y + 15
window_bottomright_x = window_topleft_x + 25

screen = curses.initscr()

# X ruler
x_rule = curses.newpad(1, 30)
for x in range(26):
    try:
        x_rule.addch(0, x, ord('A') + x)
    except curses.error:
        pass
x_rule.refresh(0, 0,
               window_topleft_y-2, window_topleft_x,
               window_topleft_y-2, window_topleft_x+25)

# Y ruler
y_rule = curses.newpad(30, 2)
for y in range(26):
    try:
        s = str(y)
        if len(s) == 1:
            y_rule.addch(y, 0, ord(' '))
            y_rule.addch(y, 1, ord(s[0]))
        else:
            y_rule.addch(y, 0, ord(s[0]))
            y_rule.addch(y, 1, ord(s[1]))
    except curses.error:
        pass
y_rule.refresh(0, 0,
               window_topleft_y, window_topleft_x-4,
               window_topleft_y+15, window_topleft_x-3)

# Make the pad
pad = curses.newpad(pad_height, pad_width)

# Fill the pad
for y in range(pad_height):
    for x in range(pad_width):
        try:
            pad.addch(y, x, ord('a') + random.randint(0, 25))
        except curses.error:
            pass


def refresh_pad(pad, pad_anchor_y, pad_anchor_x):
    # Displays a section of the pad
    pad.refresh(pad_anchor_y, pad_anchor_x,
                window_topleft_y, window_topleft_x,
                window_bottomright_y, window_bottomright_x)


y, x = 0, 0
refresh_pad(pad, y, x)

for _ in range(1000000):
    c = pad.getkey()

    if c == 'q':
        break

    if c == 'l':
        x += 1
        if x > 10:
            x = 10

    if c == 'h':
        x -= 1
        if x < 0:
            x = 0

    if c == 'j':
        y += 1
        if y > 10:
            y = 10

    if c == 'k':
        y -= 1
        if y < 0:
            y = 0

    refresh_pad(pad, y, x)
