from rich import print as rprint  # noqa F401
from rich.console import Console
from rich.theme import Theme

_theme = Theme(
    {
        "info": "bright_blue",
        "success": "bright_green",
        "warning": "bright_yellow",
        "error": "bright_red",
    }
)

console = Console(theme=_theme)
