from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


#class Welcome(Page):
#    form_model = 'player'

class Link(Page):
    form_model = 'player'

    

page_sequence = [Link]
