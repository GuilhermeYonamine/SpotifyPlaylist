import pyautogui

pyautogui.FAILSAFE = False
musica = int(input(print("digite o numero de musicas para mover")))
musica -= musica
# pyautogui.position()
# pyautogui.PAUSE = 0.5

# pyautogui.press("win")
# pyautogui.write("spotify")
# pyautogui.press("enter")
# pyautogui.sleep(5)
pyautogui.keyDown("alt")
pyautogui.press("tab")
pyautogui.keyUp("alt")
pyautogui.click(380, 670)
pyautogui.sleep(0.7)
pyautogui.move(350, -50)
pyautogui.click()
pyautogui.leftClick(650, 600)
pyautogui.click()
pyautogui.sleep(3.5)
pyautogui.press("end")
pyautogui.sleep(3)
pyautogui.scroll(700)
pyautogui.sleep(0.5)
pyautogui.mouseDown()
pyautogui.sleep(0.5)
pyautogui.moveTo(650, 400)
pyautogui.moveTo(650, 181)
pyautogui.sleep(20)
pyautogui.moveTo(650, 685)
pyautogui.mouseUp()
pyautogui.sleep(1)

for i in range(musica + 1):
    pyautogui.press("end")
    pyautogui.sleep(3)
    pyautogui.scroll(780)
    pyautogui.sleep(0.5)
    pyautogui.mouseDown()
    pyautogui.sleep(0.5)
    pyautogui.moveTo(650, 400)
    pyautogui.moveTo(650, 181)
    pyautogui.sleep(20)
    pyautogui.moveTo(650, 685)
    pyautogui.mouseUp()
    pyautogui.sleep(1)
