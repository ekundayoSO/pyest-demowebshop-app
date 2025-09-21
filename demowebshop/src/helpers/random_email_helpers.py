
import random
import string
import logging as logger

def generate_random_email_and_password(domain=None, email_prefix= None):

    if not domain:
        domain = 'gmail.com'
    #if not email_prefix:
    #    email_prefix = 'testuser'

    random_string_length = 6
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_string_length))

    #email = email_prefix + '_' + random_string + '@' + domain
    email = random_string + '@' + domain




    logger.info(f"Generated random email: {email}")

    random_passwd_length = 20
    random_password = ''.join(random.choices(string.ascii_letters, k=random_passwd_length))

    logger.info(f"Generated random password: {random_password}")

    random_info = {"email": email, "password": random_password}

    return random_info

