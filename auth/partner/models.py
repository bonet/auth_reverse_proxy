import datetime as dt

from libs.database import (
    Column,
    Model,
    SurrogatePK,
    db,
    reference_col,
    relationship,
)

class Partner(SurrogatePK, Model):
    """A Company has many users"""

    __tablename__ = "partners"
    name = Column(db.String(256), unique=False, nullable=True)
    secret_key = Column(db.String(256), unique=False, nullable=True)
    scopes = Column(db.JSON, nullable=True, default='{}', server_default='{}')
    oauth2_token = relationship("OAuth2Token", back_populates="partner")
    created_at = Column(db.DateTime, nullable=True, default=dt.datetime.utcnow)
    updated_at = Column(db.DateTime, nullable=True, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow)


    def __init__(self, **kwargs):
        """Create instance."""
        db.Model.__init__(self, **kwargs)

