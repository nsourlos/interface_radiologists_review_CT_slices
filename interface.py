
#Import Libraries
import os
from tkinter import * #Not the best way but that's how I found it online
from PIL import ImageTk, Image

#Path of folder with subfolders with images
data_path="C:/Users/soyrl/Desktop/test_no/"

def Take_input(): #Function to get input from tkinter and save it to txt
    INPUT = inputtxt.get("1.0", "end-1c") #Get input from tkinter window txt prompt
    
    if os.path.isfile(save_path+'.txt'): #If there is already a file with that named saved in that folder
    #This happens if we click 'save' below multiple times
        for i in range(100): #Up to 100 times save a new file instead of replacing the previous one - Helpful in case of errors
            if os.path.isfile(save_path+str(i)+'.txt'):
                pass
            else:
                with open(save_path+str(i)+'.txt', 'w') as f:
                    f.write(INPUT)
                    f.close()
                    break

    else: #If no txt file exists, save it
        with open(save_path+'.txt', 'w') as f:
            f.write(INPUT)
            f.close()


for path,subdir,files in os.walk(data_path): #Loop over that path

    if subdir==[]: #When this is empty we only have files in subfolders and not other subdirectories
        for file in files: #For each file in that subfolder
            if 'txt' not in file: #If it's not one of the newly created txt files below
                save_path=path+'/'+file[:-4] #Get path without the jpg/png ending
    
                #https://www.geeksforgeeks.org/how-to-create-full-screen-window-in-tkinter/
                #https://zetcode.com/tkinter/layout/
                win=Tk() #Initialize tkinter
                win.title(path.split('/')[-1])#'Annotation tool') #title of the tkinter window
                width= win.winfo_screenwidth()
                height= win.winfo_screenheight()
                
                #setting tkinter window size
                win.geometry("%dx%d" % (width, height))
                # win.attributes("-fullscreen", True)  # substitute `Tk` for whatever your `Tk()` object is called
                # win.geometry("600x700+0+0") #Size of that window
        
                #https://stackoverflow.com/questions/23901168/how-do-i-insert-a-jpeg-image-into-a-python-tkinter-window
                #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
                orig_img=Image.open(path+'/'+file) #Open image
                newsize=(768,400) #Size to resize it #was 768,512
                new_img=orig_img.resize(newsize) #Resize image
                img = ImageTk.PhotoImage(new_img) #Convert it to Tkinter compatible version

                #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
                panel = Label(win, image = img) #To display image on Tkinter window

                #https://www.geeksforgeeks.org/python-tkinter-text-widget/
                l = Label(text = file) #To create a txt window
                inputtxt = Text(win, height = 10,
                                width = 25,
                                bg = "light yellow") #Specify dimensions of window and color
    
                l.place(x=520,y=520) 
                Display = Button(win, height = 2,
                                  width = 20,
                                  text ="Save",
                                  command = lambda:Take_input()) #Create button which when clicked executed function to save txt

                #Following needed from Tkinter - The Pack geometry manager packs widgets in rows or columns.
                panel.pack()
                l.pack()
                inputtxt.pack(side=LEFT)#,fill=BOTH,expand=YES)
                Display.pack()
    
                #start the GUI
                mainloop()
