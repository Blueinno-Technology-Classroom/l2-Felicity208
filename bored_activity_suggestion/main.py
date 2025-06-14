import os
from openai import AzureOpenAI
# import pygame, pygame.camera
import cv2


# endpoint = "https://ai-gpt-instance.openai.azure.com/"
# model_name = "gpt-4.1-nano"
# deployment = "gpt-4.1-nano"

# subscription_key = "748f28e0fdb44d919a2f1bc89004d444"
# api_version = "2024-12-01-preview"

# client = AzureOpenAI(
#     api_version=api_version,
#     azure_endpoint=endpoint,
#     api_key=subscription_key
# )

# system_message = "you are responsible for providing task or activities options for secondary students, that can be worked on alone. These actvities should either be relieving boredom, or boosting physical, mental and social health."

# history = [
#         {"role": "system", "content": system_message},
#         {"role": "user", "content": "Suggest two activity options"}
#     ]

# response = client.chat.completions.create(
#     model=deployment,
#     temperature=0.6,
#     max_tokens=400,
#     messages=history
# )
# # print(response)


# while True:
#     content = response.choices[0].message.content
#     history.append({"role":"assistant", "content":content})
#     print(content)


#     user_response = input("Type your choice (1 / 2 / None of these):  ")

#     if user_response == "1":
#         history.append({"role": "user", "content": "I prefer option 1, please elaborate on the details and break down the steps"})
#     elif user_response == "2":
#         history.append({"role": "user", "content": "I prefer option 2, please elaborate on the details and break down the steps"})
#     else:
#         history.append({"role": "user", "content": "Please suggest two more different options."})

#     response = client.chat.completions.create(
#         model=deployment,
#         temperature=0.6,
#         max_tokens=400,
#         messages=history
#     )

#     if user_response == "1" or user_response == "2":
#         break

# content = response.choices[0].message.content

# history.append({"role":"assistant", "content":content})

# print(content)

# input("Hit enter key once you have finished this activity!")

# print("Now take a picture and show me your result!")

# pygame.camera.init()
# print(pygame.camera.list_cameras())
# cam = pygame.camera.Camera("FaceTime HD Camera", (640, 480))
# cam.start()
# img = cam.get_image()
# pygame.image.save(img, "image.png")


cam = cv2.VideoCapture(0)

while True:
    s, img = cam.read()
    if s:
        cv2.namedWindow("camera", cv2.WINDOW_AUTOSIZE)
        cv2.putText(img=img,
                    text="Press Space to take a picture!",
                    org=(30,50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=4,
                    color=(255,255,255),
                    thickness=9)
        cv2.putText(img=img,
                    text="Press Space to take a picture!",
                    org=(30,50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=4,
                    color=(0,0,0),
                    thickness=4)
        cv2.imshow("camera", img)

        if cv2.waitKey(1) == 32:
            _, img = cam.read()
            break



cv2.destroyAllWindows()
cv2.imwrite("image.png", img)