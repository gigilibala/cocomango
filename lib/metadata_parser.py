import yaml


class PackageMetadata:
    def __init__(self, content: str) -> None:
        self._data = self._parse(content)

    def _parse(self, content: str) -> None:
        return yaml.load(content, Loader=yaml.UnsafeLoader)

    def __repr__(self) -> str:
        return yaml.dump(self._data)
