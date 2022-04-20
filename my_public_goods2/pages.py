
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class MyPage(Page):
    form_model = 'player'
    form_fields = ['contribution']
    
class ResultsWaitPage(WaitPage):
    body_text = 'Waiting for other players in the experiment.'
    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Results(Page):
    form_model = 'player'

##class BeforeFinalResults(WaitPage): # this could be 3/18
##    def after_all_players_arrive(self):
##        for player in self.group.get_players():
##            player.final_payoff()
            
    #after_all_players_arrive = 'final_payoff' # this could be 3/18
    
class FinalResults(Page):
    """Final payoff"""
    #form_model = 'player'

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        payment_round = self.player.payround # THIS AND LINE BELOW WORK 3/17
        player_in_payment_round = self.player.in_round(payment_round)
        mpl_payoff = self.player.mpl_payment ## 3/18
        #mpl_payment = self.participant.vars['mpl_payoff'] # Added this 3/17
        return {
            'app2_payoff': player_in_payment_round.payoff,
            'payment_round': payment_round,
            'mpl_payoff': self.player.mpl_payment,## 3/18
            'app1_payoff': mpl_payoff,
            'total_payoff': self.player.total_payoff ## 3/18
        }

    def before_next_page(self):
        for player in self.group.get_players():
            print('computing final payoff')
            player.final_payoff()
            
    

##    def vars_for_template(self):
##
##        return {
##            'paying_round': self.session.vars['paying_round'],
##            'player_in_all_rounds': self.player.in_all_rounds(),
##            'payment_player': self.player.in_round['paying_round'],
##            'total_payoff': sum([p.payoff
##                                 for p in self.player.in_round(paying_round)])
##        }

        #payment_player = player.in_round(paying_round) # This is what I added
        #print(payment_player.payoff)

class Link(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds
    form_model = 'player'

    
page_sequence = [MyPage, ResultsWaitPage, Results, FinalResults, Link]
