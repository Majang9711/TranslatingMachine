from charset_normalizer import detect
from googletrans import Translator
import tkinter as tk #GUI

translator = Translator()

def Main():
    result = translator.translate(TranslatorEntry.get())

    DetectLabel = tk.Label(root, text=result.text, width=30)
    DetectLabel.grid(row=2,column=2)


root = tk.Tk() 
root.title("이정진의 번역기")
root.geometry("640x200")
root.resizable(False, False)

TranslatorEntryLabel = tk.Label(root, text="번역할 문장 > ", width=10)
TranslatorEntryLabel.grid(row=1, column=0)

TranslatorEntry=tk.Entry(root, width=50, relief="sunken")
TranslatorEntry.insert(0, "번역 하실 문자를 입력 해주세요!!")
TranslatorEntry.grid(row=1, column=2)


ConvertButton = tk.Button(root, text="Translate", overrelief="solid", width=15, command=Main, repeatdelay=1000, repeatinterval=100)
ConvertButton.grid(row=3, column=2)


root.mainloop() #창이 종료시까지 반복