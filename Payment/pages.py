
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

#class Venmo(Page):
#    form_model = 'player'
#    form_fields = ['name', 'venmo']
# NEED TO SWAP VENMO FOR INFORMATION LATER

# class Information(Page):
#     form_model = 'player'
#     form_fields = ['name', 'venmo']


class Payment(Page):
    form_model = 'player'

page_sequence = [Payment]
