import datetime as dt

from libs.database import (
    Column,
    Model,
    SurrogatePK,
    db,
    reference_col,
    relationship,
)

from libs.extensions import bcrypt

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


    def __init__(self, email, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, email=email, password=password, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

