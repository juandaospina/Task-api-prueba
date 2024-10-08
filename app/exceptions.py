import typing as t

class ObjectNotFound(Exception):
    _status_code = 404
    _message = "Objecto no encontrado"

    def __init__(
            self, 
            message: t.Optional[str] = None, 
            status_code: t.Optional[int] = None, 
            payload: t.Optional[t.Dict] = None
        ) -> None:
        Exception.__init__(self, message)
        self.message = message if message is not None else self._message
        self.status_code = status_code if status_code is not None else self._status_code
        self.payload = payload

    def to_dict(self):
        _response = dict(self.payload or ())
        _response["message"] = self.message
        _response["status_code"] = self.status_code
        return _response
    

class Unauthorized(Exception):
    status_code = 401
    message = "Usuario no autorizado"

    def to_dict(self):
        response = dict(())
        response["message"] = self.message
        response["status_code"] = self.status_code
        return response