import streamlit as st
from modules.card import Card
from modules.deck import Deck
from modules.planets import Planet
from modules.shop_deck import Shop_deck
import time

st.set_page_config(layout="wide",)

card_width=105
carte_mano = 8
massimo_mani = 5
massimo_scarti = 5
tipi_mazzi = ("Verde","Rosso","Giallo","Blu")
st.session_state['punteggio_base'] = 300
#Mani_giocabili = 5
#grandezza_mano = 5

if 'deck' not in st.session_state:
    number_of_decks = 1
    st.session_state['deck'] = Deck(number_of_decks)
    st.session_state['shop_cards'] = Shop_deck(number_of_decks)
    st.session_state['shop_cards'].shuffle()
    st.session_state['shop_cards_shown'] = []
    st.session_state['deck'].shuffle()
    st.session_state['drawn_cards'] = []
    st.session_state['selected_cards'] = []
    st.session_state['carte_mano'] = []
    st.session_state['result'] = str()
    st.session_state['punteggio'] = int()
    st.session_state['carte_rimanenti'] = len(st.session_state['deck'].cards)
    st.session_state['soldi'] = 4
    st.session_state['punteggio da fare'] = int(st.session_state['punteggio_base'])
    st.session_state['show_blind'] = False
    st.session_state['livello'] = 1
    st.session_state['ante'] = 1
    st.session_state['divisore_punteggio'] = 1.5
    st.session_state['vittoria'] = False
    st.session_state.show_dialog = False
    st.session_state.num_mazzo = 0
    st.session_state.tipo_mazzo = ["Mazzo blu", "Mazzo verde", "Mazzo giallo", "Mazzo rosso"]
    if st.session_state.num_mazzo == 0:
        st.session_state['mani_rimanenti'] = int(6)
    elif st.session_state.num_mazzo != 0:
        st.session_state['mani_rimanenti'] = int(5)
    if st.session_state.num_mazzo == 3:
        st.session_state['scarti_rimanenti'] = int(6)
    elif st.session_state.num_mazzo != 3:
        st.session_state['scarti_rimanenti'] = int(5)
    if st.session_state.num_mazzo == 2:
        st.session_state['soldi'] = int(14)
    elif st.session_state.num_mazzo != 2:
        st.session_state['soldi'] = int(4)
    #punteggi base
    #coppia
    st.session_state['moltiplicatore_base_coppia'] = int(2)
    st.session_state['Fiche_base_coppia'] = int(10)
    #doppia coppia
    st.session_state['moltiplicatore_base_doppiacoppia'] = int(2)
    st.session_state['Fiche_base_doppiacoppia'] = int(20)
    #tris
    st.session_state['Fiche_base_tris'] = int(30)
    st.session_state['moltiplicatore_base_tris'] = int(3)
    #straight
    st.session_state['moltiplicatore_base_straight'] = int(4)
    st.session_state['Fiche_base_straight'] = int(30)
    #colore
    st.session_state['Fiche_base_colore'] = int(35)
    st.session_state['moltiplicatore_base_colore'] = int(4)
    #fullhouse
    st.session_state['Fiche_base_fullhouse'] = int(40)
    st.session_state['moltiplicatore_base_fullhouse'] = int(4)
    #fourofakind
    st.session_state['Fiche_base_four'] = int(60)
    st.session_state['moltiplicatore_base_four'] = int(7)
    #straightflush
    st.session_state['Fiche_base_straightflush'] = int(100)
    st.session_state['moltiplicatore_base_straightflush'] = int(8)
    #royal
    st.session_state['Fiche_base_royal'] = int(100)
    st.session_state['moltiplicatore_base_royal'] = int(8)  
           


option_subcol1,option_subcol2 = st.columns([0.5,0.5])
        
