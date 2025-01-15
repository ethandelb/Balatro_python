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
    # st.image([card.image for card in deck.mano], width=card_width )
    # while len(deck.mano) < carte_mano:
    #     carte_mano = str(carte_mano)
    #     st.button("carta" + carte_mano)
    #     carte_mano = int(carte_mano)
    #     carte_mano = carte_mano - 1

columns = st.columns(8)
with columns[0]:
    card = deck.draw()
    st.image(card.image,use_container_width=True)
    st.button("carta 1",use_container_width=True)

    







