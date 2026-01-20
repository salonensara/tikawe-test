CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    glider_type TEXT,
    callsign TEXT,
    compsign TEXT,
    glider_class INTEGER,
    options TEXT,
    user_id INTEGER REFERENCE users
);