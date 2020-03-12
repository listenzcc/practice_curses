import curses
from curses import wrapper

# stdscr will not be used,
# it stays here just for triggering auto-completion
stdscr = curses.initscr()


def main(stdscr):
    # Clear screen
    stdscr.clear()
    # Position of curse
    x, y = 2, 1
    # Display something
    attrs = dict(
        A_NORMAL=curses.A_NORMAL,
        A_BLINK=curses.A_BLINK,
        A_BOLD=curses.A_BOLD,
        A_ITALIC=curses.A_ITALIC,
        A_DIM=curses.A_DIM,
        A_REVERSE=curses.A_REVERSE,
        A_UNDERLINE=curses.A_UNDERLINE,
    )
    for key in attrs:
        stdscr.addstr(y, x, key, attrs[key])
        y += 1

    if curses.has_colors():
        for j in [1, 2, 3]:
            stdscr.addstr(y, x, 'COLOR', curses.color_pair(j))
            y += 1

    # Press keyboard to escape
    stdscr.refresh()
    stdscr.addstr(y, x, 'Press to escape.')
    stdscr.getkey()


if __name__ == '__main__':
    wrapper(main)
