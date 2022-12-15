import pathlib
from typing import Union, Optional, Callable

PathType = Union[str, pathlib.Path]

def my_sort(src: PathType, output: Optional[PathType]=None, reverse: bool=False,
		key: Optional[Callable]=None, nflows: int=1,
        bsize: Optional[int]=None, type_data: str = 's') -> None:
