from goose.clan import Clan
from db.database import Database
from goose.clan import generateRandomClan
from geesemanager import createGeese

db = Database("10.0.2.15:4200")
db.Delete()
db.Create()
geesearray = createGeese(1000)
testClan = Clan(geesearray)
db.Save(testClan.geese)
db.Save(testClan.geese)
