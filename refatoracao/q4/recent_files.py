from __future__ import annotations

from typing import Iterator


class RecentFiles:

    def __init__(self, limit: int):
        self._files: list[str] = []
        self._limit = limit

    def add_file(self, path: str) -> None:
        if path in self._files:
            self._files.remove(path)
        self._files.insert(0, path)
        while len(self._files) > self._limit:
            self._files.pop()

    def __len__(self) -> int:
        return len(self._files)

    def __getitem__(self, index: int) -> str:
        return self._files[index]

    def __iter__(self) -> Iterator[str]:
        return iter(self._files)

    def __contains__(self, path: object) -> bool:
        return path in self._files
