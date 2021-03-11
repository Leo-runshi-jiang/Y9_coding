import requests
import time
import json
import tkinter as tk
import random
from tkinter import ttk

auth_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjRlMDRjMWRkLWY3ODQtNDMwMi05NWVhLTM0YzNjNzhmOTc5MCIsImlhdCI6MTYxNTE3NjM2Nywic3ViIjoiZGV2ZWxvcGVyL2ZhZjQ1MzlkLTFhYmYtNWMyNC1jZDBlLTVmY2FlZDJlYTBlYSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTg0LjE0Ny4yMzMuNTYiXSwidHlwZSI6ImNsaWVudCJ9XX0.SOwZMKazT935RA7-NLzKsVw-akWZQmYX5-XxubCSSK-WTvxPPpTWkOXH6zRxPaaOjV8gpE5r_4vqkOznFrX7CA"
auth_key_brawlify = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJicmF3bGlmeS5jb20iLCJhdWQiOiJicmF3bGlmeS5jb20iLCJzdWIiOiI3NzUxNDQ5MTIwNzY4MDAwMjAiLCJpYXQiOjE2MTQwODk2MzQsImp0aSI6Im96MzBWRkVpdGZobnExZk9ab2lDdkZVZWR3dU1EWFB6MWNIQ1Jwdm14cEVuU1I0dmhNMVJXcDR5QTJkRDVzSEk1azZmQmxiODlMNXdiV3NkSGJaakNZNk9RQXJUTmpVVHdDb1c2aDBmVXRHdWdWRE96bEdCVno4SnQzRzdkZVZYM3ZySzZucUtBOUtHZENQV3E5eEwySVhCTkVhOGkxWFFtN0R5SlVtV0RTUjdTTWtLd3N1WUZyZ2dJYnpKYnBjbFltYXVYNGNUMnk1TlppckJZWlVnUVFmUHhuSzh0THN4Y2hQUE9GTU9BcjRla3BzU3gwdEkyZTRlRUxuVnd2Ri0yNzQifQ.o17Qjk1wabKPrJHeKEPmNUhS0iMpdOrG-kmEMlwXkzD-m3H0NWJN9seld2EYJcu5Oxz6b1DnADHv5haQ_cSAOw"
tips=["Please enter in your ID, do not inclued #","Don't use gold in the shop until you maxed all brawlers", "Buying a brawlpass is the best use of your gems", "Do not waste gems on brawlpass progression","When you have most brawlers save up your boxes for when the next bralwer is released", "Git gud"]
#search returns{playerinfo:playerinfo,winrate:winrate,battlelog:battle }


def get_playertag(*args):
	return(IDchoosen.get())

def get_player_info(playertag):
	#get player info
	headers = {'Accept': 'application/json', 'authorization': 'Bearer ' + auth_key}
	playerID = '%' + str(playertag)
	#print(json.loads(requests.get('https://api.brawlstars.com/v1/players/'+playerID, headers=headers).text))
	name = json.loads(requests.get('https://api.brawlstars.com/v1/players/'+playerID, headers=headers).text)["name"]
	trophies = json.loads(requests.get('https://api.brawlstars.com/v1/players/'+playerID, headers=headers).text)["trophies"]
	highesttrophies = json.loads(requests.get('https://api.brawlstars.com/v1/players/'+playerID, headers=headers).text)["highestTrophies"]
	Victories = json.loads(requests.get('https://api.brawlstars.com/v1/players/'+playerID, headers=headers).text)["3vs3Victories"]
	infotext= json.loads(requests.get('https://api.brawlstars.com/v1/players/'+playerID, headers=headers).text)
	solowins = infotext["soloVictories"]
	duowins = infotext["duoVictories"]
	clubname = infotext["club"]["name"]

	playerinfo= str("name: "+name+"\n"+"trophies: "+str(trophies)+"  "+"highest: "+str(highesttrophies)+"\n"+"club: "+clubname+"\n"+"3vs3 Victories: "+str(Victories)+"\n"+"solo Victories: " +str(solowins)+"  "+"duo: "+str(duowins))
	return(playerinfo)

