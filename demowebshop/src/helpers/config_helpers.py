import os

def get_base_url():

    env = os.environ.get('ENV', 'test')

    if env.lower() == 'test':
        return 'https://demowebshop.tricentis.com/'
    elif env.lower() == 'prod':
        return  'http://demostore.prod.qaacadem.com'
    else:
        raise Exception(f"Unknown environment: {env}")