import tkinter as tk
import random
from tkinter import ttk
tips=["Please enter in your ID","Don't use gold in the shop until you maxed all brawlers", "Buying a brawlpass is the best use of your gems", "Do not waste gems on brawlpass progression","When you have most brawlers save up your boxes for when the next bralwer is released", "Git gud"]

def gettips():
  num = random.randint(0,5)
  return(tips[num])

def getplayerIDs():
	return("1111111","22222222")

def get_playertag(*args):
  print(IDchoosen.get())

def runsearch():
  get_playertag()

def get_winrate():
	return("100%")

winrate=get_winrate()
root = tk.Tk()
root.config(bg="#434343")
root.title("Brawl Stars API")

gemgrabpng=tk.PhotoImage(file="Images/modes/gemgrab.png")
brawlballpng=tk.PhotoImage(file="Images/modes/brawlball.png")
showdownpng=tk.PhotoImage(file="Images/modes/showdown.png")
siegepng=tk.PhotoImage(file="Images/modes/siege.png")
heistpng=tk.PhotoImage(file="Images/modes/heist.png")
bountypng=tk.PhotoImage(file="Images/modes/bounty.png")
slot51=tk.PhotoImage(file="Images/AMBER.png")
slot52=tk.PhotoImage(file="Images/COLONEL RUFFS.png")
slot53=tk.PhotoImage(file="Images/LOU.png")

combostyle = ttk.Style()
combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'fieldbackground': 'white',
                                       'background': 'white'
                                       }}}
                         )
combostyle.theme_use('combostyle')

btnstyle = ttk.Style()
 
btnstyle.configure('TButton', font =
               ("Helvetica", 26),
                    borderwidth = '2',
                    relief="solid",
                    background= "#999999",
                    foreground = "white")

divider1 = tk.Label(root)
divider1.config(bg="#434343", height=1, width= 100)
divider1.pack(fill="both")

topframe = tk.Frame(root, bg="#3C78D8")
topframe.pack()

title = tk.Label(topframe, text = "BRAWL TRACKER", font=("Helvetica", 50))
title.config(fg = "white", bg = "#3C78D8", anchor="w", padx=20)
title.grid(row=0, column=0)

playeridtext = tk.Label(topframe, text = "Player ID:", font=("Helvetica", 26), borderwidth=2, relief="solid")
playeridtext.config(fg = "white", bg = "#999999", anchor="w", padx=10)
playeridtext.grid(row=0, column=1)

n = tk.StringVar() 
IDchoosen = ttk.Combobox(topframe, width = 10, height = 10, textvariable = n, font=("Helvetica", 30)) 
IDchoosen['values'] = getplayerIDs()
IDchoosen.grid(row=0, column=2)

search = ttk.Button(topframe, text = "Search")
search.config(command=runsearch)
search.grid(row=0, column=3)

divider15 = tk.Label(root)
divider15.config(bg="#434343", height=1, width= 100)
divider15.pack(fill="both")

tipssection = tk.Label(root, text = gettips(), font=("Helvetica", 15))
tipssection.config(fg = "white", bg = "#434343", anchor="w", padx=20)
tipssection.pack()

divider2 = tk.Label(root)
divider2.config(bg="#434343", height=1, width= 100)
divider2.pack(fill="both")

middleframe = tk.Frame(root)
middleframe.config(bg="#434343")
middleframe.pack()

playerinfoframe = tk.Frame(middleframe)
playerinfoframe.config(padx=10, bg="#999999")
playerinfoframe.grid(row=0,column=0)

playerinfotitle = tk.Label(playerinfoframe, text = "Player Info:", font=("Helvetica", 35))
playerinfotitle.config(fg = "white", anchor="w",bg = "#999999",width= 15)
playerinfotitle.pack()

playerinfotext = tk.Label(playerinfoframe)#, text= playername+"\n"+playertrophies+"\n")


middiv = tk.Label(middleframe)
middiv.config(width = 2, bg="#434343")
middiv.grid(row=0,column=1)

winrateframe = tk.Frame(middleframe)
winrateframe.config(padx=-10,bg="#999999")
winrateframe.grid(row=0,column=2)

winratetext = tk.Label(winrateframe, font=("Helvetica", 35), text = "Winrate:")#, text = "Winrate: "+winrate, font=("Helvetica", 35))
winratetext.config(fg = "white", anchor="center",bg = "#999999", width = 25)
winratetext.pack()

battleloggraphframe = tk.Frame(winrateframe)
battleloggraphframe.pack()

test=tk.Label(battleloggraphframe, text = "Hi test")
test.pack()

divider3 = tk.Label(root)
divider3.config(bg="#434343", height=1, width= 100)
divider3.pack(fill="both")


recommandtitle = tk.Label(root, text = "Recommanded Brawlers", font=("Helvetica", 35))
recommandtitle.config(fg = "white", bg = "#999999", anchor="w", width = 42, padx=10)
recommandtitle.pack()

divider4 = tk.Label(root)
divider4.config(bg="#434343", height=1, width= 100)
divider4.pack()

recomframe1 = tk.Frame(root,bg="#434343")
recomframe1.pack()

slot1img=tk.Label(recomframe1, image=gemgrabpng, width=220, height=88)
slot1img.pack(side="left",padx=20)

