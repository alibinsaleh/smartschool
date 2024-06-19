import curses

def main(stdscr):
    stdscr.nodelay(True)
    stdscr.clear()
    stdscr.addstr("Press 'q' to quit.\n")

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key != -1:
            stdscr.addstr(f"Key {chr(key)} pressed\n")

curses.wrapper(main)

