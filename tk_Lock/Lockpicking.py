import tkinter as tk

def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

def on_canvas_click(event):
    global pin_x, selected_pin
    pin_x = event.x
    selected_pin = canvas.find_closest(event.x, event.y)[0]

def on_canvas_drag(event):
    global pin_x
    if "moveable" in canvas.gettags(selected_pin):
        x = event.x - pin_x
        # 이미지가 움직일 때의 새로운 x 좌표 계산
        new_x = canvas.coords(selected_pin)[0] + x

        # 이미지가 100 이상인지 확인하고 움직임 제한
        if new_x >= 100 and new_x <=170:
            canvas.move(selected_pin, x, 0)
            pin_x = event.x

        check_image_position()

def on_release(event):

    results = [clear1, clear2, clear3, clear4, clear5]

    if all(results):
        canvas.delete(images[0])
        images.append(canvas.create_image(center_x, center_y, image=unlock))
        canvas.tag_lower(images[6])

        win.after(2000, exit_program)

def exit_program():
    win.destroy()


def check_image_position():
    global clear1, clear2, clear3, clear4, clear5, prev1, prev2, prev3, prev4, prev5, results
    pin1_x = canvas.coords(images[1])[0]
    pin2_x = canvas.coords(images[2])[0]
    pin3_x = canvas.coords(images[3])[0]
    pin4_x = canvas.coords(images[4])[0]
    pin5_x = canvas.coords(images[5])[0]

    conditions = {
        "clear1": (pin1_x == 160),
        "clear2": (pin2_x == 150),
        "clear3": (pin3_x == 130),
        "clear4": (pin4_x == 150),
        "clear5": (pin5_x == 140)
    }

    clear1 = conditions["clear1"]
    clear2 = conditions["clear2"]
    clear3 = conditions["clear3"]
    clear4 = conditions["clear4"]
    clear5 = conditions["clear5"]

    if clear1 and pin1_x != prev1:
        print(1)
    elif clear2 and pin2_x != prev2:
        print(2)
    elif clear3 and pin3_x != prev3:
        print(3)
    elif clear4 and pin4_x != prev4:
        print(4)
    elif clear5 and pin5_x != prev5:
        print(5)
        
    prev1, prev2, prev3, prev4, prev5 = pin1_x, pin2_x, pin3_x, pin4_x, pin5_x

prev1 = prev2 = prev3 = prev4 = prev5 = 0
clear1 = clear2 = clear3 = clear4 = clear5 = False

win = tk.Tk()
win.title("Lock Picking")

width, height = 360, 500
canvas = tk.Canvas(win, width=width, height=height)
canvas.pack()

center_window(win, width, height)

# 이미지 불러오기
lock = tk.PhotoImage(file="tk_Lock/resources/images/Lock.png")
unlock = tk.PhotoImage(file="tk_Lock/resources/images/unlocked_Lock.png")
pin1 = tk.PhotoImage(file="tk_Lock/resources/images/pin1.png")
pin2 = tk.PhotoImage(file="tk_Lock/resources/images/pin2.png")
pin3 = tk.PhotoImage(file="tk_Lock/resources/images/pin3.png")
pin4 = tk.PhotoImage(file="tk_Lock/resources/images/pin4.png")
pin5 = tk.PhotoImage(file="tk_Lock/resources/images/pin5.png")

center_x, center_y = width // 2, height // 2
pin_x = pin1_x = pin2_x = pin3_x = pin4_x = pin5_x = 100
pin1_y = 265
pin_y_gap = 40

# 이미지들을 리스트로 관리
images = []
# 이미지를 캔버스에 추가하고, 이동할 수 있도록 태그를 설정
images.append(canvas.create_image(center_x, center_y, image=lock))
images.append(canvas.create_image(pin1_x, pin1_y, image=pin1, tags="moveable"))
images.append(canvas.create_image(pin2_x, pin1_y + pin_y_gap, image=pin2, tags="moveable"))
images.append(canvas.create_image(pin3_x, pin1_y + pin_y_gap*2, image=pin3, tags="moveable"))
images.append(canvas.create_image(pin4_x, pin1_y + pin_y_gap*3, image=pin4, tags="moveable"))
images.append(canvas.create_image(pin5_x, pin1_y + pin_y_gap*4, image=pin5, tags="moveable"))

# 마우스 클릭 이벤트와 드래그 이벤트를 캔버스에 바인딩
canvas.bind("<Button-1>", on_canvas_click)
canvas.bind("<B1-Motion>", on_canvas_drag)
canvas.bind("<ButtonRelease-1>", on_release)

win.mainloop()
