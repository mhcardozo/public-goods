from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Quiz'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    quiz1 = models.StringField(
        choices=[['1', '1'], ['2', '10'], ['3', '20']],
        label='''1)	How many times will you have to make a decision during the experiment?''',
        widget=widgets.RadioSelect
    )
    def quiz1_error_message(self, value):
        print('value is', value)
        if (value != '2'):
            return 'wrong, number ' + value + ' is not the correct answer'

    quiz2 = models.StringField(
        choices=[['1', 'True'], ['2', 'False']],
        label='''2)	Each round you are randomly assigned to a group of 4.''',
        widget=widgets.RadioSelect
    )
    def quiz2_error_message(self, value):
        print('value is', value)
        if (value != '1'):
            return 'wrong, number ' + value + ' is not the correct answer'

    quiz3 = models.StringField(
        choices=[['1', '20'], ['2', '50'], ['3', '60']],
        label='''3)	If you participated in 100 rounds, how many times on average would you get 0.4 as your Random Number?''',
        widget=widgets.RadioSelect
    )
    def quiz3_error_message(self, value):
        print('value is', value)
        if (value != '1'):
            return 'wrong, number ' + value + ' is not the correct answer'

    quiz4 = models.StringField(
        choices=[['1', '80'], ['2', '(80 – 43) + (0.2 x 99)'], ['3', '(80 – 43) + (0.2 x 99) + 16']],
        label='''4)	Suppose your Random Number is 0.2, you choose Contract 3 that allocates 43 Tokens to the Group Account and the Group Account ends up having 99 Tokens in it. Your earnings for that round are''',
        widget=widgets.RadioSelect
    )
    def quiz4_error_message(self, value):
        print('value is', value)
        if (value != '3'):
            return 'wrong, number ' + value + ' is not the correct answer'

    quiz5 = models.StringField(
        choices=[['1', '80'], ['2', '(80 - 43) + (0.4 x 99)'], ['3', '(80 - 43) + (0.4 x 99) + 16']],
        label='''5)	Suppose your Random Number is 0.4, you choose Contract 3 that allocates 43 Tokens to the Group Account and the Group Account ends up having 56 Tokens in it. Your earnings for that round are''',
        widget=widgets.RadioSelect
    )
    def quiz5_error_message(self, value):
        print('value is', value)
        if (value != '1'):
            return 'wrong, number ' + value + ' is not the correct answer'

    quiz6 = models.StringField(
        choices=[['1', '10'], ['2', '11'], ['3', '16']],
        label='''6)	If the earnings of the round randomly picked for your payments were 88 Tokens. Your earnings in dollars at the end of the experiment (including your $5 show fee) are''',
        widget=widgets.RadioSelect
    )
    def quiz6_error_message(self, value):
        print('value is', value)
        if (value != '3'):
            return 'wrong, number ' + value + ' is not the correct answer'
