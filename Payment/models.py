from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, Page,
    Currency as c, currency_range
)

# import random
import numpy as np


doc = ''


class Constants(BaseConstants):

    name_in_url = 'Payment'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):

    def creating_session(self):
        #print('is this working')
        self.group_randomly()
        players = self.get_players()


class Group(BaseGroup):

    def some_method(self):
        print('is this working')
        players = self.get_players()
        for p in players:
            print('writing final payoffs')
            p.payoff = 99 #self.subsession.in_all_rounds().payoff #there is an e



class Player(BasePlayer):
    payment = models.FloatField()



#class MyWaitPage(Page):
#   after_all_players_arrive = 'set_payment'
 


