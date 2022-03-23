from datetime import datetime

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import csv

from matplotlib.dates import DateFormatter

session_attempts = []
percentages_correct = []
array_of_questions = []


def find_stats(stats_file):
    with open(stats_file) as csvfile:
        if session_attempts:
            session_attempts.clear()
            percentages_correct.clear()
            array_of_questions.clear()
        plots = csv.reader(csvfile, delimiter=',')
        # In order to assign the first prev_date
        START_DATE = "0-0-0"

        prev_date = START_DATE
        sum_of_percents = 0
        num_of_quizzes = 0
        num_of_questions = 0
        for row in plots:
            cur_date = row[2]
            # This is to make sure we include the first line of data
            if prev_date == START_DATE:
                prev_date = cur_date
            # If we are still on the same date add the values but don't append
            if prev_date == cur_date:
                sum_of_percents += float(row[1])
                num_of_quizzes += 1
                num_of_questions += int(row[0])
            else:
                # Appending the previous date data to the graph
                average = sum_of_percents/num_of_quizzes
                array_of_questions.append(num_of_questions)
                percentages_correct.append(average)
                session_attempts.append(datetime.strptime(prev_date, "%Y-%m-%d"))
                sum_of_percents = 0
                num_of_quizzes = 0
                num_of_questions = 0
                # Adding the current date data to the calculations for the date
                sum_of_percents += float(row[1])
                num_of_quizzes += 1
                num_of_questions += int(row[0])
                prev_date = cur_date
        # Adding the last value (or group of values to the graph
        average = sum_of_percents / num_of_quizzes
        array_of_questions.append(num_of_questions)
        percentages_correct.append(average)
        session_attempts.append(datetime.strptime(prev_date, "%Y-%m-%d"))


def get_plot(window, title):
    window.title("User Stats")
    figure1 = plt.Figure(figsize=(6, 5), dpi=100)
    figure1.suptitle(title)
    sub_plot = figure1.add_subplot(111)

    sub_plot.plot(session_attempts, percentages_correct, color='g', linestyle='dashed', marker='o',
                  label="Percent Correct")
    sub_plot.set_xlabel('Session Date')
    sub_plot.set_ylabel('Percentage Correct')

    # Used to format my axis
    date_form = DateFormatter("%m-%d")
    sub_plot.xaxis.set_major_formatter(date_form)
    figure1.autofmt_xdate()

    # Used to add number of questions to the graph
    for attempt, percentage, question_count in zip(session_attempts, percentages_correct, array_of_questions):
        sub_plot.annotate(str(question_count) + " Qs", xy=(attempt, percentage + .1))

    sub_plot.grid()
    sub_plot.legend()

    data_plot = FigureCanvasTkAgg(figure1, master=window)
    return data_plot
