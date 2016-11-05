from crate import client


class Database:
    def __init__(self, crateServer):
        self.server = crateServer

    '''
    Create database to store geese
    '''
    def Create(self):
        connection = client.connect(crateServer)
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE geese(
            ID int PRIMARY KEY,
            HASHID string,
            LIFESPAN float,
            AGE int,
            HUNGER float,
            LOCATION_X float,
            LOCATION_Y float,
	    IS_ALIVE boolean,
	    RANGE float,
	    MIGRATION int,
            HEALTH int,
   	    GENDER int
        );
        """)

    '''
    Save function for geese table
    Accesses crate on ip provided and saves _geeseArray in it
    '''
    def Save(self, geeseArray):
        connection = client.connect(crateServer)
        cursor = connection.cursor()
        for bird in geeseArray:
	    if bird.saved:
		cursor.execute("""
	        UPDATE geese
		SET HASHID = '""" + bird.hashid + """
		' , LIFESPAN = """ + bird.lifespan + """ 
		, AGE = """ +bird.age + """
		, HUNGER = """ + bird.hunger + """
		, LOCATION_X = """ + bird.location.x + """
		, LOCATION_Y = """ + bird.location.y + """
                , IS_ALIVE = """ + goose.is + """
		, HEALTH = """ + goose.health + """
		, GENDER = """ + goose.gender + """
		WHERE ID = """ + goose.id);
	    else:
		cursor.execute("""
	        INSERT INTO geese (ID, HASHID, LIFESPAN, AGE, HUNGER""" + """
		, LOCATION_X, LOCATION_Y, HEALTH, GENDER)""" + """ 
		VALUES( """ + goose.id + ", '" + goose.lifespan + "', " +
		
		SET HASHID = '""" + goose.hashid + """
		' , LIFESPAN = """ + goose.lifespan + """ 
		, AGE = """ + goose.age + """
		, HUNGER = """ + goose.hunger + """
		, LOCATION_X = """ + goose.location.x + """
		, LOCATION_Y = """ + goose.location.y + """
		, HEALTH = """ + goose.health + """
		, GENDER = """ + goose.gender + """
		WHERE ID = """ + goose.id); 

    '''
    Load function for geese table
    Accesses crate on ip provided and loads it into _geeseArray
    '''
    def Load(self, _geeseArray):
        connection = client.connect(crateServer)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM geese
        """);
