from typing import List

from src.shared.domain.entities.user import User
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class UserRepositoryMock(IUserRepository):
    _instance = None
    _initialized = False
    
    users: List[User]

    def __new__(cls, use_singleton: bool = True, *args, **kwargs):
        if not use_singleton:
            return super().__new__(cls)
            
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, use_singleton: bool = True):
        if use_singleton and self._initialized:
            return
        
        if not self._initialized:
            self.users = [
                User(name="Bruno Soller", email="soller@soller.com", user_id="1", state=STATE.APPROVED),
                User(name="Vitor Brancas", email="brancas@brancas.com", user_id="2", state=STATE.REJECTED),
                User(name="João Vilas", email="bruno@bruno.com", user_id="3", state=STATE.PENDING)
            ]
            self._initialized = True

    def get_user(self, user_id: str) -> User:
        for user in self.users:
            if user.user_id == user_id:
                return user
        raise NoItemsFound("user_id")

    def get_all_user(self) -> List[User]:
        return self.users

    def create_user(self, new_user: User) -> User:
        self.users.append(new_user)
        return new_user

    def delete_user(self, user_id: str) -> User:
        for idx, user in enumerate(self.users):
            if user.user_id == user_id:
                return self.users.pop(idx)

        raise NoItemsFound("user_id")

    def update_user(self, user_id: str, new_name: str) -> User:
        for user in self.users:
            if user.user_id == user_id:
                user.name = new_name
                return user

        raise NoItemsFound("user_id")

