from Hero.core.bot import HeroBot
from Hero.core.dir import dirr
from Hero.core.git import git
from Hero.core.userbot import Userbot
from Hero.misc import dbb, sudo
from aiohttp import ClientSession

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Load Sudo Users from DB
sudo()

# Bot Client
app = HeroBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
