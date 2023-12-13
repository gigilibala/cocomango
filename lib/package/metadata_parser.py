import yaml


class PackageMetadata:
    def __init__(self) -> None:
        try:
            with open("package.yaml", "r", encoding="utf-8") as f:
                self._content = f.read()
        except:
            print("Failed to read package.yaml. Make sure there is such file.")
            exit(1)

        self._parse(self._content)

    def _parse(self, content: str) -> None:
        self._data = yaml.load(content, Loader=yaml.UnsafeLoader)

    def __repr__(self) -> str:
        return yaml.dump(self._data)
