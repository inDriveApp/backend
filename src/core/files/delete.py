from shutil import rmtree

from fastapi import HTTPException

from src.models.dtos.file import FileDTO


def delete(dto: FileDTO):
    return 'WIP'
