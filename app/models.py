import datetime as dt

from passlib.hash import pbkdf2_sha256

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    profile_image_url = db.Column(db.String, nullable=True, default=None)
    last_logged_at = db.Column(db.DateTime, default=None, nullable=True)
    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow)
    
    def __str__(self) -> str:
        return self.email

    def __repr__(self) -> str:
        return f"<User id={self.id} email={self.email}>"
    
    def __hash__(self) -> int:
        return hash((self.id, self.email))

    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return False

        return self.id == other.id and self.email == other.email

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
    
    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)
