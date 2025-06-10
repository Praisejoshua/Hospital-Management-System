import pandas 
import random
import os
from django.conf import settings

def get_random_health_tips():
    """
    Returns a random health tip from the health_tips.excel sheet file.
    """
    file_path = os.path.join(settings.BASE_DIR, 'data', 'health_tips.xlsx')

    df = pandas.read_excel(file_path)
    tips = df['Health Tip'].tolist()

    return random.choice(tips) if tips else "No health tips available at the moment."