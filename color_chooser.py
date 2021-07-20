import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
import serial
import time

#setup window
root = tk.Tk()
root.title("Color Chooser")
root.geometry('500x350')

#Send hexadecimal number to Arduino
def change_color():
    colors = askcolor(title="Tkinter Color Chooser")
    root.configure(bg=colors[1])
    print(colors[1])
    #output is a tuple so convert to a list
    color_list = list(colors)
    #convert to string then bytes
    ser.write(bytes(str(color_list[1]), 'utf-8'))

def window():
    #choose color
    ttk.Button(root, text = "Select Color", command=change_color).grid(column=1,row=5,padx=10,pady=25)
    #exit program
    ttk.Button(root, text = "Quit", command=quit).grid(column=2, row=5, padx=10, pady=25)
    root.mainloop()

if __name__ == "__main__":
    
    #setup communication to Arduino
    try:
        ser = serial.Serial(
        port = "/dev/ttyACM1", #port will change depending what USB port is being used
        baudrate = 9600,
        timeout = 2)
    except:
        print("Error - Could not open USB serial port.")
        print("Exiting")
        time.sleep(2)
        exit()
        
    window()
    