def get_battle_log(playertag):
	#get the battle log
	headers = {'Accept': 'application/json', 'authorization': 'Bearer ' + auth_key}
	playerID = '%' + playertag
	battlelog = requests.get('https://api.brawlstars.com/v1/players/'+playerID+"/battlelog", headers=headers)
	return(battlelog.text)

def get_winrate(playertag):
	battlelog= json.loads(get_battle_log(playertag))

	wins=0
	numshowdown=0
	for i in range(0,21,1):
		if (battlelog["items"][i]["battle"]["mode"]== "soloShowdown"):
			numshowdown=numshowdown+1
			
		elif (battlelog["items"][i]["battle"]["mode"]== "duoShowdown"):
			numshowdown=numshowdown+1
		else:
			if (battlelog["items"][i]["battle"]["result"]=="victory"):
				wins=wins+1
	winrate=int((wins/(20-numshowdown))*100)
	losses=int(20-numshowdown-wins)
	return([winrate,wins,losses])

def get_trophies(playertag):
	playerinformation = json.loads(get_player_info(playertag))
	trophies=playerinformation["trophies"]
	return(str(trophies))

def addbrawlerimg(name,number):
	pass
	'''
	recom1=tk.PhotoImage(file="Images/AMBER.png")
	recom2=tk.PhotoImage(file="Images/COLONEL RUFFS.png")
	recom3=tk.PhotoImage(file="Images/LOU.png")

	slot6brawler1=tk.Label(slot6recom, image=tk.PhotoImage(file="Images/AMBER.png"), width=44, height=44)
	slot6brawler1.pack(side="left")

	slot6brawler2=tk.Label(slot6recom, image=tk.PhotoImage(file="Images/COLONEL RUFFS.png"), width=44, height=44)
	slot6brawler2.pack(side="left")

	slot6brawler3=tk.Label(slot6recom, image=tk.PhotoImage(file="Images/LOU.png"), width=44, height=44)
	slot6brawler3.pack(side="left")
	'''

def opendict(filename):
	#opens file as a dictionary
	file = open(filename, "r")
	readfile = str(file.read())
	dictionary =json.loads(readfile)
	print(dictionary)
	file.close()
	return(dictionary)

def addNewPlayer(playertag):
	userData = open("UserData.txt","r").read().split(', ')
	if (playertag not in userData):
		newList = open("UserData.txt","r").read() + ", " + str(playertag)
		open("UserData.txt","w").write(newList)


def get_event_info():
	headers = {'Accept': 'application/json', 'authorization': 'Bearer ' + auth_key_brawlify}
	eventinfo = requests.get("http://api.brawlapi.com/v1/events", headers=headers)
	return(eventinfo.text)

def get_slot1():
	eventinfo=json.loads(get_event_info())
	mapname=eventinfo["active"][0]["map"]["name"]
	gamemode=str(eventinfo["active"][0]["map"]["gameMode"]["name"])
	bestbrawler1= eventinfo["active"][0]["map"]["stats"][0]["brawler"]
	bestbrawler1winrate= eventinfo["active"][0]["map"]["stats"][0]["winRate"]
	bestbrawler2= eventinfo["active"][0]["map"]["stats"][1]["brawler"]
	bestbrawler2winrate= eventinfo["active"][0]["map"]["stats"][1]["winRate"]
	bestbrawler3= eventinfo["active"][0]["map"]["stats"][2]["brawler"]
	bestbrawler3winrate= eventinfo["active"][0]["map"]["stats"][2]["winRate"]
	return([mapname,gamemode,bestbrawler1,bestbrawler1winrate,bestbrawler2,bestbrawler2winrate,bestbrawler3,bestbrawler3winrate])
