from pimp.common import *

import rich_click as click

logger = logging.getLogger(__name__)

@click.group(name="ts")
@click.pass_context
def run_ts(ctx: click.core.Context):
    ...

@run_ts.command(name="parse")
# @click.option("--language", "--lang", default="english", help="Mnemonic language")
@click.argument("path", type=click.Path(exists=True))
@click.pass_context
def ts_shell(
    ctx: click.core.Context,
    path: plib.Path,
):
    """
    Parse a file.
    """
    print("ts shell")

