import sqlite3
import uuid

def seed_db(conn:sqlite3.Connection)-> bool:
    try:
        id = uuid.uuid4()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO remember (id, tag, command, description) 
                       VALUES (?, ?, ?, ?)""", 
                       (str(id), "ls", "remember ls", "All remember commands on this system"))
        conn.commit()
        print("DB seeded")
        return True 
    except Exception as e:
        print(f"Something went wrong at create_db() :( {str(e)}")
        return False

def create_db()-> bool:
   try:
        conn = sqlite3.connect("remember.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS remember(id VARCHAR(255), tag VARCHAR(255), command VARCHAR(255), description VARCHAR(1000))")
        conn.commit()
        return seed_db(conn)
   except Exception as e:
       print(f"Something went wrong at create_db() :( {str(e)}")
       return False
   finally:
       conn.close()
       
    
def parse_input_command(command:str)-> bool:
   try:
        command_list = command.split()
        if command_list[0] == 'remember' and create_db():
            print(command_list)
            return True
        else:
            print('fuck you')
        return False
   except Exception as e:
       print(f"Something went wrong at parse_input_command() :( {str(e)}")
       
    
def main():
    command = input("")
    parse_input_command(command)

if __name__ == "__main__":
    main()