#!/usr/bin/python3

class Config():
    FLASK_DEBUG_MODE = True

    conn_data = {
        'host': 'localhost',
        'port': 6379,
        'db': 0,
    }

    def get(self, key):
        return self.conn_data.get(key)


#Export Config instance
cfg = Config()