def get_slot2():
	eventinfo=json.loads(get_event_info())
	mapname=eventinfo["active"][1]["map"]["name"]
	gamemode=str(eventinfo["active"][1]["map"]["gameMode"]["name"])
	bestbrawler1= eventinfo["active"][1]["map"]["stats"][0]["brawler"]
	bestbrawler1winrate= eventinfo["active"][1]["map"]["stats"][0]["winRate"]
	bestbrawler2= eventinfo["active"][1]["map"]["stats"][1]["brawler"]
	bestbrawler2winrate= eventinfo["active"][1]["map"]["stats"][1]["winRate"]
	bestbrawler3= eventinfo["active"][1]["map"]["stats"][2]["brawler"]
	bestbrawler3winrate= eventinfo["active"][1]["map"]["stats"][2]["winRate"]
	return([mapname,gamemode,bestbrawler1,bestbrawler1winrate,bestbrawler2,bestbrawler2winrate,bestbrawler3,bestbrawler3winrate])

def get_slot3():
	eventinfo=json.loads(get_event_info())
	mapname=eventinfo["active"][3]["map"]["name"]
	gamemode=str(eventinfo["active"][3]["map"]["gameMode"]["name"])
	bestbrawler1= eventinfo["active"][3]["map"]["stats"][0]["brawler"]
	bestbrawler1winrate= eventinfo["active"][3]["map"]["stats"][0]["winRate"]
	bestbrawler2= eventinfo["active"][3]["map"]["stats"][1]["brawler"]
	bestbrawler2winrate= eventinfo["active"][3]["map"]["stats"][1]["winRate"]
	bestbrawler3= eventinfo["active"][3]["map"]["stats"][2]["brawler"]
	bestbrawler3winrate= eventinfo["active"][3]["map"]["stats"][2]["winRate"]
	return([mapname,gamemode,bestbrawler1,bestbrawler1winrate,bestbrawler2,bestbrawler2winrate,bestbrawler3,bestbrawler3winrate])

def get_slot4():
	eventinfo=json.loads(get_event_info())
	mapname=eventinfo["active"][4]["map"]["name"]
	gamemode=str(eventinfo["active"][4]["map"]["gameMode"]["name"])
	bestbrawler1= eventinfo["active"][4]["map"]["stats"][0]["brawler"]
	bestbrawler1winrate= eventinfo["active"][4]["map"]["stats"][0]["winRate"]
	bestbrawler2= eventinfo["active"][4]["map"]["stats"][1]["brawler"]
	bestbrawler2winrate= eventinfo["active"][4]["map"]["stats"][1]["winRate"]
	bestbrawler3= eventinfo["active"][4]["map"]["stats"][2]["brawler"]
	bestbrawler3winrate= eventinfo["active"][4]["map"]["stats"][2]["winRate"]
	return([mapname,gamemode,bestbrawler1,bestbrawler1winrate,bestbrawler2,bestbrawler2winrate,bestbrawler3,bestbrawler3winrate])

def get_slot5():
	eventinfo=json.loads(get_event_info())
	mapname=eventinfo["active"][5]["map"]["name"]
	gamemode=str(eventinfo["active"][5]["map"]["gameMode"]["name"])
	bestbrawler1= eventinfo["active"][5]["map"]["stats"][0]["brawler"]
	bestbrawler1winrate= eventinfo["active"][5]["map"]["stats"][0]["winRate"]
	bestbrawler2= eventinfo["active"][5]["map"]["stats"][1]["brawler"]
	bestbrawler2winrate= eventinfo["active"][5]["map"]["stats"][1]["winRate"]
	bestbrawler3= eventinfo["active"][5]["map"]["stats"][2]["brawler"]
	bestbrawler3winrate= eventinfo["active"][5]["map"]["stats"][2]["winRate"]
	return([mapname,gamemode,bestbrawler1,bestbrawler1winrate,bestbrawler2,bestbrawler2winrate,bestbrawler3,bestbrawler3winrate])

