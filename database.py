class InMemoryDB:
    def __init__(self):
        self.main_db = {}  
        self.transaction_db = None 

    def begin_transaction(self):
        if self.transaction_db is not None:
            raise Exception("Transaction already in progress")
        self.transaction_db = {}

    def put(self, key, val):
        if self.transaction_db is None:
            raise Exception("No active transaction")
        if type(key) != str:
            raise Exception("Key can only be a String")
        if type(val) != int:
            raise Exception("Value can only be an Integer")
        self.transaction_db[key] = val

    def get(self, key):
        if self.main_db and key in self.main_db:
            return self.main_db.get(key)
        return None

    def commit(self):
        if self.transaction_db is None:
            raise Exception("No active transaction to commit")
        self.main_db.update(self.transaction_db)
        self.transaction_db = None

    def rollback(self):
        if self.transaction_db is None:
            raise Exception("No active transaction to rollback")
        self.transaction_db = None


#Test cases 
if __name__ == "__main__":
    db = InMemoryDB()

    print(db.get("A"))

    try:
        db.put("A", 5)
    except Exception as e:
        print(e)

    db.begin_transaction()

    db.put("A", 5)

    print(db.get("A"))

    db.put("A", 6)

    db.commit()

    print(db.get("A"))

    try:
        db.commit()
    except Exception as e:
        print(e)

    try:
        db.rollback()
    except Exception as e:
        print(e)

    print(db.get("B"))

    db.begin_transaction()

    db.put("B", 10)

    db.rollback()

    print(db.get("B"))
