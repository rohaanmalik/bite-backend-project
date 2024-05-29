import time
import threading
class MiniRedis:
    def __init__(self):
        self.store = {}
        self.expiration = {}
        self.lock = threading.Lock()
    
    def set(self, key, value):
        """ Stores the key-value pair in the database"""
        with self.lock:
            self.store[key] = value
            if key in self.expiration:
                del self.expiration[key]
            return "OK"

    def get(self, key):
        """ Retrieves the value associated with the key."""
        with self.lock:
            if key in self.expiration and time.time() > self.expiration[key]:
                del self.store[key]
                del self.expiration[key]
                return "nil"
            if key in self.store:
                return self.store[key]
            return "nil"
    
    def delete(self, key):
        """ Deletes the key-value pair from the database."""
        with self.lock:
            if key in self.store:
                del self.store[key]
                if key in self.expiration:
                    del self.expiration[key]
                return 1
            return 0
