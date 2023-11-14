from flask import Flask, request, render_template
from dotenv import load_dotenv
import requests
import json
load_dotenv()

app = Flask(__name__)

SWAPI_URL = 'https://swapi.py4e.com/api/'

@app.route('/', methods=['GET', 'POST'])
def mainpage():
    '''The main page that displays a form for the user to select and display a character from SWAPI'''
    if request.method == 'POST':
        #collect character id
        character_id = request.form['character-id']
        error = False
        if character_id =='17':
            error = True
            context = {
                'error': error
            }
            return render_template('swapi_selector.html', **context)

        elif character_id:
            # response = requests.get(f"{SWAPI_URL}/people/{character_id}")
            response = requests.get(f'{SWAPI_URL}/people/{character_id}')
            character_info = response.json()
            print(character_info)
            # Homeworld api requests
            home_response = requests.get(character_info['homeworld'])
            home_world = home_response.json()

            # Films api requests
            listoffilms = []
            for film in character_info['films']:
                filmdata = requests.get(film).json()
                listoffilms.append(filmdata['title'])
            
            context = {
                'character_info': character_info,
                'homeworld': home_world,
                'films': listoffilms,
            }
            return render_template('swapi_selector.html', **context)
    else:
        return render_template('swapi_selector.html', **context)    

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)