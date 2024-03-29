import os, re
from os import environ


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))


# test 
DRAGONS = set(int(x) for x in os.environ.get("DRAGONS", "").split())
DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())



PICS = (environ.get('PICS', 'https://graph.org/file/d2c20ed467fd8a101409f.jpg https://graph.org/file/9fbfa93142640fdaeaf80.jpg https://graph.org/file/e2fba097d69d27061b1e1.jpg https://graph.org/file/fed816c138a42cafc24bb.jpg https://graph.org/file/e6ecfe9f99030aebbbd05.jpg https://graph.org/file/941bae7b0584a16eb0fd2.jpg https://graph.org/file/3f38fa53398771d450c0f.jpg')).split()
MALIK_PH = environ.get("MALIK_PH", "https://telegra.ph/file/0547d69b90b596ad6bae1.jpg")
SMART_PIC = environ.get("SMART_PIC", "https://graph.org/file/2182926ecba267071b0ec.jpg")
VIDEO_VD = environ.get("VIDEO_VD", "https://telegra.ph/file/566ff238e36d9f2425568.mp4")
M_N_F = environ.get("M_N_F", "https://telegra.ph/file/7cf564b255461abfc75fe.jpg")
PHT = environ.get("PHT", "https://graph.org/file/6fd6ac1307da808e44571.jpg")
PHTT = environ.get("PHTT", "https://telegra.ph/file/1ddc551c64a4afd5a660e.mp4")
M_NT_F = environ.get("M_NT_F", "https://graph.org/file/bbb4bcb02f35d6b87f11c.jpg")

DEL_SECOND = int(os.environ.get("DEL_SECOND", "300"))


CREATOR_USERNAME = os.environ.get("CREATOR_USERNAME", "sahid_malik")
CREATOR_NAME = os.environ.get("CREATOR_NAME", "sahid malik")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "hjhjvjjjvbot")


auth_userss = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERSS', '').split()]
AUTH_USERSS = (auth_userss) if auth_userss else []

AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
AUTO_DELETE2 = is_enabled((environ.get('AUTO_DELETE2', "True")), True)
# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')


# Others
FILTER_BUTTONS = os.environ.get("FILTER_BUTTONS", "10")
DB_AUTO_DELETE = is_enabled((environ.get('DB_AUTO_DELETE', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'm_house786')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🏷 <b>Title</b>: <a href={url}>{title}</a>\n🎭<b> 𝐆𝐞𝐧𝐫𝐞𝐬​</b>: {genres}</a>\n📆 <b>𝐘𝐞𝐚𝐫​</b>: <a href={url}/releaseinfo>{year}</a></b>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"


SHORTENER_API = environ.get("SHORTENER_API", None)
LONG_MEGHA_URL = environ.get("LONG_MEGHA_URL", False)

REQ_GRP = int(environ.get('REQ_GRP', '-1001645795385'))
