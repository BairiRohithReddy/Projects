cache_store = {}

def check_cache(hash_key):
    return cache_store.get(hash_key)

def update_cache(hash_key, status):
    cache_store[hash_key] = status
