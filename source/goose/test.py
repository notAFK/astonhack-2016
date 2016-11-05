import clan
import entity

jimmy = entity.Goose('Jimmy', 8000, 100, 0, entity.Location(40, 50))
print jimmy

geeseclan = clan.Clan(clan.generateClan(100))
print geeseclan

print 'DONE'
assert True
