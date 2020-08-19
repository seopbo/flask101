db = {
    "user": "root",
    "password": "Qh132042!",
    "host": "localhost",
    "port": 3306,
    "database": "miniter"
}
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
