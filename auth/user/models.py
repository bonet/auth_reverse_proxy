import datetime as dt

from libs.database import (
    Column,
    Model,
    SurrogatePK,
    db,
    reference_col,
    relationship,
)

class User(SurrogatePK, Model):
    """A Company has many users"""

    __tablename__ = "users"
    email = Column(db.String(80), unique=True, nullable=False)
    password = Column(db.LargeBinary(128), nullable=True)

    fullname = Column(db.String(256), unique=False, nullable=True)
    address = Column(db.String(256), unique=False, nullable=True)
    phone = Column(db.String(20), unique=False, nullable=True)
    oauth2_token = relationship("OAuth2Token", back_populates="user")
    created_at = Column(db.DateTime, nullable=True, default=dt.datetime.utcnow)
    updated_at = Column(db.DateTime, nullable=True, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow)


    def __init__(self, **kwargs):
        """Create instance."""
        db.Model.__init__(self, **kwargs)

