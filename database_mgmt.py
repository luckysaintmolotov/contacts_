import sqlite3, datetime,random
from contact_creation import fake_contact 
from contact_creation import list_of_many_fakes
file_path = f"databases/{datetime.date.today()}.db"
gender = ["male","female","unisex"]
amount = random.randint(10,25)
contact = fake_contact(random.choice(['male','female','unisex']))
_list = list_of_many_fakes(amount,gender)
def create_contact_database():
    file_path = f"databases/{datetime.date.today()}.db"
    print(file_path)
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            middle_name TEXT,
            last_name TEXT,
            nickname TEXT,
            title TEXT,
            company TEXT,
            job_title TEXT,
            department TEXT,
            phone_home TEXT,
            phone_mobile TEXT,
            phone_work TEXT,
            phone_fax TEXT,
            address_home_street TEXT,
            address_home_city TEXT,
            address_home_country TEXT,
            birthday TEXT,
            website TEXT,
            notes TEXT,
            relationship TEXT,
            custom_fields TEXT
        )
    """)
    conn.commit()
    conn.close()
    return file_path

def insert_fake_new_contact(filepath, contact):
    conn = sqlite3.connect(filepath)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO contacts (
            first_name, middle_name, last_name, nickname, title, company, job_title, department,
            phone_home, phone_mobile, phone_work, phone_fax, address_home_street, address_home_city, address_home_country,
            birthday, website, notes, relationship, custom_fields
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, contact)
    conn.commit()
    conn.close()

def fill_with_many_fakes(filepath,list_of_fakes):
    conn = sqlite3.connect(filepath)
    cursor = conn.cursor()
    for fake in list_of_fakes:
        cursor.execute("""
        INSERT INTO contacts (
            first_name, middle_name, last_name, nickname, title, company, job_title, department,
            phone_home, phone_mobile, phone_work, phone_fax, address_home_street, address_home_city, address_home_country,
            birthday, website, notes, relationship, custom_fields
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, fake)
        conn.commit()
    conn.close()



create_contact_database()
insert_fake_new_contact(file_path,contact)
fill_with_many_fakes(file_path,_list)