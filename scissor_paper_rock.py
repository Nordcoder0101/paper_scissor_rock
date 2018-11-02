from flask import Flask, render_template, request, redirect, session
from random import random


app = Flask(__name__)
app.secret_key = "Don't mess with the rock"

gamekey = {'rock': {'paper': 'loss', 
                    'scissors': 'win', 
                    'rock': 'tie'},
          'paper': {'rock': 'win',
                    'scissors': 'loss', 'paper':'tie'}, 
          'scissors': {'paper': 'win',
                      'rock': 'loss', 
                      'scissors': 'tie'}
          }

def random_pic():
  computer_pick_list = ['rock','paper','scissors']
  random_val = round(random()*2)
  return computer_pick_list[random_val]

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result", methods=["POST"])
def show_result():
  player_choice = request.form["choice"]
  computer_choice = random_pic()
  message1 = f"You picked {player_choice}"
  message2 = f"Computer picked {computer_choice}"
  message3 = f"You {gamekey[player_choice][computer_choice]}"
  result = gamekey[player_choice][computer_choice]
  session['player_choice'] = player_choice
  session['computer_choice'] = computer_choice
  
  
  if result == 'win':
    session['win_counter'] += 1
  elif result == 'loss':
    session['loss_counter'] += 1
  else:
    session['tie_counter'] += 1  

  return redirect("/")

if __name__ =='__main__':
    app.run(debug=True)