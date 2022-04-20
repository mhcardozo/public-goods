from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


#class Welcome(Page):
#    form_model = 'player'

class Introduction(Page):
    form_model = 'player'

class Quiz1(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 'quiz6']

    

page_sequence = [Introduction, Quiz1]
