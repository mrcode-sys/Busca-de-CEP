from datetime import datetime, timedelta

def cache_is_valid(updated_at, ttl_hours):
    return updated_at >= datetime.now() - timedelta(ttl_hours)
