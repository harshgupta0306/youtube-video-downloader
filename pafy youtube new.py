from tkinter import *

import ttkbootstrap as ttk
from tkinter import filedialog

import pafy 
from threading import *

import os


top = ttk.Window(themename="solar")
top.geometry("1000x700")

logo = PhotoImage(file='C:/Users/Hp/Desktop/codes/backup/youtube video downloader/icon/youtube.png')
top.title("Youtube Video Downloader")
top.iconphoto(False,logo)

color =  "#CCCC99"
dark_green = "#666633"
red = "#990033"


def threading():
    # Call work function
    t1=Thread(target=video_url_entered)
    t1.start()
    

        

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location  
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')



path = get_download_path()

yt = None



def entry_1_clicked(e):
    if E1.get().find("please enter url here") != -1 :
        E1.delete(0,END)
    

def update_progress_bar(p):
    progress['value'] = p
    progress.update()


def percentage(remaining, total ):

    pre = float(remaining) /float(total) * float(100)
    return round(pre)

def progress_func(filesize,done,ratio,speed,eta):
    L5.config(text = "<<<<<Downloading>>>>>    ("+str(done//1000000)+"mb/"+str(filesize//1000000)+"mb)   speed(" + str(round(speed))+"kbps)")
    p = percentage(done,filesize)

    update_progress_bar(p)
    
  


def video_url_entered():
    global yt,names
    print(E1.get())
    video_url = E1.get()
    yt = pafy.new(video_url)
    title = yt.title
    L2.config(text=title )

    names=yt.allstreams
    print(names)

    refresh(names)    
    

    


def download_file():
    global yt ,strea    
    if yt !=None:
        L5.grid(row= 7 , columnspan = 3,column= 0, pady=10)
        choice = options.get()
        print(l)
        index = l.index(choice)
     
        download = names[index].download(path,callback=progress_func)
        
        print(" ")
        L5.config(text = "download complete")
    else:
        print("first submit a url")    

def select_path():
    global path 
    file = filedialog.askdirectory(title="select where to download ")
    path = file
    E2.delete(0,END)
    E2.insert(0,path)
    print(path )
    # L5.config(text=path)

def refresh(option):
    global l
    l=[]
    for i in option:
        l.append(str(i))
        print(type(i))
    options['values'] =l

    n.set(options['values'][0])





Grid.rowconfigure(top,0,weight=1)
Grid.columnconfigure(top,0,weight=1)
  
Grid.rowconfigure(top,1,weight=1)
Grid.columnconfigure(top,1,weight=1)

Grid.rowconfigure(top,2,weight=1)
Grid.columnconfigure(top,2,weight=1)

Grid.rowconfigure(top,3,weight=1)

Grid.rowconfigure(top,4,weight=1)

Grid.rowconfigure(top,5,weight=1)

Grid.rowconfigure(top,6,weight=1)



# Code to add widgets will go here...




L1 = ttk.Label(top,font=("lucida", 12), text = "Please Enter Youtube Url :")
L1.grid(row=0,column=0,pady=30,padx=10,sticky=E)

L2 = ttk.Label(top,font=("lucida", 12),text ="",anchor=CENTER,wraplength=350,width = 45)
L2.grid(row=1, column=1,pady = 30,sticky="NSEW")


L3=ttk.Label(top,font=("lucida", 12),text ="Title Of The Video :")
L3.grid(row = 1 , column= 0,pady = 30 ,padx=6,sticky=E)

L4 = ttk.Label(top,font=("lucida", 12),text ="Select File :")
L4.grid(row = 3 ,pady = 30,sticky=E,padx=6)

L5 =ttk. Label(top,font=("lucida", 12), text = "",anchor=CENTER)
L5.grid(row= 7 , columnspan = 3,column= 0,pady=10,sticky="NSEW")

 
E1 = ttk.Entry(top, width=50)
E1.grid(row=0,column=1,pady = 30,padx=5,sticky="NSEW",)
E1.bind("<Button-1>",entry_1_clicked)
E1.insert(0,"please enter url here")


E2 = ttk.Entry(top, width=50,)
E2.grid(row=4,column=1,pady = 30,sticky="NSEW")
E2.insert(0,path)



progress = ttk.Progressbar(top, orient = HORIZONTAL,length = 500, mode = 'determinate',style='Striped.Horizontal.TProgressbar')
progress["value"]=0
progress.grid(row = 6,column=0,pady = 5,columnspan=3,sticky="NSEW")
              

B1 = ttk.Button(top, text = "Browse path",command = select_path)
B1.grid(row=4 , columnspan= 1 ,ipady=11,ipadx=12, pady = 30 ,padx = 5,sticky=E)

b2 = ttk.Button(top ,text = "Download", command = download_file)
b2.grid(row = 5 ,column=0,ipady=11,ipadx=12,columnspan=3,pady = 30)

b3 =ttk.Button(top ,text = "Submit Url", command = threading)
b3.grid(row = 0 ,column=2,ipady=11,ipadx=12, sticky=W)

# E1.bind("<Button-2>",video_url_entered)

n = StringVar()
options = ttk.Combobox(top, width =60,style = "success.TCombobox", textvariable = n)

options['values'] = ()
options['state'] = 'readonly'

options.grid(row = 3 , column = 1,pady=30)
options.current()


# h = StringVar()
# quality = ttk.Combobox(top, width =60,style = "success.TCombobox", textvariable = h)

# quality['values'] = ()
# quality['state'] = 'readonly'

# quality.grid(row = 3 , column = 1,pady=30)
# quality.current()

top.mainloop()

