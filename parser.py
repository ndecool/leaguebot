from time import *
import leaguepedia_parser
import os
playerb=[]
playerr=[]
games = leaguepedia_parser.get_games("LFL/2020 Season/Summer Season")
lenght = len(games)
for   y in range(1): 
	#Recupération games
	result = leaguepedia_parser.get_game_details(games[y])
	teamblue = result["teams"]["BLUE"]["players"]
	lenghtblue  = (len(teamblue))
	for   x in range(lenghtblue):
		temp = teamblue[x]
		champname=temp["championName"]
		playername=temp["uniqueIdentifiers"]["leaguepedia"]["name"]
		playerb.insert(x,champname+" ("+playername+")")
	teamred = result["teams"]["RED"]["players"]
	lenghtred  = (len(teamred))
	for   x in range(lenghtred):
		temp = teamred[x]
		champname=temp["championName"]
		playername=temp["uniqueIdentifiers"]["leaguepedia"]["name"]
		playerr.insert(x,champname+" ("+playername+")")
	#Nom des teams
	teamnameblue = result["teams"]["BLUE"]["name"]
	teamnamered = result["teams"]["RED"]["name"]
	
	# nom team gagnante
	if result["winner"]=='BLUE':
		win=teamnameblue
	else:
		win=teamnamered
	
	#Temps
	timegame = strftime('%M'+'min'+' %S'+'s', gmtime(result["duration"]))
	
	#Affichage
	#Compteur
	compteur = y+1
	print(str(compteur)+"/"+str(lenght))
	out='"'+teamnameblue+" VS "+teamnamered+","+playerb[0]+" | "+playerr[0]+","+playerb[1]+" | "+playerr[1]+","+playerb[2]+" | "+playerr[2]+","+playerb[3]+" | "+playerr[3]+","+playerb[4]+" | "+playerr[4]+","+"Victoire de "+win+" en "+timegame+","+"VOD : "+result["vod"]+","+"Match History :"+result["sources"]["leaguepedia"]["matchHistoryUrl"]+'"'
	cmd = "/usr/bin/python3 /home/ndecool/leaguebot/test.py "+out
	os.system(cmd)