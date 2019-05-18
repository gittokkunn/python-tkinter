import sys 
import tkinter
from tkinter import StringVar, ttk
from pytube import YouTube


root = tkinter.Tk()
root.title("Sample App")
root.geometry('500x500+0+0')


# プログレスバー
ft = ttk.Frame()
progressbar = ttk.Progressbar(
    ft,
    orient='horizontal',
    length=200,
    mode='determinate'
)
ft.grid()
progressbar.grid()
progressbar.configure(maximum=10, value=0)
progressbar.start(10)

# ラベル
lbl = tkinter.Label(text='URL')
lbl.place(x=30, y=70)


# ラベル
title = tkinter.Label(text='動画タイトル')
title.place(x=60, y=30)


def getVideoInfo():
    try:
        yt = YouTube(sv.get())
        lbl.configure()
        title['text'] = yt.title
        print(f'title: {yt.title}')
    except:
        print('URL not valid')
    

# URL入力フォーム
sv = StringVar()
# sv.trace("w", lambda name, index, mode, sv=sv: getVideoInfo(sv))
input = tkinter.Entry(width=20, textvariable=sv, validate="focusout", validatecommand=getVideoInfo)
input.place(x=90, y=70)


def download():
    progressbar.start(10)
    url = input.get()
    print(f'start download from {url}')
    yt = YouTube(url)
    yt.streams.first().download()
    progressbar.stop()
    # progressbar['value'] = 0
    print(f'download done')


btn = tkinter.Button(root, text='ダウンロード', command=download)
btn.place(x=80, y=100)


root.mainloop()