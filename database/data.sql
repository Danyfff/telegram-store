CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INT,
    post VARCHAR(255)
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INT,
    descript TEXT,
    id_categori INT,
    FOREIGN KEY (id_category) REFERENCES categories(id)
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_item INT,
    id_buyer INT,
    order_date TEXT,
    status TEXT,
    descript TEXT,
    FOREIGN KEY (id_item) REFERENCES items(id),
    FOREIGN KEY (id_buyer) REFERENCES users(id)
);