@st.dialog("Impostazioni partita")
def show_options():
    st.title("Scegli un mazzo: ")
    immagine_mazzo = 'static/images/{}.png'.format(st.session_state.tipo_mazzo[st.session_state.num_mazzo])
    st.session_state['scritta_mazzo'] = str(st.session_state.tipo_mazzo[st.session_state.num_mazzo])
    place_holder =st.empty()
    i1,colo1,colo2,colo3,i2=st.columns([0.2,0.2,0.1,0.2,0.2])
    i3,colo5,i7=st.columns([0.23,0.15,0.2])
    colmazzo1,colmazzo2,colmazzo3 = st.columns([0.4,0.33,0.33],)
    with st.container():
        if colo3.button("->",use_container_width=True):
            if st.session_state.num_mazzo < len(st.session_state.tipo_mazzo) - 1:
                st.session_state.num_mazzo += 1   
                immagine_mazzo = 'static/images/{}.png'.format(st.session_state.tipo_mazzo[st.session_state.num_mazzo])
                st.session_state['scritta_mazzo'] = str(st.session_state.tipo_mazzo[st.session_state.num_mazzo])
                with place_holder:
                    colo5.write(st.session_state['scritta_mazzo'])
        if colo1.button("<-",use_container_width=True):
            if st.session_state.num_mazzo > 0:
                st.session_state.num_mazzo -= 1
                immagine_mazzo = 'static/images/{}.png'.format(st.session_state.tipo_mazzo[st.session_state.num_mazzo])
                st.session_state['scritta_mazzo'] = str(st.session_state.tipo_mazzo[st.session_state.num_mazzo])
                with place_holder:
                    colo5.write(st.session_state['scritta_mazzo'])
    with st.container():
        if st.session_state.num_mazzo == 0:
            st.session_state['mani_rimanenti'] = int(6)
            colmazzo2.image(immagine_mazzo,caption="Aggiunge una mano extra", width=105)
        elif st.session_state.num_mazzo != 0:
            st.session_state['mani_rimanenti'] = int(5)
        if st.session_state.num_mazzo == 3:
            st.session_state['scarti_rimanenti'] = int(6)
            colmazzo2.image(immagine_mazzo, caption="Aggiunge uno scarto extra", width=105)
        elif st.session_state.num_mazzo != 3:
            st.session_state['scarti_rimanenti'] = int(5)
        if st.session_state.num_mazzo == 2:
            st.session_state['soldi'] = int(14)
            colmazzo2.image(immagine_mazzo, caption="Aggiunge 10 soldi extra", width=105)
        elif st.session_state.num_mazzo != 2:
            st.session_state['soldi'] = int(4)
        if st.session_state.num_mazzo == 1:
           colmazzo2.image(immagine_mazzo, caption= "non ricordo cosa faccia", width=105)   
    st.divider()
    if st.button("Rerun(ricarca per applicare mazzi)"):
        st.rerun()



@st.dialog("Puntate")
def show_blinds():
    small_blindcol,big_blincol,boss_blindcol = st.columns([0.33,0.33,0.33])
    with st.container():
        small_blindcol.title("Piccolo buio")
        big_blincol.title("Grande buio")
        boss_blindcol.title("Boss")


@st.dialog("Negozio")
def show_shop():
    st.title("Scegli cosa comprare: ")
    colonna1,colonna2,colonna3 = st.columns([0.3,0.5,0.5])
    with st.container():
        if colonna1.button("Next run"):
            number_of_decks = 1
            st.session_state['punteggio'] = 0
            st.session_state['show_blind'] = True
            st.session_state['punteggio da fare'] = (st.session_state['punteggio_base'] * st.session_state['ante']*st.session_state['livello'])/ st.session_state['divisore_punteggio']
            st.session_state['deck'] = Deck(number_of_decks)
            st.session_state['deck'].shuffle()
            st.session_state['drawn_cards'] = []
            st.session_state['selected_cards'] = []
            st.session_state['carte_mano'] = []
            st.session_state['carte_rimanenti'] = len(st.session_state['deck'].cards)
            st.session_state.tipo_mazzo = ["Mazzo blu", "Mazzo verde", "Mazzo giallo", "Mazzo rosso"]
            if st.session_state.num_mazzo == 0:
                st.session_state['mani_rimanenti'] = int(6)
            elif st.session_state.num_mazzo != 0:
                st.session_state['mani_rimanenti'] = int(5)
            if st.session_state.num_mazzo == 3:
                st.session_state['scarti_rimanenti'] = int(6)
            elif st.session_state.num_mazzo != 3:
                st.session_state['scarti_rimanenti'] = int(5)
            if st.session_state.num_mazzo == 2:
                st.session_state['soldi'] = int(14)
            elif st.session_state.num_mazzo != 2:
                st.session_state['soldi'] = int(4)
            st.rerun()
        #carte shop
        
        carte_negozio = st.session_state['shop_cards'].draw_shop()
        st.session_state['shop_cards_shown'].append(carte_negozio)

        st.image(carte_negozio.card_image ,use_container_width=True)


        
if st.session_state['show_blind']:
    st.session_state['show_blind'] = False
    show_blinds()    




