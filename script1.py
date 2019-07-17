from pynput.mouse import Listener
import logging

logging.basicConfig(filename=("mouse_log.txt"), level=logging.DEBUG, format='%(asctime)s.%(msecs)03d,%(message)s',
                    datefmt='%H:%M:%S')


def on_move(x, y):
    logging.info("moved,{0},{1}".format(x, y))


def on_click(x, y, button, pressed):
    if pressed:
        logging.info('clicked,{0},{1},{2}'.format(x, y, button))


def on_scroll(x, y, dx, dy):
    logging.info('scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))


#
# with Listener(on_move=on_move, on_click=on_click) as listener:
#     listener.join()

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
