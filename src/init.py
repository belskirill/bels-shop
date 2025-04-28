from src.connectors.redis_connectors import RedisManager
from src.config import settigns

redis_manager = RedisManager(host=settigns.REDIS_HOST, port=settigns.REDIS_PORT)