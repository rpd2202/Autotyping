import pyautogui
while 1:
    b=input("Type the message to send repeateadly:")
    a=int(input("enter number of times to send the message:"))
    o=''
    while o=='':
        o=pyautogui.confirm("Click on the text box and press YES",buttons=['YES','NO'])
    for i in range(1,a+1):
        pyautogui.write(b,interval=0.1)
        pyautogui.press('enter')
    pyautogui.press('enter')
