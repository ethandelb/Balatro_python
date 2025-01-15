import streamlit as st
from modules.card import Card
from modules.deck import Deck

st.set_page_config(
   layout="wide",
)

card_width=105
carte_mano = 8
#Scarti = 4
#Mani_giocabili = 5
#grandezza_mano = 5


number_of_decks = st.number_input("Number of decks", min_value=1, max_value=10, value=1)

deck = Deck(number_of_decks)

start_button = st.button("Start")
if start_button:
    deck.shuffle()

columns = st.columns(carte_mano)
n=0
while n < carte_mano:
    with columns[n]:
       card = deck.draw()
       st.image(card.image,use_container_width=True)
       card_button = st.button("carta " + str(n+1),use_container_width=True) 
    n = n +1
    



    