col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1],vertical_alignment="center")
with col1:
    if st.button("Start",use_container_width=True):
        number_of_decks = 1
        st.session_state['deck'] = Deck(number_of_decks)
        st.session_state['deck'].shuffle()
        st.session_state['drawn_cards'] = []
        st.session_state['selected_cards'] = []
        st.session_state['carte_mano'] = []
        st.session_state['result'] = str()
        st.session_state['punteggio'] = int(300)
        st.session_state['scarti_rimanenti'] = int(5)
        st.session_state['mani_rimanenti'] = int(5)
        st.session_state['carte_rimanenti'] = len(st.session_state['deck'].cards)
        st.session_state['show_blind'] = False
        #punteggi base
        #coppia
        st.session_state['moltiplicatore_base_coppia'] = int(2)
        st.session_state['Fiche_base_coppia'] = int(10)
        #doppia coppia
        st.session_state['moltiplicatore_base_doppiacoppia'] = int(2)
        st.session_state['Fiche_base_doppiacoppia'] = int(20)
        #tris
        st.session_state['Fiche_base_tris'] = int(30)
        st.session_state['moltiplicatore_base_tris'] = int(3)
        #straight
        st.session_state['moltiplicatore_base_straight'] = int(4)
        st.session_state['Fiche_base_straight'] = int(30)
        #colore
        st.session_state['Fiche_base_colore'] = int(35)
        st.session_state['moltiplicatore_base_colore'] = int(4)
        #fullhouse
        st.session_state['Fiche_base_fullhouse'] = int(40)
        st.session_state['moltiplicatore_base_fullhouse'] = int(4)
        #fourofakind
        st.session_state['Fiche_base_four'] = int(60)
        st.session_state['moltiplicatore_base_four'] = int(7) 
    if st.button("Options",use_container_width=True):
        show_options()
    if st.session_state['punteggio'] >= st.session_state['punteggio da fare']:
        st.session_state['vittoria'] = True
        if st.session_state['livello'] == 3:
            st.session_state['livello'] = 1
            st.session_state['ante'] += 1
            st.session_state['punteggio_base'] += 300
        else:
            st.session_state['livello'] += 1
        show_shop()

         
            


with col2:
    subcol1,scubcol2 =st.columns([0.5,0.5])
    with subcol1:
        Scarta = st.button("scarta",type='primary',use_container_width=True)
    with scubcol2:
        Hand = st.button("Butta mano",use_container_width=True)
with col5:
    st.header("Mani rimanenti: " + str(st.session_state['mani_rimanenti']))
    st.header("Scarti rimanenti: " + str(st.session_state['scarti_rimanenti']))
    st.header("Carte rimanenti "+str(st.session_state['carte_rimanenti']))
    if st.session_state['carte_rimanenti'] <= 0:
        st.header("Hai finito le carte!")
        number_of_decks = 1
        st.session_state['deck'] = Deck(number_of_decks)
        st.session_state['deck'].shuffle()
        st.session_state['drawn_cards'] = []
        st.session_state['selected_cards'] = []
        st.session_state['carte_mano'] = []
        st.session_state['result'] = str()
        st.session_state['punteggio'] = int()
        st.session_state['scarti_rimanenti'] = int(5)
        st.session_state['mani_rimanenti'] = int(5)
        st.session_state['carte_rimanenti'] = len(st.session_state['deck'].cards)

st.divider()

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
                