def get_slot6():
	eventinfo=json.loads(get_event_info())
	mapname=eventinfo["active"][6]["map"]["name"]
	gamemode=str(eventinfo["active"][6]["map"]["gameMode"]["name"])
	bestbrawler1= eventinfo["active"][6]["map"]["stats"][0]["brawler"]
	bestbrawler1winrate= eventinfo["active"][6]["map"]["stats"][0]["winRate"]
	bestbrawler2= eventinfo["active"][6]["map"]["stats"][1]["brawler"]
	bestbrawler2winrate= eventinfo["active"][6]["map"]["stats"][1]["winRate"]
	bestbrawler3= eventinfo["active"][6]["map"]["stats"][2]["brawler"]
	bestbrawler3winrate= eventinfo["active"][6]["map"]["stats"][2]["winRate"]
	return([mapname,gamemode,bestbrawler1,bestbrawler1winrate,bestbrawler2,bestbrawler2winrate,bestbrawler3,bestbrawler3winrate])

def getbrawlername(brawlerid):
	headers = {'Accept': 'application/json', 'authorization': 'Bearer ' + auth_key}
	brawlername = requests.get('https://api.brawlstars.com/v1/brawlers/'+brawlerid, headers=headers)
	return(json.loads(brawlername.text)["name"])

def gettips():
  num = random.randint(1,5)
  return(tips[num])

def getplayerIDs():
	userData = open("UserData.txt","r").read().split(', ')
	return(userData)

def mapinfoupdate():

	slot1info=get_slot1()
	slot2info=get_slot2()
	slot3info=get_slot3()
	slot4info=get_slot4()
	slot5info=get_slot5()
	slot6info=get_slot6()

	slot1mapname.config(text=slot1info[0]+"\n")
	slot2mapname.config(text=slot2info[0]+"\n")
	slot3mapname.config(text=slot3info[0]+"\n")
	slot4mapname.config(text=slot5info[0]+"\n")
	slot5mapname.config(text=slot6info[0]+"\n")
	slot6mapname.config(text=slot4info[0]+"\n")

	addbrawlerimg(get_slot1()[2],1)
	addbrawlerimg(get_slot1()[4],2)
	addbrawlerimg(get_slot1()[6],3)

	addbrawlerimg(get_slot2()[2],4)
	addbrawlerimg(get_slot2()[4],5)
	addbrawlerimg(get_slot2()[6],6)

	addbrawlerimg(get_slot3()[2],7)
	addbrawlerimg(get_slot3()[4],8)
	addbrawlerimg(get_slot3()[6],9)

	addbrawlerimg(get_slot4()[2],10)
	addbrawlerimg(get_slot4()[4],11)
	addbrawlerimg(get_slot4()[6],12)

	addbrawlerimg(get_slot5()[2],13)
	addbrawlerimg(get_slot5()[4],14)
	addbrawlerimg(get_slot5()[6],15)

	addbrawlerimg(get_slot6()[2],16)
	addbrawlerimg(get_slot6()[4],17)
	addbrawlerimg(get_slot6()[6],18)


def count(runsearch):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1    # executed every time the wrapped function is called
        return runsearch(*args, **kwargs)
    wrapper.counter = 0         # executed only once in decorator definition time
    return wrapper

@count
def runsearch():
	mapinfoupdate()
	addNewPlayer(get_playertag())

	tipssection.config(text = gettips())
	playerinfotext.config(text= get_player_info(get_playertag()),anchor="w")
	winratetext.config(text = "Winrate: "+str(get_winrate(get_playertag())[0])+"%")
	winlosstext.config(text=str(get_winrate(get_playertag())[1])+" wins\n"+ str(get_winrate(get_playertag())[2])+" losses")
	
root = tk.Tk()
root.config(bg="#434343")
root.title("Brawl Stars API")

