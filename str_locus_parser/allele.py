from typing import Any

OFF_LADDER_VALUES = ["OL",]
ALLOWED_CHARS = set('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.')

class AlleleValueError(ValueError):
    message = "Invalid allele value \"%s\""
    
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.message.format(self.value)


class UnnamedAlleleWasFound(AlleleValueError):
    message = "An unnamed allele was found \"%s\""


class Allele:
    def __init__(self, value: str) -> None:
        self._validate_value(value)
        self.__value = self._prepare_value(value)

    @property
    def value(self) -> str | None:
        return self.__value
    
    def _prepare_value(self, value: str) -> str:
        if "," in value:
            return self._replace_commas(value)
            
    def _validate_value(self, value: str) -> None:
        self._type_validator(value)
        self._value_validator(value)
        self._off_ladder_validator(value)

    @staticmethod    
    def _type_validator(value: str) -> Exception | None:
        if not isinstance(value, str):
            raise TypeError("Type error. The allele must be of type str")
        
    @staticmethod
    def _value_validator(value: str) -> Exception | None:
        if not set(value).issubset(ALLOWED_CHARS):
            raise AlleleValueError(value)


    @staticmethod    
    def _off_ladder_validator(value: str) -> Exception | None:
        if value in OFF_LADDER_VALUES:
            raise UnnamedAlleleWasFound(value)
    
    @staticmethod    
    def _replace_commas(value: str) -> str:
        return value.replace(",", ".", -1)