slot1recom=tk.Frame(recomframe1, bg="#434343")
slot1recom.pack(side="left")

slot1mapname=tk.Label(slot1recom, text="Snaked Assault\n", font=("Helvetica", 15))
slot1mapname.config(fg="white",bg="#434343",anchor="w")
slot1mapname.pack(side="top")

slot1brawler1=tk.Label(slot1recom, image=slot51, width=44, height=44)
slot1brawler1.pack(side="left")

slot1brawler2=tk.Label(slot1recom, image=slot52, width=44, height=44)
slot1brawler2.pack(side="left")

slot1brawler3=tk.Label(slot1recom, image=slot53, width=44, height=44)
slot1brawler3.pack(side="left")

slot2img=tk.Label(recomframe1, image=showdownpng, width=220, height=88)
slot2img.pack(side="left",padx=20)

slot2recom=tk.Frame(recomframe1, bg="#434343")
slot2recom.pack(side="left")

slot2mapname=tk.Label(slot2recom, text="Snaked Assault\n", font=("Helvetica", 15))
slot2mapname.config(fg="white",bg="#434343",anchor="w")
slot2mapname.pack(side="top")

slot2brawler1=tk.Label(slot2recom, image=slot51, width=44, height=44)
slot2brawler1.pack(side="left")

slot2brawler2=tk.Label(slot2recom, image=slot52, width=44, height=44)
slot2brawler2.pack(side="left")

slot2brawler3=tk.Label(slot2recom, image=slot53, width=44, height=44)
slot2brawler3.pack(side="left")

recomframe2 = tk.Frame(root,bg="#434343")
recomframe2.pack()

slot3img=tk.Label(recomframe2, image=brawlballpng, width=220, height=88)
slot3img.pack(side="left",padx=20)

slot3recom=tk.Frame(recomframe2, bg="#434343")
slot3recom.pack(side="left")

slot3mapname=tk.Label(slot3recom, text="Snaked Assault\n", font=("Helvetica", 15))
slot3mapname.config(fg="white",bg="#434343",anchor="w")
slot3mapname.pack(side="top")

slot3brawler1=tk.Label(slot3recom, image=slot51, width=44, height=44)
slot3brawler1.pack(side="left")

slot3brawler2=tk.Label(slot3recom, image=slot52, width=44, height=44)
slot3brawler2.pack(side="left")

slot3brawler3=tk.Label(slot3recom, image=slot53, width=44, height=44)
slot3brawler3.pack(side="left")

slot4img=tk.Label(recomframe2, image=bountypng, width=220, height=88)
slot4img.pack(side="left",padx=20)

slot4recom=tk.Frame(recomframe2, bg="#434343")
slot4recom.pack(side="left")

slot4mapname=tk.Label(slot4recom, text="Snaked Assault\n", font=("Helvetica", 15))
slot4mapname.config(fg="white",bg="#434343",anchor="w")
slot4mapname.pack(side="top")

slot4brawler1=tk.Label(slot4recom, image=slot51, width=44, height=44)
slot4brawler1.pack(side="left")

slot4brawler2=tk.Label(slot4recom, image=slot52, width=44, height=44)
slot4brawler2.pack(side="left")

slot4brawler3=tk.Label(slot4recom, image=slot53, width=44, height=44)
slot4brawler3.pack(side="left")

recomframe3 = tk.Frame(root,bg="#434343")
recomframe3.pack()

slot5img=tk.Label(recomframe3, image=heistpng, width=220, height=88)
slot5img.pack(side="left",padx=20)

slot5recom=tk.Frame(recomframe3, bg="#434343")
slot5recom.pack(side="left")

slot5mapname=tk.Label(slot5recom, text="Snaked Assault\n", font=("Helvetica", 15))
slot5mapname.config(fg="white",bg="#434343",anchor="w")
slot5mapname.pack(side="top")

slot5brawler1=tk.Label(slot5recom, image=slot51, width=44, height=44)
slot5brawler1.pack(side="left")

slot5brawler2=tk.Label(slot5recom, image=slot52, width=44, height=44)
slot5brawler2.pack(side="left")

slot5brawler3=tk.Label(slot5recom, image=slot53, width=44, height=44)
slot5brawler3.pack(side="left")

slot6img=tk.Label(recomframe3, image=siegepng, width=220, height=88)
slot6img.pack(side="left",padx=20)

slot6recom=tk.Frame(recomframe3, bg="#434343")
slot6recom.pack(side="left")

slot6mapname=tk.Label(slot6recom, text="Snaked Assault\n", font=("Helvetica", 15))
slot6mapname.config(fg="white",bg="#434343",anchor="w")
slot6mapname.pack(side="top")

slot6brawler1=tk.Label(slot6recom, image=slot51, width=44, height=44)
slot6brawler1.pack(side="left")

slot6brawler2=tk.Label(slot6recom, image=slot52, width=44, height=44)
slot6brawler2.pack(side="left")

slot6brawler3=tk.Label(slot6recom, image=slot53, width=44, height=44)
slot6brawler3.pack(side="left")
'''
for i in range(0,20,1):
	if winlist[i]="1":
		battlelogresults+i=tk.canvas 
'''


root.mainloop()