gemgrabpng=tk.PhotoImage(file="Images/modes/gemgrab.png")
brawlballpng=tk.PhotoImage(file="Images/modes/brawlball.png")
showdownpng=tk.PhotoImage(file="Images/modes/showdown.png")
siegepng=tk.PhotoImage(file="Images/modes/siege.png")
heistpng=tk.PhotoImage(file="Images/modes/heist.png")
bountypng=tk.PhotoImage(file="Images/modes/bounty.png")
AMBER=tk.PhotoImage(file="Images/AMBER.png")
RUFFS=tk.PhotoImage(file="Images/COLONEL RUFFS.png")
LOU=tk.PhotoImage(file="Images/LOU.png")
MR=tk.PhotoImage(file="Images/MR.png")
BIBI=tk.PhotoImage(file="Images/BIBI.png")
TARA=tk.PhotoImage(file="Images/Tara.png")
ROSA=tk.PhotoImage(file="Images/ROSA.png")
CROW=tk.PhotoImage(file="Images/Crow.png")
SPIKE=tk.PhotoImage(file="Images/SPIKE.png")
JACKY=tk.PhotoImage(file="Images/Jacky.png")
BULL=tk.PhotoImage(file="Images/Bull.png")
SANDY=tk.PhotoImage(file="Images/Sandy.png")


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

tipssection = tk.Label(root, text = "Please enter in your ID, do not inclued #", font=("Helvetica", 15))
tipssection.config(fg = "white", bg = "#434343", anchor="w", padx=20)
tipssection.pack()

divider2 = tk.Label(root)
divider2.config(bg="#434343", height=1, width= 100)
divider2.pack(fill="both")

middleframe = tk.Frame(root)
middleframe.config(bg="#434343")
middleframe.pack()

playerinfoframe = tk.Frame(middleframe)
playerinfoframe.config(bg="#3C78D8")
playerinfoframe.grid(row=0,column=0)

playerinfotitle = tk.Label(playerinfoframe, text = "  Player Info:", font=("Helvetica", 35))
playerinfotitle.config(fg = "white", anchor="w",bg = "#3C78D8",width= 15)
playerinfotitle.pack(fill="both")

playerinfotext = tk.Label(playerinfoframe, font=("Helvetica", 20))
playerinfotext.config(fg="white", anchor="w",bg="#999999")
playerinfotext.pack(fill='both')


middiv = tk.Label(middleframe)
middiv.config(width = 2, bg="#434343")
middiv.grid(row=0,column=1)

winrateframe = tk.Frame(middleframe)
winrateframe.config(padx=-10,bg="#999999")
winrateframe.grid(row=0,column=2)

winratetext = tk.Label(winrateframe, font=("Helvetica", 35))
winratetext.config(fg = "white", anchor="center",bg = "#3C78D8", width = 25)
winratetext.pack()

winlosstext = tk.Label(winrateframe, font=("Helvetica", 50))
winlosstext.config(fg = "white", anchor="center",bg = "#999999")
winlosstext.pack()

battleloggraphframe = tk.Frame(winrateframe)
battleloggraphframe.pack()

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

slot1mapname=tk.Label(slot1recom, font=("Helvetica", 15))
slot1mapname.config(fg="white",bg="#434343",anchor="w")
slot1mapname.pack(side="top")

slot1brawler1=tk.Label(slot1recom, image=AMBER, width=44, height=44)
slot1brawler1.pack(side="left")

slot1brawler2=tk.Label(slot1recom, image=MR, width=44, height=44)
slot1brawler2.pack(side="left")

slot1brawler3=tk.Label(slot1recom, image=RUFFS, width=44, height=44)
slot1brawler3.pack(side="left")

slot2img=tk.Label(recomframe1, image=showdownpng, width=220, height=88)
slot2img.pack(side="left",padx=20)

slot2recom=tk.Frame(recomframe1, bg="#434343")
slot2recom.pack(side="left")

slot2mapname=tk.Label(slot2recom, font=("Helvetica", 15))
slot2mapname.config(fg="white",bg="#434343",anchor="w")
slot2mapname.pack(side="top")

