# imports
from instapy import InstaPy
from instapy import smart_run
import configparser

#load config 
config = configparser.ConfigParser()
parser = configparser.ConfigParser()
parser.read("setting.txt")

print("Login with : "+parser.get("instagram-account", "username"))



#login credentials
insta_username = parser.get('instagram-account', 'username')
insta_password = parser.get('instagram-account', 'password')

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_skip_users(skip_private=False, private_percentage=0)
    session.set_user_interact(amount=3, randomize=True, percentage=50)

                       

    # activity   
    accs = parser.get('follow-by-list', 'followlist').split(",")
    print(accs)
    session.follow_by_list(accs,  sleep_delay=600, interact=True)

  
