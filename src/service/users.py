import uuid
from datetime import datetime, timedelta

import logging

from src.exceptions import UserNotFondException, FailedPasswordException, PasswordChangeNotFoundException, \
    UserNofFoundException, RuntimeErrorException
from src.schemas.users import UserPasswordChache
from src.service.auth import AuthService
from src.service.base import BaseService
from src.tasks.tasks import info_update_password
from src.time import download_image_user


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

        await self.db.password_change.delete_not_confirm_user(user.id)
        await self.db.password_change.add_data(password_change_tokens)
        await self.db.commit()
        info_update_password.delay(user.email)
        # TODO: добавить обработку ошибок
        # TODO: имитация перехода по ссылке,
        #  отдельная ручка как будто фронт отправляет что пользователь подтвердил


    async def change_confirmed_password(self, user_id):
        try:
            user = await self.db.password_change.get_data(user_id)
            if user.expires_at < datetime.utcnow():
                raise ... # время ожидания истекло
            await self.db.users.update_password(user.user_id, user.new_password_hash)
            await self.db.password_change.edit_data(user.id)
            await self.db.commit()
            logging.warning(user)
        except PasswordChangeNotFoundException:
            raise PasswordChangeNotFoundException

    async def edit_base_info(self, user_id, data):
        try:
            user = await self.db.users.user_edit_info(user_id, data)
            await self.db.commit()
            return user
        except UserNofFoundException:
            raise UserNofFoundException


    async def get_user_base_info(self, user_id):
        try:
            user = await self.db.users.get_user_base_info_model(user_id)
            return user
        except UserNofFoundException:
            raise UserNofFoundException


    async def edit_photo(self, user, file):
        try:
            link = await download_image_user(file)
            await self.db.users.edit_link(user, link_photo=link)
            await self.db.commit()
            return link
        except UserNofFoundException:
            raise UserNofFoundException
        except RuntimeError:
            raise RuntimeErrorException



