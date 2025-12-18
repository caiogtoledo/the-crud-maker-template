import pytest

from src.modules.delete_user.app.delete_user_usecase import DeleteUserUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.mock.user_repository_mock import UserRepositoryMock


class Test_DeleteUserUsecase:
    def test_delete_user(self):
        repo = UserRepositoryMock()
        usecase = DeleteUserUsecase(repo)

        lenBefore = len(repo.users)

        user = usecase("2")

        assert len(repo.users) == lenBefore - 1

    def test_delete_user_not_found(self):
        repo = UserRepositoryMock()
        usecase = DeleteUserUsecase(repo)

        with pytest.raises(NoItemsFound):
            user = usecase("69")

    def test_delete_user_invalid_id(self):
        repo = UserRepositoryMock()
        usecase = DeleteUserUsecase(repo)

        with pytest.raises(EntityError):
            user = usecase(1)
