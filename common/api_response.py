from enum import Enum


class ApiResponse(Enum):
    SUCCESS = ("S00", "성공")
    NO_DATA_REQUIRED = ("E24", "필수 값이 없습니다.")
    JSON_DECODE_ERROR = ("E90", "유효하지 않은 JSON 형태입니다.")

    def __init__(self, code, msg):
        self.code = code
        self.msg = msg