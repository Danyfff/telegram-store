from .db_manager import DBManager

class DB(DBManager):
    def __init__(self):
        super().__init__()

    # Запросы связвнные с пользователями
    def get_user(self, telegram_id: int):
        '''Проверка на существование пользователя в системе'''
        
        req = self.execute("SELECT * "
                "FROM users "
                "WHERE telegram_id= ? ",
                args=(telegram_id, ), many=False)
        
        if req['code'] == 200:
            return True
        else:
            return False

    def create_user(self, telegram_id, post='user'):
        '''Создание нового пользователя'''
        
        req = self.execute("INSERT INTO users(telegram_id, post) "
                       "VALUES (?, ?) ", 
                       args=(telegram_id, post, ), many=False)
        return req
    
    def get_user_post(self, telegram_id: int):
        '''Проверка на существование пользователя в системе'''
        
        req = self.execute("SELECT post "
                "FROM users "
                "WHERE telegram_id= ? ",
                args=(telegram_id, ), many=False)
        
        if req['code'] == 200:
            return req['data'][0]


    # Запросы к категориям
    def get_all_categories(self):
        '''Получение списка всех категорий'''
        
        req = self.execute("SELECT * "
                "FROM categories ")
        return req
    
    def get_categories_by_id(self, id):
        '''Получение категории по его id'''
        
        req = self.execute("SELECT name "
                "FROM categories "
                "WHERE id= ? ",
                args=(id, ), many=False)
        return req
        
    def create_category(self, name):
        '''Создание новой категории'''
        
        req = self.execute("INSERT INTO categories(name) "
                       "VALUES (?) ", 
                       args=(name,), many=False)
        return req
    
    def delete_category(self, id):
        '''Удаление категории'''
        
        req = self.execute("DELETE FROM categories "
                         "WHERE id = ?",
                        args=(id, ), many=False)
        return req
    

    # Запросы связвнные с товарами
    def get_all_items(self):
        '''Получение списка всех товаров'''
        
        req = self.execute("SELECT * "
                "FROM items ")
        return req 
    
    def get_all_items(self, id_categori):
        '''Получение списка всех товаров с определенной категорией'''
        
        req = self.execute("SELECT * "
                "FROM items "
                "WHERE id_category= ? ",
                args=(id_categori, ))
        return req
    
    def create_item(self, name, price, descript, id_category):
        '''Создание нового товара'''
        
        req = self.execute("INSERT INTO items(name, price, descript, id_category) "
                       "VALUES (?, ?, ?, ?) ", 
                       args=(name, price, descript, id_category, ), many=False)
        return req
    
    def delete_item(self, id):
        '''Удаление товара'''
        
        req = self.execute("DELETE FROM items "
                         "WHERE id = ?",
                        args=(id, ), many=False)
        return req
        
    
db = DB()