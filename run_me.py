import typing as t
from pathlib import Path

BASE_NAME = "py-template"
BASE_DESCRIPTION = "It's a Python project template!"
BASE_NAME_UNDERSCORE = BASE_NAME.replace("-", "_")


class TemplateSwap(t.NamedTuple):  # noqa: D101
    src: Path
    needs_hyphen: bool = False
    has_description: bool = False


SWAPS = (
    TemplateSwap(src=Path("./.ruff.toml")),
    TemplateSwap(src=Path("./pyproject.toml"), needs_hyphen=True, has_description=True),
    TemplateSwap(src=Path("./README.md"), needs_hyphen=True, has_description=True),
    TemplateSwap(src=Path("./tox.ini")),
)


def make_swaps(new_name: str, new_description: str) -> None:  # noqa: D103
    underscored_name = new_name.replace("-", "_")

    Path("./py_template").rename(underscored_name)
    for swap in SWAPS:
        full_src = swap.src.read_text()

        if swap.needs_hyphen:
            full_src = full_src.replace(BASE_NAME, new_name)
        else:
            full_src = full_src.replace(BASE_NAME_UNDERSCORE, underscored_name)

        if swap.has_description:
            full_src = full_src.replace(BASE_DESCRIPTION, new_description)

        swap.src.write_text(full_src)


if __name__ == "__main__":
    new_name = input("New Package Name (hyphenated): ")
    new_description = input("New Package Description: ")

    make_swaps(new_name, new_description)
    Path(__file__).unlink()
