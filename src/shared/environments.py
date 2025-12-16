import os

class Environment:
    def __init__(self):
        self.env = self.get_env() or "local"

    def get_repositories(self):
        if self.env == "local":
            from src.shared.infra.repositories.mock.user_repository_mock import UserRepositoryMock

            return {
                "user_repo": UserRepositoryMock(),
            }

        elif self.env in ["dev", "hml", "prd"]:
            from src.shared.infra.repositories.mongodb.user_repository_mongo import UserRepositoryMongo

            return {
                "user_repo": UserRepositoryMongo("users", db_name_suffix=self.env),
            }
        else:
            raise Exception(f"Invalid environment: {self.env}")

    @staticmethod
    def get_env():
        return os.getenv("ENV")
