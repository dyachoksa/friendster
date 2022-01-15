import uuid

from passlib.hash import pbkdf2_sha256

class User:
    def __init__(self, email=None, name=None, **kwargs):
        self.id = uuid.uuid4()
        self.email = email
        self.name = name
        self.password = kwargs.get("password")
    
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
        return self.email
    
    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)

    def save(self):
        users.append(self)


users = [
    User(email="sergey@example.com", name="Sergey", password=pbkdf2_sha256.hash("password")),
    User(email="user@test.com", name="Test User", password=pbkdf2_sha256.hash("password")),
]


def get_user_by_email(email: str):
    for user in users:
        if user.email == email:
            return user
    
    return None
