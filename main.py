import mimetypes
import os
import subprocess
import sys
import tkinter as tk

from PIL import ImageTk
from tkinterdnd2 import DND_FILES, TkinterDnD

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class MyApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        ## ウィンドウサイズ
        width = 260
        height = 260
        self.geometry(f'{width}x{height}')
        self.minsize(width, height)
        self.maxsize(width, height)
        self.title(f'convert webp')
       
        # ## フレーム
        self.frame_drag_drop = frameDragAndDrop(self)

        # ## 配置
        self.frame_drag_drop.grid(column=0, row=0, padx=0, pady=0, sticky=(tk.E, tk.W, tk.S, tk.N))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


class frameDragAndDrop(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # canvas
        self.canvas = tk.Canvas(self)
        
        # canvas の配置
        self.canvas.pack(expand=True,fill=tk.BOTH)
        
        # 画像パス
        self.photo_image = ImageTk.PhotoImage(file=resource_path("./resource/dnd.png"))
       
        # 画像の描画
        self.canvas.create_image(128, 128, image=self.photo_image)
        
        ## ドラッグアンドドロップ
        self.canvas.drop_target_register(DND_FILES)
        self.canvas.dnd_bind('<<Drop>>', self.funcDragAndDrop)


    def funcDragAndDrop(self, e):

        image_list = self.canvas.tk.splitlist(e.data)

        for im in image_list:
            if 'image' in mimetypes.guess_type(im)[0]:
                dirname=os.path.dirname(im)
                basename=os.path.splitext(os.path.basename(im))[0]
                command=[bin_file, im, '-metadata', 'icc', '-o', f'{dirname}/{basename}.webp']
                subprocess.run(command)
        


if __name__ == "__main__":
    bin_file = f'{os.path.dirname(__file__)}/resource/cwebp.exe'
    app = MyApp()
    app.mainloop()
