"""
	COPYRIGHT INFORMATION
	---------------------
Python Twitch bot
	Copyright © Renato Souza 2020.

Some code in this file is licensed under the Apache License, Version 2.0.
    http://aws.amazon.com/apache2.0/
	NOTES
	-----

Otherwise, the modifications to this code, and all the code in the /lib directory, are copyright © Renato Souza 2020.
"""

import cv2 as cv
import numpy as np
import pyautogui
import os

from irc.bot import SingleServerIRCBot
from requests import get
from time import time
from windowcapture import WindowCapture
from vision import Vision
from lib import cmds

NAME = "LorPlays"
OWNER = "lorplays"
TOKEN = "cfz4w854dhcow6ed6f3rpigxnn1idi"
CLIENTID = "gp762nuuoqcoxypju8c569th9wz7q5"


def Start(GameMode, Deck):
    if GameMode == "PvE":
        pyautogui.click((2003, 368), clicks=1, interval=1)
        pyautogui.click((2216, 343), clicks=1, interval=1)
        if Deck == 1:
            pyautogui.click((2566, 302), clicks=1, interval=1)
        elif Deck == 2:
            pyautogui.click((2908, 292), clicks=1, interval=1)
        elif Deck == 3:
            pyautogui.click((3249, 313), clicks=1, interval=1)
        elif Deck == 4:
            pyautogui.click((3593, 316), clicks=1, interval=1)
        # Play
        pyautogui.click((3548, 982), clicks=1, interval=1)
        
    elif(GameMode == "PvP"):
        pyautogui.click((2003, 368), clicks=1, interval=1)
        pyautogui.click((2222, 262), clicks=1, interval=1)
        if Deck == 1:
            pyautogui.click((2566, 302), clicks=1, interval=1)
        elif Deck == 2:
            pyautogui.click((2908, 292), clicks=1, interval=1)
        elif Deck == 3:
            pyautogui.click((3249, 313), clicks=1, interval=1)
        elif Deck == 4:
            pyautogui.click((3593, 316), clicks=1, interval=1)
        # Play
        pyautogui.click((3548, 982), clicks=1, interval=1)
        
    elif(GameMode == "Gauntlet"):
        print("Teste")
        
    elif(GameMode == "Labs"):
        pyautogui.click((2003, 368), clicks=1, interval=1)
        pyautogui.click((2216, 343), clicks=1, interval=1)
        # Play
        pyautogui.click((3090, 802), clicks=1, interval=1)

def Replace(args):
    argList = args.split()
    for item in argList:
        if item == "1":
            pyautogui.click((2452, 541), clicks=1, interval=1)
        elif item == "2":
            pyautogui.click((2726, 541), clicks=1, interval=1)
        elif item == "3":
            pyautogui.click((3040, 541), clicks=1, interval=1)
        elif item == "4":
            pyautogui.click((3310, 541), clicks=1, interval=1)
        pass
    pyautogui.click((3590, 539), clicks=1, interval=2)

def DontReplace():
    pyautogui.click((3590, 539), clicks=1, interval=1)

def Emoji(Name):
    pyautogui.click((2277, 1031), clicks=1, interval=0.25)
    if Name == "Shen":
        pyautogui.click((2278, 846), clicks=1, interval=0.25)
    elif Name == "SadPoro":
        pyautogui.click((2074, 842), clicks=1, interval=1)
    elif Name == "Jinx":
        pyautogui.click((2284, 357), clicks=1, interval=1)
    elif Name == "Darius":
        pyautogui.click((2091, 603), clicks=1, interval=1)
    elif Name == "Dongers":
        pyautogui.click((2303, 590), clicks=1, interval=1)
    elif Name == "Poro":
        pyautogui.click((2072, 372), clicks=1, interval=1)

def Surrender():
    pyautogui.click((3766, 52), clicks=1, interval=1)
    pyautogui.click((2733, 892), clicks=1, interval=1)
    pyautogui.click((3017, 609), clicks=1, interval=10)
    # waiting to cancel
    pyautogui.click((3192, 984), clicks=1, interval=1)

def DragAndDrop(initialX, initialY, dropX, dropY, Delay):
    # initialX, initialY, dropX, dropY, Delay
    pyautogui.moveTo(initialX, initialY, Delay)
    pyautogui.dragTo(dropX, dropY, Delay)

