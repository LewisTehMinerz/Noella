#######################################
############# Config File #############
#######################################

from discord.ext import commands
from collections import Counter
from collections import OrderedDict, deque, Counter
from datetime import datetime as dt

import openweathermapy.core as owm
import cogs.utils.checks
import cogs.utils.db
import cogs.utils.formats
import time
import logging
import aiohttp
import discord
import sys
import asyncio
import datetime
import traceback
import copy
import unicodedata
import inspect
import os
import json

dev_discord = "https://discord.gg/EVfHKKn"

client_id   = 'BOTID' # your bot's client ID
token = 'TOKEN' # your bot's token
postgresql = 'postgresql://NAME:PASSWORD@LOCALHOST/DB' # your postgresql info from above

carbon_key = '' # your bot's key on carbon's site
bots_key = '' # your key on bots.discord.pw
openweathermap_api = "" # your key for OpenWeatherMap API
youtube_api = "" # your key for YouTube API
osu_api = "" # your key for osu! API
Mashape_API = "" # your key for Mashape API

embed_color = 13454262 #Default Embed Color
embed_color_succes = 65280 #Default SuccesEmbed Color
embed_color_error = 13434880 #Default ErrorEmbed Color
embed_color_attention = 16776960 #Default AttentionEmbed Color
message_delete_time = 15 #Default Message Delete Time
