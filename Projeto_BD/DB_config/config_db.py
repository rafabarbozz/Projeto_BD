from configparser import ConfigParser

# Function that gets what is inside de file database.ini and associate to each
# variable
def config(filename="DB_config/database.ini", section="postgresql"):
    #creat parser
    parser = ConfigParser()
    
    #read config_file
    parser.read(filename)
    
    #get sextion, default to psql
    db = {}
    
    #check to see if the section (psql) exists
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]]= param[1]
            
    #return error if a param, is called and not listed in .ini file
    else:
        raise Exception(f"Sectio n {section} not found in {filename} file")
    
    return db # return a dictionary