with col2:
    if Scarta:
        if st.session_state['scarti_rimanenti'] > 0:
            for card in st.session_state['selected_cards']:
                if card in st.session_state['drawn_cards']:
                    st.session_state['drawn_cards'].remove(card)
            st.session_state['carte_rimanenti'] = len(st.session_state['deck'].cards)
            st.session_state['selected_cards'] = []
            st.session_state['scarti_rimanenti'] = st.session_state.get('scarti_rimanenti',0) -1
            st.rerun()

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
    is_highcard = len(set(scala_carte)) > 0

    if is_royal:
        st.session_state['result'] = "Hai fatto scala reale!"
        for card in st.session_state['carte_mano']:
            st.session_state['Fiche_base_royal'] += card.card_scores[1]
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + (st.session_state['moltiplicatore_base_royal'] * st.session_state['Fiche_base_royal'])
    elif is_straightflush:
        st.session_state['result'] = "Hai fatto scala colore!"
        for card in st.session_state['carte_mano']:
            st.session_state['Fiche_base_straightflush'] += card.card_scores[1]
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + (st.session_state['moltiplicatore_base_straightflush'] * st.session_state['Fiche_base_straightflush'])
    elif is_fourofakind:
        st.session_state['result'] = "Hai fatto poker!"
        st.session_state['carte_mano'] = [card for card in st.session_state['carte_mano'] if value_counts[card.card_scores[1]] == 4]
        for card in st.session_state['carte_mano']:
            st.session_state['Fiche_base_four'] += card.card_scores[1]
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + (st.session_state['moltiplicatore_base_four'] * st.session_state['Fiche_base_four'])
    elif is_fullhouse:
        st.session_state['result'] = "Hai fatto full house!"
        for card in st.session_state['carte_mano']:
            st.session_state['Fiche_base_fullhouse'] += card.card_scores[1]
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + (st.session_state['moltiplicatore_base_fullhouse'] * st.session_state['Fiche_base_fullhouse'])
    elif is_flush:
        st.session_state['result'] = "Hai fatto flush!"
        for card in st.session_state['carte_mano']:
            st.session_state['Fiche_base_colore'] += card.card_scores[1]
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + (st.session_state['moltiplicatore_base_colore'] * st.session_state['Fiche_base_colore'])
    elif is_straight:
        st.session_state['result'] = "Hai fatto scala!"
        for card in st.session_state['carte_mano']:
            st.session_state['Fiche_base_tris'] += card.card_scores[1]
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + (st.session_state['moltiplicatore_base_straight'] * st.session_state['Fiche_base_straight'])
    elif is_theeofakind:
        st.session_state['result'] = "Hai fatto tris!"
        st.session_state['carte_mano'] = [card for card in st.session_state['carte_mano'] if value_counts[card.card_scores[1]] == 3]
        for card in st.session_state['carte_mano']:
            st.session_state['Fiche_base_tris'] += card.card_scores[1]
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + (st.session_state['moltiplicatore_base_tris'] * st.session_state['Fiche_base_tris'])
    elif is_doublepair:
        st.session_state['result'] = "Hai fatto doppia coppia!"
        st.session_state['carte_mano'] = [card for card in st.session_state['carte_mano'] if value_counts[card.card_scores[1]] == 2]
        for card in st.session_state['carte_mano']:
            st.session_state['Fiche_base_doppiacoppia'] += card.card_scores[1]
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + (st.session_state['moltiplicatore_base_doppiacoppia'] * st.session_state['Fiche_base_doppiacoppia'])
    elif is_pair:
        sorted(value_counts.values())
        st.session_state['carte_mano'] = [card for card in carte_mano if value_counts[card.card_scores[1]] == 2]
        st.session_state['result'] = "Hai fatto coppia!"
        for card in st.session_state['carte_mano']:
            n= 0
            st.session_state['Fiche_base_coppia'] = st.session_state['Fiche_base_coppia'] + card.card_scores[n]
            n +=1
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + (st.session_state['moltiplicatore_base_coppia'] * st.session_state['Fiche_base_coppia'])
    elif is_highcard: 
        st.session_state['result'] = "Hai fatto carta alta!"
        st.session_state['punteggio'] = st.session_state.get('punteggio',0) + 5 + card.card_scores[1] 
    # else:
    #     st.session_state['result'] = "Hai fatto carta alta!"
    #     st.session_state['punteggio'] = st.session_state.get('punteggio',0) + card.card_scores[1]
    


    #Debug
    #st.write(f"Flush: {is_flush}, Straight: {is_straight},Royal: {is_royal}, Four of a kind {is_pair}")
    #st.write(f"Punteggio attuale: {st.session_state.get('punteggio', 0)}")
    #st.write(f"Tipo di punteggio: {type(st.session_state.get('punteggio', 0))}")

with col3:
    if Hand:
        if st.session_state['mani_rimanenti'] > 0:
            for card in st.session_state['selected_cards']:
                if card in st.session_state['drawn_cards']:
                    st.session_state['drawn_cards'].remove(card)
                    st.session_state['carte_mano'].append(card)
            st.session_state['selected_cards'] = []
            riconoscimento_mani(st.session_state['carte_mano'])
            st.session_state['carte_mano'] = []
            st.header(st.session_state['result'])
            st.session_state['mani_rimanenti'] = st.session_state.get('mani_rimanenti',0) -1
            st.session_state['result'] = str()
            st.session_state['carte_rimanenti'] = len(st.session_state['deck'].cards)
            time.sleep(2)
            st.session_state['Fiche_base_coppia'] = int(10)
            st.rerun()
        else:
            st.header("Non hai più mani inizia una nuova partita")
with col4:
    st.header("livello: " + str(st.session_state['livello']))
    st.header("Ante: "+ str(st.session_state['ante']))
    st.header("Punteggio:"+ (str(st.session_state['punteggio']))+"/"+(str(st.session_state['punteggio da fare'])))
    st.header('Soldi: '+(str(st.session_state['soldi'])))



    
    
    







    







