import logging
import uuid
from datetime import datetime, timedelta

from src.exceptions import UserNotFondException, FailedPasswordException
from src.schemas.users import UserPasswordChache
from src.service.auth import AuthService
from src.service.base import BaseService


class UsersService(BaseService):
    async def request_password_change(self, user, data):
        user = await self.db.users.get_user(user)
        if not user:
            raise UserNotFondException
        if not AuthService().verify_password(
            data.old_password, user.password
        ):
            raise FailedPasswordException

        new_password = AuthService().hash_password(data.new_password)
        token = str(uuid.uuid4())
        password_change_tokens = UserPasswordChache(
            user_id=user.id,
            token=token,
            new_password_hash=new_password,
            expires_at=datetime.utcnow() + timedelta(hours=1),
            is_used=False,
        )

        await self.db.password_change.add_data(password_change_tokens)
        await self.db.commit()
        # TODO: добавить обработку ошибок
        # TODO: добавить celery задачу для отправки письма на почту кто изменил пароль
        # TODO: имитация перехода по ссылке,
        #  отдельная ручка как будто фронт отправляет что пользователь подтвердил


