import db


def add_item(glider_type, callsign, compsign, glider_class, options, user_id):
    sql = """INSERT INTO items (glider_type, callsign, compsign,
    glider_class, options, user_id) VALUES (?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [glider_type, callsign, compsign, glider_class, options, user_id])

def get_items():
    sql = """SELECT id, glider_type, callsign, compsign,
             glider_class, options FROM items ORDER BY id DESC"""
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT
            items.id,
            items.glider_type, items.callsign,
            items.compsign, items.glider_class,
            items.options, users.username,
            users.id user_id
            from items, users
            WHERE items.user_id = users.id
            AND items.id = ?"""
    return db.query(sql, [item_id])[0]

def update_item(item_id, glider_type, callsign, compsign, glider_class, options):
    sql = """UPDATE items SET glider_type = ?,
                    callsign = ?,
                    compsign = ?,
                    glider_class = ?,
                    options = ?
            WHERE   id = ?"""
    db.execute(sql, [glider_type, callsign, compsign, glider_class, options, item_id])