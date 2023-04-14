import sys
sys.path.append('/home/jae/myprj/mysite')  #  Python search 디렉토리 경로 추가

# To use Django objects in the file which are not created from startapps command, add DJANGO_SETTING_MODULE to the system environemnt 
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

from daq.models import Tnh

def save_db(msg):
    db_tab1 = Tnh()
    data = msg.split() # split string type of data
    db_tab1.temperature = float(data[0])
    db_tab1.humidity = float(data[1])
    db_tab1.save()

    print(db_tab1.temperature, db_tab1.humidity)
