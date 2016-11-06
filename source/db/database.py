from crate import client


class Database:
    def __init__(self, crateServer):
        self.server = crateServer

    '''
    Create database to store geese
    '''
    def Create(self):
        connection = client.connect(self.server)
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE geese(" +
            "ID int PRIMARY KEY,"+
            "HASHID string,"+
            "LIFESPAN float,"+
            "AGE int,"+
            "HUNGER float,"+
            "LOCATION_X float,"+
            "LOCATION_Y float,"+
	    "IS_ALIVE boolean,"+
	    "RANGE float,"+
	    "MIGRATION int,"+
            "HEALTH int," +
   	    "GENDER int)"
        )

    '''
    Save function for geese table
    Accesses crate on ip provided and saves _geeseArray in it
    '''
    def Save(self, geeseArray):
        connection = client.connect(self.server)
        cursor = connection.cursor()
        for bird in geeseArray:
	    if bird.saved:
		command = "UPDATE geese SET HASHID = '" + bird.hashid 
		command += "' , LIFESPAN = " + str(bird.lifespan)
		command += ", AGE = " + str(bird.age)
		command += ", HUNGER = " + str(bird.hunger)
		command += ", LOCATION_X = " + str(bird.location.x)
		command += ", LOCATION_Y = " + str(bird.location.y)
                command += ", IS_ALIVE = " + str(bird.isAlive)
		command += ", MIGRATION = " + str(bird.migrateCounter)
		command += ", RANGE = " + str(bird.range)
		command += ", HEALTH = " + str(bird.health)
		command += ", GENDER = " + str(bird.gender) + " "
		command += "WHERE ID = " + str(bird.id)
		cursor.execute(command)
	    else:
		command = "INSERT INTO geese (ID, HASHID, LIFESPAN, AGE, HUNGER"
		command += ", LOCATION_X, LOCATION_Y, HEALTH, GENDER, "
		command += "IS_ALIVE, RANGE, MIGRATION) "
		command += "VALUES( " + str(bird.id) + ", '" + bird.hashid + "', "
		command += str(bird.lifespan) + ", "
		command += str(bird.age) + ", " + str(bird.hunger) + ", "
		command += str(bird.location.x) + ", "
		command += str(bird.location.y) +  ", " + str(bird.health)  + ", "
		command += str(bird.gender) + ", " + str(bird.isAlive)  + ", "
		command += str(bird.range) + ", " + str(bird.migrateCounter) + ")"
		cursor.execute(command)
		result = cursor.fetchone()
		bird.saved = True

    '''
    Load function for geese table
    Accesses crate on ip provided and loads it into geeseArray
    Empties the presented array and populates it with geese data
    '''
    def FetchGeese(self):
        connection = client.connect(self.server)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM geese limit 1000000")
	result = cursor.fetchall()
	return result

    def FetchLocations(self):
	connection = client.connect(self.server)
        cursor = connection.cursor()
        cursor.execute("SELECT LOCATION_X, LOCATION_Y FROM geese limit 1000000")
	result = cursor.fetchall()
	return result
	
    def Delete(self):
	connection = client.connect(self.server)
        cursor = connection.cursor()
        cursor.execute("""
        DROP TABLE geese
        """);
