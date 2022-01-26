import datetime as dt

from libs.database import (
    Column,
    Model,
    SurrogatePK,
    db,
    reference_col,
    relationship,
)

from authlib.integrations.sqla_oauth2 import OAuth2TokenMixin


class OAuth2Token(SurrogatePK, Model, OAuth2TokenMixin):
    """A Company has many users"""

    __tablename__ = "oauth2_tokens"
    user_id = reference_col("users", nullable=False, column_kwargs={'index': True})
    user = relationship("User", back_populates="oauth2_token")
    auth_code = Column(db.String(256), unique=False, nullable=True)


    def __init__(self, **kwargs):
        """Create instance."""
        db.Model.__init__(self, **kwargs)

