import asyncio

try:
    from typing import Awaitable
except ImportError:
    from types import GeneratorType as Awaitable


class AIOFile:
    def __init__(self, filename: str, mode:str="r",
                 access_mode:int=0x644, loop: asyncio.AbstractEventLoop=None): ...
    def __repr__(self) -> str: ...

    def read(self, size: int=-1, offset: int=0, priority: int=0) -> AIOOperation: ...

    def write(self, data: (str, bytes), offset:int=0, priority:int=0) -> AIOOperation: ...

    def flush(self, priority:int=0) -> AIOOperation: ...


class AIOOperation:
    def __init__(self, state: int, aio_file: AIOFile, offset: int, nbytes: int, reqprio: int): ...
    def run(self): ...
    def poll(self) -> bool: ...
    def result(self) -> bytes: ...
    def close(self): ...

    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...

    @property
    def nbytes(self) -> int: ...

    @property
    def offset(self) -> int: ...

    @property
    def reqprio(self) -> int: ...

    @property
    def buffer(self) -> bytes: ...

    @buffer.setter
    def buffer(self, data: bytes): ...

    @property
    def closed(self) -> bool: ...

    def __await__(self) -> Awaitable: ...
    def __iter__(self) -> "AIOOperation": ...

    __next__ = __await__
