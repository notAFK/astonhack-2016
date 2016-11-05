from goose.clan import Clan
from db.database import Database
from goose.clan import generateRandomClan
db = Database("10.0.2.15:4200")
testClan = Clan(generateRandomClan(10, 0, 0))
db.Save(testClan.geese) 
