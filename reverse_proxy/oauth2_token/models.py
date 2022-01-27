import datetime as dt

from libs.database import (
    Column,
    Model,
    SurrogatePK,
    db,
    reference_col,
    relationship,
)


class OAuth2Token():
    def __init__(self, auth):
        self.token = None

    @classmethod
    def find_by_access_token(self, session, access_token, user_id):
        self.token = session.execute("SELECT * FROM oauth2_tokens")

