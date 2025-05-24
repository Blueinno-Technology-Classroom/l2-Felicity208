import pyautogui as gui
import keyboard
import time
import multiprocessing

gui.PAUSE = 0

#gui.displayMousePosition()
btn_pos = (296, 337)


upgrade_btn_pos = [
    (655, 298),
    (655, 346),
    (655, 393),
    (655, 440),
    (655, 487),
]


def click_button():
    while True:
        gui.click(btn_pos)
        if keyboard.is_pressed("Esc"):
            break


def click_upgrade():
    while True:
        for pos in upgrade_btn_pos:
            im = gui.screenshot()
            pos_scaled = (pos[0]*2, pos[1]*2)
            _, g, _, _ = im.getpixel(pos_scaled)
            #print(g, pos)
            if g > 100:
                time.sleep(0.2)
                gui.click(pos)
        if keyboard.is_pressed("Esc"):
            break

            

if __name__ == '__main__':
    main_process = multiprocessing.Process(target=click_button)
    upgrade_process = multiprocessing.Process(target=click_upgrade)

    main_process.start()
    upgrade_process.start()