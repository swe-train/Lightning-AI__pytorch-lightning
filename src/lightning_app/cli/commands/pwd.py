import os
import sys

from rich.live import Live
from rich.spinner import Spinner
from rich.text import Text

from lightning_app.cli.commands.cd import _CD_FILE
from lightning_app.utilities.app_helpers import Logger

logger = Logger(__name__)


def pwd() -> str:
    """Print your current working directory in the Lightning Cloud filesystem."""

    if sys.platform == "win32":
        print("`pwd` isn't supported on windows. Open an issue on Github.")
        sys.exit(0)

    with Live(Spinner("point", text=Text("pending...", style="white")), transient=True):

        root = _pwd()

    print(root)

    return root


def _pwd() -> str:
    root = "/"

    if not os.path.exists(_CD_FILE):
        with open(_CD_FILE, "w") as f:
            f.write(root + "\n")
    else:
        with open(_CD_FILE) as f:
            lines = f.readlines()
            root = lines[0].replace("\n", "")

    return root