slot2brawler1=tk.Label(slot2recom, image=AMBER, width=44, height=44)
slot2brawler1.pack(side="left")

slot2brawler2=tk.Label(slot2recom, image=BIBI, width=44, height=44)
slot2brawler2.pack(side="left")

slot2brawler3=tk.Label(slot2recom, image=RUFFS, width=44, height=44)
slot2brawler3.pack(side="left")

recomframe2 = tk.Frame(root,bg="#434343")
recomframe2.pack()

slot3img=tk.Label(recomframe2, image=brawlballpng, width=220, height=88)
slot3img.pack(side="left",padx=20)

slot3recom=tk.Frame(recomframe2, bg="#434343")
slot3recom.pack(side="left")

slot3mapname=tk.Label(slot3recom, font=("Helvetica", 15))
slot3mapname.config(fg="white",bg="#434343",anchor="w")
slot3mapname.pack(side="top")

slot3brawler1=tk.Label(slot3recom, image=JACKY, width=44, height=44)
slot3brawler1.pack(side="left")

slot3brawler2=tk.Label(slot3recom, image=ROSA, width=44, height=44)
slot3brawler2.pack(side="left")

slot3brawler3=tk.Label(slot3recom, image=SPIKE, width=44, height=44)
slot3brawler3.pack(side="left")

slot4img=tk.Label(recomframe2, image=bountypng, width=220, height=88)
slot4img.pack(side="left",padx=20)

slot4recom=tk.Frame(recomframe2, bg="#434343")
slot4recom.pack(side="left")

slot4mapname=tk.Label(slot4recom, font=("Helvetica", 15))
slot4mapname.config(fg="white",bg="#434343",anchor="w")
slot4mapname.pack(side="top")

slot4brawler1=tk.Label(slot4recom, image=MR, width=44, height=44)
slot4brawler1.pack(side="left")

slot4brawler2=tk.Label(slot4recom, image=AMBER, width=44, height=44)
slot4brawler2.pack(side="left")

slot4brawler3=tk.Label(slot4recom, image=RUFFS, width=44, height=44)
slot4brawler3.pack(side="left")

recomframe3 = tk.Frame(root,bg="#434343")
recomframe3.pack()

slot5img=tk.Label(recomframe3, image=heistpng, width=220, height=88)
slot5img.pack(side="left",padx=20)

slot5recom=tk.Frame(recomframe3, bg="#434343")
slot5recom.pack(side="left")

slot5mapname=tk.Label(slot5recom, font=("Helvetica", 15))
slot5mapname.config(fg="white",bg="#434343",anchor="w")
slot5mapname.pack(side="top")

slot5brawler1=tk.Label(slot5recom, image=AMBER, width=44, height=44)
slot5brawler1.pack(side="left")

slot5brawler2=tk.Label(slot5recom, image=RUFFS, width=44, height=44)
slot5brawler2.pack(side="left")

slot5brawler3=tk.Label(slot5recom, image=CROW, width=44, height=44)
slot5brawler3.pack(side="left")

slot6img=tk.Label(recomframe3, image=brawlballpng, width=220, height=88)
slot6img.pack(side="left",padx=20)

slot6recom=tk.Frame(recomframe3, bg="#434343")
slot6recom.pack(side="left")

slot6mapname=tk.Label(slot6recom, font=("Helvetica", 15))
slot6mapname.config(fg="white",bg="#434343",anchor="w")
slot6mapname.pack(side="top")

slot6brawler1=tk.Label(slot6recom, image=AMBER, width=44, height=44)
slot6brawler1.pack(side="left")

slot6brawler2=tk.Label(slot6recom, image=BULL, width=44, height=44)
slot6brawler2.pack(side="left")

slot6brawler3=tk.Label(slot6recom, image=SANDY, width=44, height=44)
slot6brawler3.pack(side="left")

mapinfoupdate()
root.mainloop()
