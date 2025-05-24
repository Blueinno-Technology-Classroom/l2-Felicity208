import pyautogui as gui
from PIL import ImageGrab, ImageChops
import time

#gui.displayMousePosition()

dino = {
    "left" : 78,
    "top" : 322,
    "right" : 130,
    "bottom" : 374
}


upper_area = (
    (130 + 20) ,   #left
    322 ,        #top
    (130 + 20 + 100),     #right
    (322 + int(52/2))    #bottom
)

lower_area = (
    (130 +  20),      #left
    (322 + int(52/2)),     #top
    ((130 + 20 )+ 100),   #lower_area left + 200, right
    374    #bottom
)


def screenshot():
    screen_img = ImageGrab.grab()
    screen_img_data = screen_img.load()
    for x in range(lower_area[0] , lower_area[2] ):
        for y in range(lower_area[1], lower_area[3]):
            screen_img_data[x, y] = 0
    for x in range(upper_area[0] , upper_area[2]):
        for y in range(upper_area[1], upper_area[3]):
            screen_img_data[x, y] = 0
    screen_img.show()

def check_similarity(empty_img, img):
    diff = ImageChops.difference(empty_img, img)
    bbox = diff.getbbox()


    if bbox is None:
        similarity = 100.0
    else:
        total_pixels = diff.size[0] * diff.size[1]    #box of lower area
        changed_pixels = (diff.size[0] - bbox[0]) * (diff.size[1] - bbox[1])
        similarity = (total_pixels - changed_pixels) / total_pixels *100
    return similarity



print("taking screenshot of lower area..")
empty_lower_img = ImageGrab.grab(bbox=lower_area).convert("RGB").convert("L")
# empty_lower_img.show()
print("taking screenshot of upper area..")
empty_upper_img = ImageGrab.grab(bbox=upper_area).convert("RGB").convert("L")


print("You may start the game now!")


while True:
    lower_img = ImageGrab.grab(bbox=lower_area).convert("RGB").convert("L")
    similarity = check_similarity(empty_lower_img, lower_img)
    # print(similarity)
    if similarity < 25:
        gui.press("space")
        lower_area = (lower_area[0],
                      lower_area[1],
                      lower_area[2] +3,
                      lower_area[3])
        upper_area = (upper_area[0],
                      upper_area[1],
                      upper_area[2] +3,
                      upper_area[3])
    else:
        upper_img = ImageGrab.grab(bbox=upper_area).convert("RGB").convert('L')
        similarity = check_similarity(empty_upper_img, upper_img)
        if similarity < 30:
            gui.press("down")
            lower_area = (lower_area[0],
                          lower_area[1],
                          lower_area[2] +3,
                          lower_area[3])
            upper_area = (upper_area[0],
                          upper_area[1],
                          upper_area[2] +3,
                          upper_area[3])