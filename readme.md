# Python

## Installation

Vous avez besoin d'avoir python3 d'installé.

`python3 -m venv venv`

`source ./venv/bin/activate`

`pip3 install -r requirements.txt`

`python3 app.py`

## Règles

Les règles sont simples :
- Ne touchez pas les bords de l'écran. Chaque touche en dehors de l'écran vous fait perdre une vie.
- Évitez les obstacles et votre propre python, sinon vous perdrez une vie.
- Ramassez autant de nourriture que possible pour augmenter votre score : une nourriture vaut 10 points.
- Soyez attentif aux malus et aux bonus qui peuvent modifier le cours du jeu.
    - Les bonus jaunes vous donnent une vie supplémentaire.
    - Les bonus roses ralentissent le temps.
    - Les malus kakis accélèrent le temps.
    - Les malus bleu foncé ajoutent 5 obstacles permanents pour la partie.
