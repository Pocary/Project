import tkinter as tk

def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


def check_password():
    password = [7, 2, 7, 8, 9]
    length = len(password)
    if enteredPwd[-length:] == password:
        clear_image_output()
    else:
        wrong_image_output()


def wrong_image_output():
    wrong_image = canvas.create_image(center_x, center_y - 130, image=wrong)
    win.after(200, lambda: canvas.itemconfig(wrong_image, state='hidden'))
    win.after(400, lambda: canvas.itemconfig(wrong_image, state='normal'))
    win.after(600, lambda: canvas.itemconfig(wrong_image, state='hidden'))


def clear_image_output():
    clear_image = canvas.create_image(center_x, center_y - 130, image=clear)
    win.after(300, lambda: canvas.itemconfig(clear_image, state='hidden'))
    win.after(600, lambda: canvas.itemconfig(clear_image, state='normal'))
    win.after(900, lambda: canvas.itemconfig(clear_image, state='hidden'))
    win.after(1200, lambda: canvas.itemconfig(clear_image, state='normal'))
    # win.after(1500, lambda: canvas.itemconfig(clear_image, state='hidden'))
    # win.after(1800, lambda: canvas.itemconfig(clear_image, state='normal'))
    win.after(2000, exit_program)


def exit_program():
    win.destroy()


def on_click(image_id):
    enteredPwd.append(image_id)

win = tk.Tk()
win.title("Door Lock")

width, height = 360, 500
center_window(win, width, height)
canvas = tk.Canvas(win, width=width, height=height)
canvas.pack()

board = tk.PhotoImage(file="tk_doorlock/images/board.png")
num0 = tk.PhotoImage(file="tk_doorlock/images/num0.png")
num1 = tk.PhotoImage(file="tk_doorlock/images/num1.png")
num2 = tk.PhotoImage(file="tk_doorlock/images/num2.png")
num3 = tk.PhotoImage(file="tk_doorlock/images/num3.png")
num4 = tk.PhotoImage(file="tk_doorlock/images/num4.png")
num5 = tk.PhotoImage(file="tk_doorlock/images/num5.png")
num6 = tk.PhotoImage(file="tk_doorlock/images/num6.png")
num7 = tk.PhotoImage(file="tk_doorlock/images/num7.png")
num8 = tk.PhotoImage(file="tk_doorlock/images/num8.png")
num9 = tk.PhotoImage(file="tk_doorlock/images/num9.png")
star = tk.PhotoImage(file="tk_doorlock/images/asterisk.png")
sharp = tk.PhotoImage(file="tk_doorlock/images/crosshatch.png")
clear = tk.PhotoImage(file="tk_doorlock/images/clear.png")
wrong = tk.PhotoImage(file="tk_doorlock/images/wrong.png")

center_x, center_y = width // 2, height // 2

canvas.create_image(center_x, center_y, image=board)

label_num0 = tk.Label(win, image=num0)
label_num1 = tk.Label(win, image=num1)
label_num2 = tk.Label(win, image=num2)
label_num3 = tk.Label(win, image=num3)
label_num4 = tk.Label(win, image=num4)
label_num5 = tk.Label(win, image=num5)
label_num6 = tk.Label(win, image=num6)
label_num7 = tk.Label(win, image=num7)
label_num8 = tk.Label(win, image=num8)
label_num9 = tk.Label(win, image=num9)
label_star = tk.Label(win, image=star)
label_sharp = tk.Label(win, image=sharp)

label_num0.image = num0
label_num1.image = num1
label_num2.image = num2
label_num3.image = num3
label_num4.image = num4
label_num5.image = num5
label_num6.image = num6
label_num7.image = num7
label_num8.image = num8
label_num9.image = num9
label_star.image = star
label_sharp.image = sharp

row1, row2, row3 = center_x - 75, center_x - 20, center_x + 35
column1, column2, column3, column4 = center_y - 90, center_y - 25, center_y + 40, center_y + 110

label_num1.place(x=row1, y=column1)
label_num2.place(x=row2, y=column1)
label_num3.place(x=row3, y=column1)
label_num4.place(x=row1, y=column2)
label_num5.place(x=row2, y=column2)
label_num6.place(x=row3, y=column2)
label_num7.place(x=row1, y=column3)
label_num8.place(x=row2, y=column3)
label_num9.place(x=row3, y=column3)
label_star.place(x=row1, y=column4)
label_num0.place(x=row2, y=column4)
label_sharp.place(x=row3, y=column4)



label_num1.bind("<Button-1>", lambda event, id=1: on_click(id))
label_num2.bind("<Button-1>", lambda event, id=2: on_click(id))
label_num3.bind("<Button-1>", lambda event, id=3: on_click(id))
label_num4.bind("<Button-1>", lambda event, id=4: on_click(id))
label_num5.bind("<Button-1>", lambda event, id=5: on_click(id))
label_num6.bind("<Button-1>", lambda event, id=6: on_click(id))
label_num7.bind("<Button-1>", lambda event, id=7: on_click(id))
label_num8.bind("<Button-1>", lambda event, id=8: on_click(id))
label_num9.bind("<Button-1>", lambda event, id=9: on_click(id))
label_star.bind("<Button-1>", lambda event, id=10: check_password())
label_num0.bind("<Button-1>", lambda event, id=0: on_click(id))
label_sharp.bind("<Button-1>", lambda event, id=11: on_click(id))

enteredPwd = []

win.mainloop()

print("결과 튜플:", enteredPwd)
