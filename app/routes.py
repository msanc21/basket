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
    assist=mongo.db.NBA18_19.find({"assists":{"$gt":1}}).sort([("assists",-1)])
    assist=list(assist)
    
    three=mongo.db.NBA18_19.find({"made_three_point_field_goals":{"$gt":1}}).sort([("made_three_point_field_goals",-1)])
    three=list(three)
    
    steals=mongo.db.NBA18_19.find({"steals":{"$gt":1}}).sort([("steals",-1)])
    steals=list(steals)

    blocks=mongo.db.NBA18_19.find({"blocks":{"$gt":1}}).sort([("blocks",-1)])
    blocks=list(blocks)

    ft=mongo.db.NBA18_19.find({"made_free_throws":{"$gt":1}}).sort([("made_free_throws",-1)])
    ft=list(ft)
    
    headers=["Assists","Made 3 Pointers","Steals","Blocks","Made Free Throws"]
    
    #stats = assist[:10] + three[:10] + steals[:10] + blocks[:10]+ ft[:10]
   
    return render_template('leaders.html',headers=headers,assist=assist[:10],three=three[:10],steals=steals[:10],blocks=blocks[:10],ft=ft[:10])



