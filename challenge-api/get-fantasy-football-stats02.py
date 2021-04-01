#!/usr/bin/python3
"""RZFeeser || exploring a catfact api
In this example, we query a fantasy football API source and output formatted data.
API Source:
https://fantasy.premierleague.com/api/bootstrap-static/
"""

import requests
from openpyxl import Workbook
import time

API = 'https://fantasy.premierleague.com/api/bootstrap-static/'

def main():
    # Pull data from API
    r = requests.get(API)

    # determine if r is a "200"
    if r.status_code != 200:
        print(r.status_code)
        print(r.json())
        exit()

    # we want to grab the data off the 200 response
    ffdata = r.json()
   
    #Create workbook object
    wb = Workbook()
    wbsheet = wb.active
    wbsheet.title='FF Dream Team Stats'

    #Add titles in the first row of each column
    wbheaders = ('Name', 'Minutes', 'GoalsScored', 'Assists', 'InDreamTeam', 'PointsPerGame')
    wbsheet.append(wbheaders)

    for playername in ffdata['elements']:
        webname = playername.get("web_name")
        gameminutes = playername.get("minutes")
        goalsscored = playername.get("goals_scored")
        assists = playername.get("assists")
        indreamteam = playername.get("in_dreamteam")
        pointspergame = playername.get("points_per_game")
        
        if indreamteam:
            print(" Name: " + webname + ", In Dream Team: " + str(indreamteam))
            print(" Goals scored: " + str(goalsscored) + ", Assists: " + str(assists))
            print(" Minutes: " + str(gameminutes) + ", Points per Game: " + pointspergame + "\n")
            
            #Loop to set the value of each cell
            for i in range(11):
                wbrow = (webname, gameminutes, goalsscored, assists, indreamteam, pointspergame)
                wbsheet.append(wbrow)

    timestr = time.strftime("%Y%m%d-%H%M%S")
    print("\nTime Stamp is: " + timestr + "\n")
    #Finally, save the file and give it a name
    wb.save("/home/student/mycode/challenge-api/FF_Dream_Team_Stats__" + timestr + ".xlsx")

if __name__ == "__main__":
    main()
