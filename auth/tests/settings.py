"""Settings module for test app."""
ENV = "development"
TESTING = True
SQLALCHEMY_DATABASE_URI = "postgres://some_user:some_pwd@oauth2-token-db-test:5432/auth_test"
BCRYPT_LOG_ROUNDS = (
    4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
)
DEBUG_TB_ENABLED = False
CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False
WTF_CSRF_ENABLED = False  # Allows form testing
PRESERVE_CONTEXT_ON_EXCEPTION = False
