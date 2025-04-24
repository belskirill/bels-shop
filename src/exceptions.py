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