def laba13_1():

    import tkinter as tk
    import random

    def show_thank_you():
        thank_you_label.pack()
        cat_image_label.pack()
        yes_button.pack_forget()
        no_button.pack_forget()

    def move_no_button():
        x = random.randint(0, window.winfo_width() - no_button.winfo_width())
        y = random.randint(0, window.winfo_height() - no_button.winfo_height())
        no_button.place(x=x, y=y)

    window = tk.Tk()
    window.title("Поставите автоматом 4?")
    window.geometry("500x500")

    question_label = tk.Label(window, text="Поставите автоматом 4?")
    yes_button = tk.Button(window, text="Да", command=show_thank_you)
    no_button = tk.Button(window, text="Нет", command=move_no_button)
    thank_you_label =tk.Label(window, text="СПАСИБО")
    cat_image = tk.PhotoImage(file="cat.png")
    cat_image_label = tk.Label(window, image=cat_image)

    question_label.pack()
    yes_button.pack(side=tk.LEFT)
    no_button.pack(side=tk.RIGHT)

    window.mainloop()


def laba13_2():

    import tkinter as tk
    import requests
    import json

    from io import BytesIO
    from PIL import Image, ImageTk

    app = tk.Tk()
    app.title("APOD")
    app.geometry("500x500")

    last_label = None

    def show_pic():
        global last_label
        if last_label:
            last_label.destroy()

        f = "https://api.nasa.gov/planetary/apod?api_key=uD1Hru9s42KTGJd3HM8YzlscMhOVlDcWPKgWYw4P&count=1"
        data = requests.get(f)

        tt = json.loads(data.text)
        url = tt[0]["url"]

        response = requests.get(url)
        img = Image.open(BytesIO(response.content))

        test = ImageTk.PhotoImage(img)

        label = tk.Label(image=test)
        label.image = test
        label.grid(row=0, column=0, sticky="nsew")
        label.place(x=0, y=15)

        last_label = label

    button = tk.Button(app, text="Показать картинку (:0)", command=show_pic)
    button.pack()

    app.mainloop()