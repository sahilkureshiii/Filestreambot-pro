# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '19835762'))
    API_HASH = str(getenv('API_HASH', '107b55bccb14cad585c69553e0b7be5c'))
    BOT_TOKEN = str(getenv('BOT_TOKEN','7102947390:AAGTjir-IvgtNDaAl3PFtapRACC9vy-5fk0'))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002068662847'))
    PORT = int(getenv('PORT', '22'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '67.219.139.52'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1332840810").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Skeventbharatpur'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', '67.219.139.52:22')) if not ON_HEROKU or getenv('FQDN', '67.219.139.52:22') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://testy-haddock-sisa-5f717a8a.koyeb.app/"
    else:
        URL = "https://testy-haddock-sisa-5f717a8a.koyeb.app/"
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://sahilkureshi8117:mongodb+srv://sahilkureshi8117:SMARTY786skyt@cluster0.iacbhvy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'Cuteanime811'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
