import hashlib
from db_utils import get_user_by_hash, insert_user
from cache_utils import check_cache, update_cache

def get_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def username_exists(username):
    hash_key = get_hash(username)

    # Check cache first
    cached_status = check_cache(hash_key)
    if cached_status == "taken":
        return True
    elif cached_status == "available":
        return False

    # If not in cache → check DB
    user = get_user_by_hash(hash_key)
    if user:
        update_cache(hash_key, "taken")
        return True
    else:
        update_cache(hash_key, "available")
        return False

def register_user(username, password):
    if username_exists(username):
        return False  # already exists

    username_hash = get_hash(username)
    password_hash = get_hash(password)
    insert_user(username, username_hash, password_hash)
    update_cache(username_hash, "taken")  # update cache after insert
    return True

def validate_login(username, password):
    username_hash = get_hash(username)
    password_hash = get_hash(password)
    user = get_user_by_hash(username_hash)
    if user and user[1] == password_hash:
        return True
    return False
