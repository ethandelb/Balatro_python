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
    st.session_state['selected_cards'] = []
    st.session_state['carte_mano'] = []
    st.session_state['result'] = str()
    st.session_state['punteggio'] = int()

start_button = st.button("Start")
if start_button:
    st.session_state['deck'].shuffle()
    st.session_state['drawn_cards'] = []
    st.session_state['selected_cards'] = []
    st.session_state['carte_mano'] = []

Scarta = st.button("scarta")
Hand = st.button("Butta mano")

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
        if st.button(f"carta {i + 1}", use_container_width=True) and len(st.session_state['selected_cards'])<5:
            if card not in st.session_state['selected_cards']:
                st.session_state['selected_cards'].append(card)
                card.selected = True
            else:
                st.session_state['selected_cards'].remove(card)
                card.selected = False
        if card.selected == True:
            st.write("Carta selezionata")
                

if Scarta:
    for card in st.session_state['selected_cards']:
        if card in st.session_state['drawn_cards']:
            st.session_state['drawn_cards'].remove(card)
    st.session_state['selected_cards'] = []


#Riconoscimento mani poker
def riconoscimento_mani(carte_mano):
    punteggio = 0
    scala_carte = sorted(card.card_scores[1] for card in carte_mano)
    semi = [card.suit for card in carte_mano]

    value_counts = {v: scala_carte.count(v) for v in set(scala_carte)}
    suit_counts = {s: semi.count(s) for s in set(semi)}

    
    is_flush = len(set(semi)) == 1 and len(set(scala_carte)) == 5
    is_straight = len(set(scala_carte)) == 5 and scala_carte[4]-scala_carte[0] == 4
    is_royal = is_flush and scala_carte == [10,11,11,12,13]
    is_straightflush = is_flush and is_straight
    is_pair = 2 in value_counts.values()
    is_theeofakind = 3 in value_counts.values()
    is_fourofakind = 4 in value_counts.values()
    is_fullhouse = sorted(value_counts.values()) == [2,3]
    is_doublepair = list(value_counts.values()).count(2) == 2

    if is_royal:
        st.session_state['result'] = "Hai fatto scala reale!"
        st.session_state['punteggio'] = st.session_state.get('punteggio',0)+ 400
    elif is_straightflush:
        st.session_state['result'] = "Hai fatto scala colore!"
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + 300
    elif is_fourofakind:
        st.session_state['result'] = "Hai fatto poker!"
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + 170
    elif is_fullhouse:
        st.session_state['result'] = "Hai fatto full house!"
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + 150
    elif is_flush:
        st.session_state['result'] = "Hai fatto flush!"
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + 125
    elif is_straight:
        st.session_state['result'] = "Hai fatto scala!"
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + 100
    elif is_theeofakind:
        st.session_state['result'] = "Hai fatto tris!"
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + 50
    elif is_doublepair:
        st.session_state['result'] = "Hai fatto doppia coppia!"
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + 40
    elif is_pair:
        st.session_state['result'] = "Hai fatto coppia!"
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + 30
    # else:
    #     st.session_state['result'] = "Hai fatto carta alta!"
    #     st.session_state['punteggio'] = st.session_state.get('punteggio',0) + card.card_scores[1]
    


    #Debug
    st.write(f"Flush: {is_flush}, Straight: {is_straight},Royal: {is_royal}, Four of a kind {is_pair}")
    st.write(f"Punteggio attuale: {st.session_state.get('punteggio', 0)}")
    #st.write(f"Tipo di punteggio: {type(st.session_state.get('punteggio', 0))}")

if Hand:
    for card in st.session_state['selected_cards']:
        if card in st.session_state['drawn_cards']:
            st.session_state['drawn_cards'].remove(card)
            st.session_state['carte_mano'].append(card)
    st.session_state['selected_cards'] = []
    riconoscimento_mani(st.session_state['carte_mano'])
    st.session_state['carte_mano'] = []
    st.markdown(st.session_state['result']+"+"+ str(st.session_state['punteggio']))
    
    







    







