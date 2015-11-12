# separator used by search.py, categories.py, ...
SEPARATOR = ";"

LANG            = "en_US" #"en_US" # can be en_US, fr_FR, ...
ANDROID_ID      = "xxx" # "38c6523ac43ef9e1"
GOOGLE_LOGIN    = 'xxxx@gmail.com' # 'someone@gmail.com'
GOOGLE_PASSWORD = 'xx' # 'yourpassword'
AUTH_TOKEN      = None # "yyyyyyyyy"

# force the user to edit this file
if any([each == None for each in [ANDROID_ID, GOOGLE_LOGIN, GOOGLE_PASSWORD]]):
    raise Exception("config.py not updated")

