import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("700x700")
root.title("Webカメラでの撮影")

main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, sticky=(tk.N, tk.W))
main_frame.grid_rowconfigure(0,weight=1)
main_frame.grid_columnconfigure(0,weight=1)

image_pil = None

vid = cv2.VideoCapture(0)
if not vid.isOpened():
    messagebox.showerror("うええええええええん","カメラが開けなかったのおおおぉぉぉぉぉぉ")
    exit(-1)
camera_width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
camera_height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("camera_width,camera_height={},{}".format(camera_width, camera_height))


canvas = tk.Canvas(main_frame, width=camera_width, height=camera_height, bg="#aaaaaa")
canvas.pack()

exit_button = tk.Button(main_frame, text="終わる", command=lambda: exit(0))
exit_button.pack()

save_button = tk.Button(main_frame, text="カシャ！", command=lambda: image_pil.save("picture.jpg", quality=95))
save_button.pack()

image_tk=None#グローバル変数にしてGCに消されないようにする必要がある
def update():
    global image_pil,image_tk
    ret, image_ndarray = vid.read()
    if ret:
        image_ndarray = cv2.cvtColor(image_ndarray, cv2.COLOR_BGR2RGB)
        print(image_ndarray.shape)
        image_pil = Image.fromarray(image_ndarray)
        image_tk = ImageTk.PhotoImage(image=image_pil)
        canvas.create_image(0,0, image=image_tk,anchor=tk.NW)
    else:
        image_ndarray = None
    root.after(100, update)


update()
print("mainloopに入る")
root.mainloop()
