import win32clipboard
import pyautogui
import speak_now

def select_speak():
    pyautogui.hotkey('ctrl','c')
    win32clipboard.OpenClipboard()
    x=win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    speak_now.speak(x)

