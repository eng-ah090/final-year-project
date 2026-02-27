from pathlib import Path


def parse_cst_export(path: str | Path) -> dict:
    """Parse a tiny key:value style text export."""
    parsed: dict[str, str] = {}
    for line in Path(path).read_text().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            parsed[key.strip()] = value.strip()
    return parsed
