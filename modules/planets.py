class Planet:
    def __init__(self,name):
        self.name = name

        if self.name == 'Earth':
            self.short_name = 'E'
        elif self.name == 'Jupiter':
            self.short_name = 'J'
        elif self.name == 'Mars':
            self.short_name = 'M'
        elif self.name == 'Mercury':
            self.short_name = 'Me'
        elif self.name == 'Neptune':
            self.short_name = 'N'
        elif self.name == 'Saturn':
            self.short_name = 'S'
        elif self.name == 'Uranus':
            self.short_name = 'U'
        else:
            self.short_name = 'V'

        self.image_location = 'static/images/Planets/{}.webp'.format(self.short_name)

    @property
    def card_image(self):
        return self.image_location