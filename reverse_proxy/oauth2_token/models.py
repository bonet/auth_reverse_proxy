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
    @classmethod
    def find_by_access_token(self, session, access_token, user_id):
        res = session.execute(f"SELECT * FROM oauth2_tokens WHERE access_token='{access_token}' AND user_id='{user_id}'")
        token = res.fetchone()
        return token

