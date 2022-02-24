from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import csv

x = []
y = []

def find_stats():
    with open('Output_Files/user_percentages.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        # In order to assign the first prev_date
        START_DATE = "0-0-0"

        itr = iter(plots)
        prev_date = START_DATE
        sum_of_percents = 0
        num_of_quizzes = 0
        for row in plots:
            cur_date = row[2]
            print(cur_date)
            print(str(row) + ": This is I")
            # This is to make sure we include the first line of data
            if prev_date == START_DATE:
                prev_date = cur_date
            # If we are still on the same date add the values but don't append
            if prev_date == cur_date:
                sum_of_percents += float(row[1])
                num_of_quizzes += 1
            else:
                # Appending the previous date data to the graph
                average = sum_of_percents/num_of_quizzes
                y.append(average)
                x.append(prev_date)
                sum_of_percents = 0
                num_of_quizzes = 0
                # Adding the current date data to the calculations for the date
                sum_of_percents += float(row[1])
                num_of_quizzes += 1
                prev_date = cur_date
        # Adding the last value (or group of values to the graph
        average = sum_of_percents / num_of_quizzes
        y.append(average)
        x.append(prev_date)


def get_plot(window):
    window.title("User Stats")
    figure1 = plt.Figure(figsize=(6, 5), dpi=100)
    sub_plot = figure1.add_subplot(111)
    sub_plot.plot(x, y, color='g', linestyle='dashed', marker='o', label="Percent Correct")
    sub_plot.set_xlabel('Attempts')
    sub_plot.set_ylabel('Percentage Correct')

    sub_plot.grid()
    sub_plot.legend()

    data_plot = FigureCanvasTkAgg(figure1, master=window)
    return data_plot
