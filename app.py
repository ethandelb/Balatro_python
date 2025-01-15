import streamlit as st
from modules.card import Card
from modules.deck import Deck

st.set_page_config(layout="wide",)

card_width=105
carte_mano = 8
#Scarti = 4
#Mani_giocabili = 5
#grandezza_mano = 5

if 'deck' not in st.session_state:
    number_of_decks = st.number_input("Number of decks", min_value=1, max_value=10, value=1)
    st.session_state['deck'] = Deck(number_of_decks)
    st.session_state['drawn_cards'] = []

start_button = st.button("Start")
if start_button:
    st.session_state['deck'].shuffle()
    st.session_state['drawn_cards'] = []



columns = st.columns(carte_mano)
if 'drawn_cards' not in st.session_state:
    st.session_state['drawn_cards'] = []

for i in range(carte_mano):
    with columns[i]:
        if len(st.session_state['drawn_cards']) <= i:
            card = st.session_state['deck'].draw()
            st.session_state['drawn_cards'].append(card)
        else:
            card = st.session_state['drawn_cards'][i]

        st.image(card.image, use_container_width=True)
        if st.button(f"carta {i + 1}", use_container_width=True):
            card.selected = True
        if card.selected == True:
            st.write("Carta selezionata",use_container_width=True)

    



    







