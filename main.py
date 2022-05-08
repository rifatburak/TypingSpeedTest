import tkinter as tk
import tkinter.messagebox
import random
import time
from threading import Thread

# Datas
words_data = ['remember', 'imagine', 'carriage', 'architect', 'revival', 'sentiment', 'employ',
              'enjoy', 'tidy', 'admission', 'daughter', 'presentation', 'report', 'text', 'elbow',
              'publicity', 'communist', 'awful', 'liberal', 'agony', 'know', 'manager', 'flawed',
              'value', 'hardware', 'be', 'waterfall', 'enthusiasm', 'mood', 'activate', 'motif', 'dare',
              'terrify', 'stereotype', 'widen', 'warning', 'match', 'trail', 'slice', 'gaffe', 'expression']

time_left = 60
is_timer_on = False


# Functions


def start_words():
    words_list = [random.choice(words_data) for i in range(12)]
    return words_list


def clear(event):
    if not word_entry.get().isdigit():
        word_entry.delete(0, "end")
        Thread(target=timer).start()


def get_word_and_clear(event):
    global words
    global corrected_word_count
    global corrected_char_count
    if word_entry.get().strip() == words[0]:
        del words[0]
        corrected_char_count += len(words[0])
        corrected_word_count += 1
        words.append(random.choice(words_data))
        word_box.config(text=f'{words[0]} {words[1]} {words[2]}\n'
                             f'{words[3]} {words[4]} {words[5]}\n'
                             f'{words[6]} {words[7]} {words[8]}\n'
                             f'{words[9]} {words[10]} {words[11]}')
        word_entry.delete(0, "end")
        Thread(target=wps_calculator).start()
        Thread(target=cps_calculator).start()


def timer():
    global time_left, is_timer_on, wps, cps
    is_timer_on = True
    while is_timer_on and time_left > -1:
        time_box.config(text=f'Corrected CPS:{cps}  WPS: {wps}  Time Left: {time_left}')
        time.sleep(1)
        time_left -= 1
        if time_left == 0:
            is_timer_on = False
            answer = show_score()

            if answer == 'yes':
                reset()
            elif answer == 'no':
                my_ui.quit()


def wps_calculator():
    global wps
    while is_timer_on and time_left > -1:
        if (60 - time_left) > 0:
            wps = round((corrected_word_count * 60) / (60 - time_left), 2)
            wps = int(wps)
            time.sleep(1)


def cps_calculator():
    global cps
    while is_timer_on and time_left > -1:
        if (60 - time_left) > 0:
            cps = round((corrected_char_count * 60) / (60 - time_left), 2)
            cps = int(cps)
            time.sleep(1)

def reset():
    global words, corrected_word_count, corrected_char_count, wps, cps, time_left, is_timer_on
    is_timer_on = False
    words = start_words()
    corrected_word_count = 0
    corrected_char_count = 0
    wps = 0
    cps = 0
    time_left = 60
    word_box.config(text=f'{words[0]} {words[1]} {words[2]}\n'
                                f'{words[3]} {words[4]} {words[5]}\n'
                                f'{words[6]} {words[7]} {words[8]}\n'
                                f'{words[9]} {words[10]} {words[11]}',
                    width=30)
    time_box.config(text=f'Corrected  CPS:{cps}    WPS: {wps}    Time Left: {time_left}', width=30, height=1)
    word_entry.delete(0, "end")
    word_entry.insert(0, 'click and type the words here')

def show_score():
    message = tkinter.messagebox.askquestion(title='Your Score', message=f'Corrected  CPS:{cps}    WPS: {wps}   Time Left: {time_left} \n'
                                                                         f'Do you want try again ?')
    return message


words = start_words()
corrected_word_count = 0
corrected_char_count = 0
wps = 0
cps = 0


# User interface and config
my_ui = tk.Tk()
my_ui.geometry('800x600')
my_ui.title('Typing Speed Tester')
try_again_button = tk.Button(my_ui, text='Reset', command=reset )
word_entry = tk.Entry()
word_box = tk.Label(my_ui, text=f'{words[0]} {words[1]} {words[2]}\n'
                                f'{words[3]} {words[4]} {words[5]}\n'
                                f'{words[6]} {words[7]} {words[8]}\n'
                                f'{words[9]} {words[10]} {words[11]}',
                    width=30)
word_box.config(font=('Arial', 15))
time_box = tk.Label(my_ui, text=f'Corrected  CPS:{0}    WPS: {0}    Time Left: {time_left}', width=30, height=1)
empty_box_1 = tk.Label(my_ui, text='', width=30, height=5)
empty_box_2 = tk.Label(my_ui, text='', width=30, height=5)
empty_box_3 = tk.Label(my_ui, text='', width=30, height=5)
word_entry.config(width=25, font=('Arial', 20))
word_entry.insert(0, 'click and type the words here')
word_box.grid(row=1, column=3)
empty_box_1.grid(row=2, column=1)
empty_box_2.grid(row=2, column=1)
empty_box_3.grid(row=2, column=1)
time_box.grid(row=2, column=3)
word_entry.grid(row=3, column=3)
try_again_button.grid(row=4, column=3)
word_entry.bind("<Button-1>", clear)
word_entry.bind('<space>', get_word_and_clear)


my_ui.mainloop()
