import tkinter as tk
import datetime


def append_to_csv(filename, data, labels):
    try:
        with open(filename, 'x') as f:
            for label in labels:
                f.write("{},".format(label))
            f.write("\n")

    except FileExistsError:
        pass

    with open(filename, 'a') as f:
        for item in data:
            f.write("{},".format(item))
        f.write("\n")


def create_slider(window, var, label="", min=0, max=100, orientation=tk.VERTICAL):
    slider = tk.Scale(window,
                      variable=var,
                      from_=max,
                      to=min,
                      orient=orientation,
                      label=label)

    return slider


def submit_mood_chart(var_happiness, var_anger, var_sadness, var_anxiety, var_gratitude, var_tiredness, var_period):
    print("Happiness: ", var_happiness)
    print("Anger: ", var_anger)
    print("Sadness: ", var_sadness)
    print("Anxiety: ", var_anxiety)
    print("Gratitude: ", var_gratitude)
    print("Tiredness: ", var_tiredness)
    print("On Period? ", bool(var_period))

    timestamp = datetime.datetime.now()
    date = "{:02d}/{:02d}/{:04d}".format(timestamp.day, timestamp.month, timestamp.year)

    data = [date, var_happiness, var_anger, var_sadness, var_anxiety, var_gratitude, var_tiredness, var_period]
    labels = ["Date, Happiness, Anger, Sadness, Anxiety, Gratitude, Tiredness, On Period"]
    append_to_csv("mood_chart.csv", data, labels)


if __name__ == '__main__':

    root = tk.Tk()
    # root.geometry("500x500")

    greeting = tk.Label(text="Log your mood",
                        foreground="black",
                        background="white")
    greeting.pack()

    frame = tk.Frame(root)

    var_happiness = tk.IntVar()
    var_anger = tk.IntVar()
    var_sadness = tk.IntVar()
    var_anxiety = tk.IntVar()
    var_gratitude = tk.IntVar()
    var_tiredness = tk.IntVar()
    var_period = tk.IntVar()

    slider_happiness = create_slider(root, var_happiness, "Happiness").pack(side=tk.LEFT)
    slider_anger = create_slider(root, var_anger, "Anger").pack(side=tk.LEFT)
    slider_sadness = create_slider(root, var_sadness, "Sadness").pack(side=tk.LEFT)
    slider_anxiety = create_slider(root, var_anxiety, "Anxiety").pack(side=tk.LEFT)
    slider_gratitude = create_slider(root, var_gratitude, "Gratitude").pack(side=tk.LEFT)
    slider_tiredness = create_slider(root, var_tiredness, "Tiredness").pack(side=tk.LEFT)

    button_period = tk.Radiobutton(root, text="On Period", variable=var_period, value=1).pack(side=tk.LEFT)

    button = tk.Button(text="Submit Mood Report",
                       width=25,
                       height=3,
                       bg="#34A2FE",
                       fg="black",
                       command=lambda: submit_mood_chart(var_happiness.get(),
                                                         var_anger.get(),
                                                         var_sadness.get(),
                                                         var_anxiety.get(),
                                                         var_gratitude.get(),
                                                         var_tiredness.get(),
                                                         var_period.get()))
    button.pack(side=tk.BOTTOM)

    root.mainloop()