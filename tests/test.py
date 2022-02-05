from Kavita import Kavita
import json

config = json.load(open("test_config.json","r"))

k = Kavita(url=config["url"],apiKey=config["api"])
