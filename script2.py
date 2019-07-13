import time

from pynput.mouse import Button, Controller

mouse = Controller()
from datetime import datetime as dt

f = open("mouse_log.txt", "r")
start_count = 0
end_count = 0


def get_all_action_list(file_data):
    all_actions_list = []
    for line in file_data:
        action_item = str(line).split(',')
        action_item[0] = dt.strptime(str(action_item[0]), '%H:%M:%S.%f')
        all_actions_list.append(action_item)
    return all_actions_list


action_data = get_all_action_list(f)

for index, action in enumerate(action_data):
    done_at = action[0]
    # print(done_at)
    todo = action[1]
    # button = None
    if todo == 'clicked':
        button = todo[4]
    x_axis = float(action[2])
    y_axis = float(action[3])
    # print(action)
    if start_count != 4:
        if todo == 'clicked' and x_axis == 0.0 and y_axis == 0.0:
            start_count += 1
        else:
            continue
    else:
        if todo == 'moved':
            mouse.position = (x_axis, y_axis)
        elif todo == 'clicked':
            mouse.press(Button.left)
            mouse.release(Button.left)
        if index > 0:
            # print('index>>>', index)
            seconds = (done_at - action_data[index - 1][0]).total_seconds()
            # print(seconds)
            time.sleep(seconds)

# # Read pointer position
# print('The current pointer position is {0}'.format(
#     mouse.position))
#
# # Set pointer position
# mouse.position = (10, 20)
# print('Now we have moved it to {0}'.format(
#     mouse.position))
#
# # Move pointer relative to current position
# mouse.move(5, -5)
#
# # Press and release
# mouse.press(Button.left)
# mouse.release(Button.left)
#
# # Double click; this is different from pressing and releasing
# # twice on Mac OSX
# mouse.click(Button.left, 2)
#
# # Scroll two steps down
# mouse.scroll(0, 2)
