import sqlite3

def create_tables():
    conn = sqlite3.connect("hotel_systems.db")
    cursor = conn.cursor()

    tables = [
        ("guest",
         """
         CREATE TABLE IF NOT EXISTS guest (
             guestID TEXT PRIMARY KEY,
             first_name TEXT,
             last_name TEXT,
             email TEXT,
             phone TEXT,
             address TEXT
         )
         """
        ),
        ("room",
         """
         CREATE TABLE IF NOT EXISTS room (
             room_number INTEGER PRIMARY KEY,
             room_type TEXT,
             beds INTEGER,
             capacity INTEGER,
             rate_per_night REAL
         )
         """
        ),
        ("reservation",
         """
         CREATE TABLE IF NOT EXISTS reservation (
             reservation_id INTEGER PRIMARY KEY,
             guest_id INTEGER,
             room_number INTEGER,
             check_in DATETIME,
             check_out DATETIME,
             reservation_date DATETIME,
             FOREIGN KEY (guest_id) REFERENCES guest (guestID),
             FOREIGN KEY (room_number) REFERENCES room (room_number)
         )
         """
        ),
        ("services",
         """
         CREATE TABLE IF NOT EXISTS services (
             service_id INTEGER PRIMARY KEY,
             service_name TEXT,
             description TEXT,
             price REAL
         )
         """
        ),
        ("payments",
         """
         CREATE TABLE IF NOT EXISTS payments (
             payment_id INTEGER PRIMARY KEY,
             reservation_id INTEGER,
             amount REAL,
             payment_date DATETIME,
             FOREIGN KEY (reservation_id) REFERENCES reservation (reservation_id)
         )
         """
        ),
        ("reservation_service",
         """
         CREATE TABLE IF NOT EXISTS reservation_service (
             reservation_id INTEGER,
             service_id INTEGER,
             PRIMARY KEY (reservation_id, service_id),
             FOREIGN KEY (reservation_id) REFERENCES reservation (reservation_id),
             FOREIGN KEY (service_id) REFERENCES services (service_id)
         )
         """
        ),
        ("staff_data",
         """
         CREATE TABLE IF NOT EXISTS staff_data (
             staff_id INTEGER PRIMARY KEY,
             first_name TEXT,
             last_name TEXT,
             email TEXT,
             phone TEXT,
             position TEXT,
             department TEXT,
             is_manager INTEGER,
             created_at DATETIME
         )
         """
        )
    ]

    for table_name, create_statement in tables:
        cursor.execute(create_statement)
        print(f"{table_name} table created.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
