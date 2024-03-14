#  connect to db
import app.db as db

#  create tables
def create_tables():
    db.insert('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    ''')
    db.insert('''
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            message TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

#  seed data
def seed_data():
    db.insert("INSERT INTO users (username, password) VALUES ('admin', 'admin')")
    db.insert("INSERT INTO users (username, password) VALUES ('user', 'user')")
    db.insert("INSERT INTO messages (user_id, message) VALUES (1, 'Hello, World!')")
    db.insert("INSERT INTO messages (user_id, message) VALUES (2, 'Hi there!')")

if __name__ == '__main__':
    create_tables()
    seed_data()
    print('Tables created and data seeded')
