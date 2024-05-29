import time
import threading
class MiniRedis:
    def __init__(self):
        self.store = {}
        self.expirations = {}
        self.lock = threading.Lock()
    
    def set(self, key, value):
        """ Stores the key-value pair in the database"""
        with self.lock:
            self.store[key] = value
            if key in self.expirations:
                del self.expirations[key]
            return "OK"

    def get(self, key):
        """ Retrieves the value associated with the key."""
        with self.lock:
            if key in self.expirations and time.time() > self.expirations[key]:
                del self.store[key]
                del self.expirations[key]
                return "nil"
            if key in self.store:
                return self.store[key]
            return "nil"
    
    def delete(self, key):
        """ Deletes the key-value pair from the database."""
        with self.lock:
            if key in self.store:
                del self.store[key]
                if key in self.expirations:
                    del self.expirations[key]
                return 1
            return 0

    def expiration(self, key, seconds):
        """ Sets a timeout on the specified key. After the timeout has expired, the key should be deleted. """
        with self.lock:
            if key in self.store:
                self.expirations[key] = time.time() + seconds
                return "OK"
            return -1

    def ttl(self, key):
        "Returns the remaining time to live of a key that has an expiration set, in seconds."
        with self.lock:
            if key in self.store:
                if key in self.expirations:
                    if self.expirations[key] > time.time():
                        return self.expirations[key] - time.time() 
                    self.delete(key) # passive delete because it has expired
                    return -2 # now the key does not exist
                else:
                    return -1 # exists but no expiration 
            return -2