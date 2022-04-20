from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''


class Constants(BaseConstants):

    name_in_url = 'Instructions'
    players_per_group = None
    num_rounds = 1
    play_rounds = 10


class Subsession(BaseSubsession):

    pass


class Group(BaseGroup):

    pass


class Player(BasePlayer):

    name = models.StringField(label='Type your name')
    venmo = models.StringField(label='Type your email')
#    venmo = models.StringField(label='Type your Venmo username (e.g.: @Your-Name)')
