import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1659820361:AAE47U6e1yQVVWel2M1uqz2_esUYbJXMdX4")

    APP_ID = int(os.environ.get("APP_ID", 1469098))

    API_HASH = os.environ.get("API_HASH", "f7d877ef7d619f858d8dc27ac7a121e5")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001404974777")
