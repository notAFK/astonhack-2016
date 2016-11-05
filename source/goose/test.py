import clan
import entity

jimmy = entity.Goose('Jimmy', 0, 8000, 100, 100, entity.Location(0, 0), 'male')
print jimmy
print jimmy.health, jimmy.lifespan

for i in range(1000):
    jimmy.decayLifespan()

print jimmy.health, jimmy.lifespan
jimmy.health -= 50
print jimmy.health

for i in range(1000):
    jimmy.decayLifespan()

print jimmy.health, jimmy.lifespan


print 'DONE'
assert True
