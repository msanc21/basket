from flask import render_template, request, url_for
from .__init__ import mongo
from app import app

    
@app.route('/')
@app.route('/index')
@app.route('/players')
#Display initial home page showing all player in the 2018-2019 season
def index():
    q=mongo.db.NBA18_19.find()
    q=list(q)
    header='NBA Season 2018-2019 Totals'
    return render_template('index.html',q=q,header=header)  

#Generate a search query based on team name and generate page with players stats from that team 
#fix this function to take in [player],[age],[team]
@app.route('/teams/<teamname>')
def teams(teamname):
    
    team=mongo.db.NBA18_19.find({"team":teamname })   
    team=list(team)
    print(len(team))
    return render_template('index.html', q=team, header=teamname) 
   
@app.route('/teams')
def team_list():
    teams=mongo.db.NBA18_19.distinct('team')
    teams=list(teams)
    return render_template('teamlist.html',teams=teams)

@app.route('/players/<player_name>')
def player(player_name):
    print(player_name)
    player=mongo.db.NBA18_19.find({"name":player_name})   
    player=list(player)
    return render_template('index.html', q=player, header=player_name) 

@app.route('/leaders')
def leaders():
    return render_template('leaders.html')