def UseSpell(initialX, initialY, clickX, clickY, Delay):
    pyautogui.moveTo(initialX, initialY, Delay)
    pyautogui.click(clickX, clickY, Delay)
    pyautogui.click((3590, 539), clicks=1, interval=1)

def IsMyRound():
    pass

def Allin(initialX, InitialY):
    pyautogui.moveTo(3046, 902,0.25)
    pyautogui.mouseDown(button="left")
    pyautogui.moveTo(2439, 902, 0.5)
    pyautogui.moveTo(2488, 707, 0.1)
    pyautogui.moveTo(2864, 674, 0.1)
    pyautogui.mouseUp(button="Left")
    
#region Captura de Tela

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# initialize the WindowCapture class
wincap = WindowCapture('Legends of Runeterra')
# initialize the WindowCapture class
vision_IP = Vision('img\minalegal.jpg')


loop_time = time()
while(True):
    screenshot = wincap.get_screenshot()
    
    #cv.imshow('Computer Vision', screenshot)
    #points = vision_limestone.find(screenshot, 0.5, 'rectangles')
    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')
    points = vision_IP.find(screenshot, 0.7, 'rectangles')
    
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    # press 'q' with the out
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
print('Done.')
#endregion

#region Procurando imagem dentro do jogo

'''
#haystack_img = cv.imread('img/myRound.png', cv.IMREAD_UNCHANGED)
#needle_img = cv.imread('img/btnPass.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(wincap.get_screenshot(), vision_IP, cv.TM_CCOEFF_NORMED)

# cv.imshow('Result', result)
# cv.waitKey()

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

threshold = 0.8
if max_val >= threshold:
    print('Found button.')

    # pega as dimensões da imagem pequena
    needle_w = vision_IP.shape[1]
    needle_h = vision_IP.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1], needle_h)

    cv.rectangle(needle_img, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
    # cv.drawMarker(needle_img, max_loc, (255,255,0), markerType=None, markerSize=None, thickness=None, line_type=None)
    # cv.circle(needle_img, max_loc, 5, color=(255,255,0), thickness=2, lineType=cv.LINE_4, shift=None)

    # cv.imshow('Result', haystack_img)
    # cv.waitKey()

    # Aqui é onde o programa captura a imagem e vai
    # pyautogui.click(top_left, clicks=1, interval=1, duration=0.1);

    # Start()
    # Replace("4 2 3 1")
else:
    print('Image not found.')'''

#endregion

#region Bot da Twitch
class Bot(SingleServerIRCBot):
	def __init__(self):
		self.HOST = "irc.chat.twitch.tv"
		self.PORT = 6667
		self.USERNAME = NAME.lower()
		self.CLIENT_ID = CLIENTID
		self.TOKEN = TOKEN
		self.CHANNEL = f"#{OWNER}"

		url = f"https://api.twitch.tv/kraken/users?login={self.USERNAME}"
		headers = {"Client-ID": self.CLIENT_ID, "Accept": "application/vnd.twitchtv.v5+json"}
		resp = get(url, headers=headers).json()
		self.channel_id = resp["users"][0]["_id"]

		super().__init__([(self.HOST, self.PORT, f"oauth:{self.TOKEN}")], self.USERNAME, self.USERNAME)

	def on_welcome(self, cxn, event):
		for req in ("membership", "tags", "commands"):
			cxn.cap("REQ", f":twitch.tv/{req}")

		cxn.join(self.CHANNEL)
		#db.build()
		self.send_message("Now online.")
		#Start("PvE", 1)
		#Replace("1 2")
		#Emoji("Shen")
		#DragAndDrop(3049,1056,2851, 652, 1)
		#UseSpell(2851, 652, 2883, 916, 1)
		#Allin(3046, 902)
  
	def on_pubmsg(self, cxn, event):
		tags = {kvpair["key"]: kvpair["value"] for kvpair in event.tags}
		user = {"name": tags["display-name"], "id": tags["user-id"]}
		message = event.arguments[0]
		
		if user["name"] != NAME:
			cmds.process(bot, user, message)
		
		print(f"Message from {user['name']}: {message}")
	def send_message(self, message):
		self.connection.privmsg(self.CHANNEL, message)

if __name__ == "__main__":
	bot = Bot()
	bot.start()
#endregion 