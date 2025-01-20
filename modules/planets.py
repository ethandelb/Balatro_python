import streamlit as st
if 'livello_pianeti' not in st.session_state:
    st.session_state['livello_pianeti'] = {"Earth":1, "Jupiter":1, 'Mars':1,'Neptune':1, 'Mercury':1,'Saturn':1,'Uranus':1,'Venus':1}


class Planet:
    def __init__(self,name):
        self.name = name
        self.value = int()

        if self.name == 'Earth':
            self.short_name = 'E'
            self.value = int(4)
        elif self.name == 'Jupiter':
            self.short_name = 'J'
            self.value = int(4)
        elif self.name == 'Mars':
            self.short_name = 'M'
            self.value = int(4)
        elif self.name == 'Mercury':
            self.short_name = 'Me'
            self.value = int(4)
        elif self.name == 'Neptune':
            self.short_name = 'N'
            self.value = int(4)
        elif self.name == 'Saturn':
            self.short_name = 'S'
            self.value = int(4)
        elif self.name == 'Uranus':
            self.short_name = 'U'
            self.value = int(4)
        else:
            self.short_name = 'V'
            self.value = int(4)

        self.image_location = 'static/images/Planets/{}.png'.format(self.short_name)

    def level_hands(self):
        st.session_state['livello_pianeti'][self.name] +=1


        



    @property
    def card_image(self):
        return self.image_location