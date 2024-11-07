import sqlite3

def create_db():
    try:
        # Connect to the database
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        # Create the course table if it doesn't exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS course (
                cid INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                duration TEXT,
                charges TEXT,
                description TEXT
            )
        """)
        con.commit()


        cur.execute("""
            CREATE TABLE IF NOT EXISTS student (
                roll INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                gender TEXT,
                dob TEXT,
                contact TEXT,
                addmission TEXT,
                course TEXT,
                state TEXT,
                city TEXT,
                pin TEXT,
                address TEXT
            )
        """)
        con.commit()


        cur.execute("""
            CREATE TABLE IF NOT EXISTS result (
                rid INTEGER PRIMARY KEY AUTOINCREMENT,
                roll TEXT,
                name TEXT,
                course TEXT,
                marks_ob TEXT,
                full_marks TEXT,
                per TEXT
            )
        """)
        con.commit()


        cur.execute("""
            CREATE TABLE IF NOT EXISTS result (
                rid INTEGER PRIMARY KEY AUTOINCREMENT,
                roll TEXT,
                name TEXT,
                course TEXT,
                marks_ob TEXT,
                full_marks TEXT,
                per TEXT
            )
        """)
        con.commit()

        



        print("Database and table created successfully.")

    except Exception as e:
        print(f"Error creating database: {e}")

    finally:
        # Close the connection
        if con:
            con.close()

# Call the function to create the database
if __name__ == "__main__":
    create_db()