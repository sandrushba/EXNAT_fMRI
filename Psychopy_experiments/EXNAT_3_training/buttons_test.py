from psychopy import core, event, visual
import serial
import time
ser = serial.Serial("/dev/tty.usbserial-1140", 19200, timeout=1)
time.sleep(2)  # Allow time for the serial connection to establish
win = visual.Window([800, 600], fullscr=False, color=(1, 1, 1), units='pix')
def check_button_box():
    if ser.in_waiting > 0:
        button_press = ser.readline().decode('utf-8').strip()
        return button_press
    return None
message = visual.TextStim(win, text='Press a button on the button box.', color=(-1, -1, -1))
message.draw()
win.flip()

while True:
    button_press = check_button_box()
    if button_press:
        print(f'Button pressed: {button_press}')
        core.wait(10)
        break
    if 'escape' in event.getKeys():
        break

win.close()
core.quit()