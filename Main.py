from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import filedialog
import numpy as np
from tkinter.filedialog import askopenfilename
import numpy as np 
from CannyEdgeDetection import *
import skimage
import matplotlib.image as mpimg
import os
import scipy.misc as sm
import cv2
import matplotlib.pyplot as plt 


main = tkinter.Tk()
main.title("Green Light Control System")
main.geometry("1300x1200")

global filename
global refrence_pixels
global sample_pixels
lane_value=1
def print_selected_value():
    selected_value = option_var.get()
    # print("Selected value:", selected_value,lane_value)

def option_selected(*args):
    global lane_value
    signal_value=option_var.get()
    lane_value=int(signal_value)
    # print("signal value",lane_value)
def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

def uploadTrafficImage():
    global filename
    filename = filedialog.askopenfilename(initialdir="images")
    pathlabel.config(text=filename)

def visualize(imgs, format=None, gray=False):
    j = 0
    plt.figure(figsize=(20, 40))
    for i, img in enumerate(imgs):
        if img.shape[0] == 3:
            img = img.transpose(1,2,0)
        plt_idx = i+1
        plt.subplot(2, 2, plt_idx)
        if j == 0:
            plt.title('Sample Image')
            plt.imshow(img, format)
            j = j + 1
        elif j > 0:
            plt.title('Reference Image')
            plt.imshow(img, format)
            
    plt.show()
    
def applyCanny():
    imgs = []
    img = mpimg.imread(filename)
    img = rgb2gray(img)
    imgs.append(img)
    edge = CannyEdgeDetector(imgs, sigma=1.4, kernel_size=5, lowthreshold=0.09, highthreshold=0.20, weak_pixel=100)
    imgs = edge.detect()
    for i, img in enumerate(imgs):
        if img.shape[0] == 3:
            img = img.transpose(1,2,0)
    cv2.imwrite("gray/test.png",img)
    temp = []
    img1 = mpimg.imread('gray/test.png')
    img2 = mpimg.imread('gray/refrence.png')
    temp.append(img1)
    temp.append(img2)
    visualize(temp)

def pixelcount():
    global refrence_pixels
    global sample_pixels
    img = cv2.imread('gray/test.png', cv2.IMREAD_GRAYSCALE)
    sample_pixels = np.sum(img == 255)
    img = cv2.imread('gray/refrence.png', cv2.IMREAD_GRAYSCALE)
    refrence_pixels = np.sum(img == 255)
    messagebox.showinfo("Pixel Counts", "Total Refrence White Pixels Count : "+str(sample_pixels)+"\nTotal Sample White Pixels Count : "+str(refrence_pixels))


def timeAllocation():
    avg=sample_pixels
    print(sample_pixels)
    cnt=0
    file = open("Previous_data.txt", 'r')
    lines = file.readlines()
    n=len(lines)
    i=0
    while i<n:
        if avg>=int(lines[i]):
            cnt=cnt+1
        i=i+1
    if cnt==4:
        messagebox.showinfo("Time Allocation ","very High Traffic Density"+"\n60 second")
    elif cnt==3:
        messagebox.showinfo("Time Allocation ","High Traffic Density"+"\n50 second")
    elif cnt==2:
        messagebox.showinfo("Time Allocation ","Medium Traffic Density"+"\n40 second")
    else:
        messagebox.showinfo("Time Allocation ","Low Traffic Density"+"\n30 second")
    # print(lines)
    # print(lane_value)
    # print(avg)
    lines[lane_value-1]=str(avg)+'\n'
    print(lines)
    with open("Previous_data.txt", 'w') as file:
        file.writelines(lines)
    file.close()                 
        

def exit():
    main.destroy()
    

    
# main = Tk()
main.title("Green Light Control System")
main.geometry("1300x1200")

option_var = StringVar(main)
option_var.set("Select Lane Value ")  # Set default value
# option_var.place(x=50,y=10)
option_menu = OptionMenu(main, option_var, "1", "2", "3", "4", command=option_selected)
# option_menu.place(x=50, y=50)  # Adjust placement
option_menu.config(font=('times', 14, 'bold'))  # Set font size
option_menu.pack()

font1 = ('times', 14, 'bold')
upload = Button(main, text="Upload Traffic Image", command=uploadTrafficImage)
upload.place(relx=0.437, y=50)
upload.config(font=font1)  

pathlabel = Label(main)
pathlabel.config(bg='orange', fg='white')  
pathlabel.config(font=font1)           
pathlabel.place(relx=0.437, y=100)


process = Button(main, text="Image Preprocessing Using Canny Edge Detection", command=applyCanny)
process.place(relx=0.437, y=200)
process.config(font=font1)

count = Button(main, text="White Pixel Count", command=pixelcount)
count.place(relx=0.437, y=250)
count.config(font=font1)

count = Button(main, text="Calculate Green Signal Time Allocation", command=timeAllocation)
count.place(relx=0.437, y=300)
count.config(font=font1)

exitButton = Button(main, text="Exit", command=exit)
exitButton.place(relx=0.437, y=350)

exitButton.config(font=font1)

main.config(bg='white')
main.mainloop()
