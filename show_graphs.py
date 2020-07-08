import matplotlib.pyplot as plt


def display_stats(filename):
    with open(filename, 'r') as f:
        i = 0
        data = {}
        labels = []
        dates = []
        color = {}
        num_labels = 0

        months = {1: "Jan",
                  2: "Feb",
                  3: "Mar",
                  4: "Apr",
                  5: "May",
                  6: "Jun",
                  7: "Jul",
                  8: "Aug",
                  9: "Sep",
                  10: "Oct",
                  11: "Nov",
                  12: "Dec"}

        for line in f:
            terms = line.split(',')
            date = terms[0]

            if i == 0:
                num_labels = len(terms) - 2
                labels = terms[1:-1]

                for k in range(num_labels):
                    data[k] = []
                    color[k] = []

                i += 1

            else:
                for i in range(num_labels):
                    data[i].append(int(terms[i + 1]))
                    if terms[-1].split('\n')[0] == '1':  # on period
                        color[i].append("r")
                    else:
                        color[i].append("k")
                d = date.split('/')
                dates.append("{} {}".format(months[int(d[1])], d[0]))

        m = 2
        n = 3
        fig, axes = plt.subplots(m, n)
        fig.suptitle("Mood Chart", fontsize=16)
        for k in range(num_labels):
            i = int(k / n)
            j = int(k % n)
            axes[i, j].scatter(dates, data[k], color=color[k], zorder=2)
            axes[i, j].plot(dates, data[k], 'k-', zorder=1)
            axes[i, j].set_ylabel("Percentage")
            axes[i, j].set_title(labels[k])

        fig.canvas.manager.full_screen_toggle()
        fig.show()


if __name__ == "__main__":
    display_stats("mood_chart.csv")
    input("Enter any key to exit ")
