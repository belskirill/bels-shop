from fastapi import HTTPException

class BelsShopException(Exception):
    detail = "Неожиданная ошибка"

    def __init__(self, *args, **kwargs):
        super().__init__(self.detail, *args, **kwargs)


class UserAlreadyExists(BelsShopException):
    detail = "Пользователь уже существует!"


class UserAlreadyExistsException(BelsShopException):
    detail = "Пользователь уже существует!"

class FailRegisterException(BelsShopException):
    detail = "Не удалось зарегистрироваться"


class IncorrectPasswordException(BelsShopException):
    detail = "Вы не ввели пароль!"



class FailedPasswordException(BelsShopException):
    detail = "Неверный пароль!"


class UserNotFondException(BelsShopException):
    detail = "Пользователь не найден!"

class ShopNotFoundEception(BelsShopException):
    detail = "Магазин не найден!!"


class NoResultFoundException(BelsShopException):
    detail = "Нет магазинов на проверку"


class PasswordChangeNotFoundException(BelsShopException):
    detail = "Заявка не найдена!"


class UserNofFoundException(BelsShopException):
    detail = "Пользователь не найден!"

class RuntimeErrorException(BelsShopException):
    detail = "Ошибка при загрузке файла!"

class DubliateShopException(BelsShopException):
    detail = "Такой магазин уже существует!"





class BelsHotelHTTPException(HTTPException):
    status_code = 500
    detail = None

    def __init__(self, *args, **kwargs):
        super().__init__(status_code=self.status_code, detail=self.detail)



class UserAlreadyExistsHTTPException(BelsHotelHTTPException):
    detail = "Такой пользователь уже существует!"
    status_code = 409


class FailRegisterHTTPException(BelsHotelHTTPException):
    detail = "Произошла ошибка при регистрации!"
    status_code = 400

class IncorrectPasswordHTTPException(BelsHotelHTTPException):
    detail = "Вы не ввели пароль!"
    status_code = 401


class FailedPasswordHTTPException(BelsHotelHTTPException):
    detail = "Неверный пароль!"
    status_code = 401

class UserNotFondHTTPException(BelsHotelHTTPException):
    detail = "Пользователь не найден!"
    status_code = 401


class ShopNotFoundHTTPException(BelsHotelHTTPException):
    detail = "Магазин не найден!"
    status_code = 401

class UserNofFoundHTTPException(BelsHotelHTTPException):
    detail = "Пользователь не найден!"
    status_code = 401

class RuntimeErrorHTTPException(BelsHotelHTTPException):
    detail = "Ошибка при загрузке фото!"
    status_code = 409


class PasswordChangeNotFoundHTTPException(BelsHotelHTTPException):
    detail = "Заявка не найдена!"
    status_code = 401

class MyShopNotFoundHTTPException(BelsHotelHTTPException):
    detail = "У вас нет магазина!!"
    status_code = 401

class DubliateShopHTTPException(BelsHotelHTTPException):
    detail = "Такой магазин уже существует!"
    status_code = 409


class ErrorFormatImageHTTPException(BelsHotelHTTPException):
    detail = "Неверный формат изображения!!"
    status_code = 409

class NoResultFoundHTTPException(BelsHotelHTTPException):
    status_code = 401
    detail = "Нет магазинов на проверку"


