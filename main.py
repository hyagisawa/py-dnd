import tkinter as tk
from PIL import ImageTk
from tkinterdnd2 import DND_FILES, TkinterDnD

class MyApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        ## ウィンドウサイズ
        width = 260
        height = 260
        self.geometry(f'{width}x{height}')
        self.minsize(width, height)
        self.maxsize(width, height)
        self.title(f'DnD')
       
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
        self.photo_image = ImageTk.PhotoImage(file = "./resource/kaiju.png")
      
       
        # 画像の描画
        self.canvas.create_image(128, 128, image=self.photo_image)
        
        ## ドラッグアンドドロップ
        self.canvas.drop_target_register(DND_FILES)
        self.canvas.dnd_bind('<<Drop>>', self.funcDragAndDrop)


    def funcDragAndDrop(self, e):
        ## ここを編集してください
        message = '\n' + e.data
        print(message)


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
