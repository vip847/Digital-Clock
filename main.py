from tkinter import *
from tkinter.ttk import *
from time import strftime
# you might set these variable to your ideal output
FONT_SIZE = 150
FONT_STYLE = "ds-digital" # set the font style
TEXT_COLOR = "lightgreen" # set the text color
BACKGROUND_COLOR = "black" # set the background color
TIME_FORMAT12 = "%I:%M:%S %p" # comment out this line for displaying 12 hours time format
TIME_FORMAT24 = "%H:%M:%S" # comment out this line for displaying 24 hours time format
interface = Tk()
interface.title("Digital Clock") # title of the window
interface.state("zoomed") # display the window in full screen
interface.configure(bg = BACKGROUND_COLOR) # background color
def display_time():
    time_text1 = strftime(TIME_FORMAT12) # define the time format
    time_label = Label(interface, font = (FONT_STYLE, FONT_SIZE), background = BACKGROUND_COLOR, foreground = TEXT_COLOR)
    time_label.config(text = time_text1) # set the text tag
    time_label.after(1000, display_time) # update the screen every 1 second, second argument receive non-argument function
    time_label.place(relx = 0.5, rely = 0.20, anchor = "center") 
    time_text = strftime(TIME_FORMAT24) # define the time format
    time_label = Label(interface, font = (FONT_STYLE, FONT_SIZE), background = BACKGROUND_COLOR, foreground = TEXT_COLOR)
    time_label.config(text = time_text) # set the text tag
    time_label.after(1000, display_time) # update the screen every 1 second, second argument receive non-argument function
    time_label.place(relx = 0.5, rely = 0.50, anchor = "center") 
def display_date():
    date = strftime("%d-%m-%Y") # define the date format
    date_label = Label(interface, font = (FONT_STYLE, FONT_SIZE), background = BACKGROUND_COLOR, foreground = TEXT_COLOR)
    date_label.config(text = date) # set the text tag
    date_label.after(1000, display_date) # update the screen every 1 second, second argument receive non-argument function
    date_label.place(relx = 0.5, rely = 0.80, anchor = "center")   
        # relx, rely − Horizontal and vertical offset as a float between 0.0 and 1.0, as a fraction of the height and width of the parent widget.
        # anchor − The exact spot of widget other options refer to
display_time() # call the time function
display_date() # call the date function
mainloop() # Execute Tkinter