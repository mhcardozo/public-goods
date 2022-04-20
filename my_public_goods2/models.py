
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

# import random
import numpy as np

param = [0.2, 0.2, 0.2, 0.2, 0.4]
paramf = map(float, param)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'my_public_goods2'
    players_per_group = 4
    num_rounds = 2 # CHANGE THIS TO 20!!!!
######### PARAMETERS ########
    endowment = c(80)
    threshold = c(70)
    reward1 = c(0)
    reward2 = c(0)
    reward3 = c(16)
    cont1 = c(0)
    cont2 = c(13)
    cont3 = c(43)
######### ---------- ########
    
class Subsession(BaseSubsession):

    def creating_session(self):
        self.group_randomly()
        players = self.get_players()
    
        #self.session.vars['paying_round'] = paying_round

        for p in players:
            p.type = np.random.choice([0.2, 0.4], p=[0.8, 0.2])
            p.payround = np.random.choice(np.arange(1,Constants.num_rounds+1))

   # THIS IS ME TRYING TO GET THE PAYING ROUND
        


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    def set_payoffs(self):
        players = self.get_players()
        contributions = [p.contribution for p in players]
        self.total_contribution = sum(contributions)
        for p in players:
            if self.total_contribution < Constants.threshold:
                p.payoff = Constants.endowment
                p.grouppayoff = 0
                p.indpayoff = Constants.endowment
                p.extratokens = 0
            elif p.contribution == Constants.cont1:
                p.payoff = Constants.endowment - p.contribution + p.type*self.total_contribution + Constants.reward1
                p.grouppayoff = p.type*self.total_contribution 
                p.indpayoff = Constants.endowment - p.contribution
                p.extratokens = 0
            elif p.contribution == Constants.cont2:
                p.payoff = Constants.endowment - p.contribution + p.type*self.total_contribution + Constants.reward2
                p.grouppayoff = p.type*self.total_contribution
                p.indpayoff = Constants.endowment - p.contribution
                p.extratokens = 0
            else:
                p.payoff = Constants.endowment - p.contribution + p.type*self.total_contribution + Constants.reward3
                p.grouppayoff = p.type*self.total_contribution
                p.indpayoff = Constants.endowment - p.contribution
                p.extratokens = Constants.reward3
            #p.grouppayoff = p.payoff - Constants.endowment + p.contribution # Payoff from Group Account
            #p.indpayoff = Constants.endowment - p.contribution # Payoff from Individual Account
            # THIS TO WRITE DOWN THE CONTRACT IN RESULTS:
        for p in players:
            if p.contribution == Constants.cont1:
                p.contract = 1
            elif p.contribution == Constants.cont2:
                p.contract = 2
            else:
                p.contract = 3
        for p in players:
            p.participant.vars['payments'] = 2 #self.subsession.in_all_rounds().payoff #there is an error HERE


class Player(BasePlayer):
    contract = models.IntegerField()
    contribution = models.CurrencyField(choices=[[0, 'Contract 1: 0 Tokens to Group Account'], [13, 'Contract 2: 13 Tokens to Group Account'], [43, 'Contract 3: 43 Tokens to Group Account']], label='Choose a Contract:', min=Constants.cont1)
    type = models.FloatField()
    grouppayoff = models.CurrencyField() # added 09/10 to create Group Payoff
    indpayoff = models.CurrencyField() # added 09/10 to create Individual Payoff
    extratokens = models.CurrencyField()
    payround = models.IntegerField()
    mpl_payment = models.FloatField() # added to use payoff from MPL 3/17
    total_payoff = models.FloatField()
    mpl_payoff = models.FloatField()
    payment_round= models.IntegerField()

    def final_payoff(self):
        return self.participant.vars['mpl_payoff']
        self.payment_round = self.payround # THIS AND LINE BELOW WORK 3/17, THEY WERE ORIGINALLY IN PAGES, IF IT BREAKS PUT THEM BACK!
        #self.player_in_payment_round = self.in_round(self.payment_round)
        self.mpl_payment = self.participant.vars['mpl_payoff']
        self.total_payoff = self.mpl_payment + self.payoff


    

            
            
