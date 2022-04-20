from os import environ
PARTICIPANT_FIELDS = ['mpl_payment']

SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0.125,
                               participation_fee=5)
SESSION_CONFIGS = [dict(name='public_goods',
                        num_demo_participants=4,
                        app_sequence=['mpl', 'Instructions', 'my_public_goods2', 'Payment', 'Demographics'])] # add 'Quiz'for experiment
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
POINTS_CUSTOM_NAME = 'Tokens'
DEMO_PAGE_INTRO_HTML = ''
ROOMS = [
    dict(
        name='eLab',
        display_name='eLab',
        participant_label_file='_rooms/participants.txt',
        use_secure_urls=False  # for toggling individual links (True)
    ),
    dict(
        name='econ_lab',
        display_name='Experimental Economics Lab'
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
