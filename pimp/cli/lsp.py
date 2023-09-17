from pimp.common import *

import rich_click as click

logger = logging.getLogger(__name__)


# async def run_server(config: WokeConfig, port: int) -> None:
#     from woke.lsp.server import LspServer
#
#     async def client_callback(
#         reader: asyncio.StreamReader, writer: asyncio.StreamWriter
#     ) -> None:
#         lsp_server = LspServer(config, reader, writer)
#         logger.info("Client connected")
#         await lsp_server.run()
#         writer.close()
#         logger.info("Client disconnected")
#
#     server = await asyncio.start_server(client_callback, port=port)
#     logger.info(f"Started LSP server on port {port}")
#
#     async with server:
#         await server.serve_forever()
#
#
# @click.command(name="lsp")
# @click.option("--port", default=65432, type=int, help="Port to listen on.")
# @click.pass_context
# def run_lsp(context: click.Context, port: int):
#     """
#     Start the LSP server.
#     """
#     config = WokeConfig()
#     config.load_configs()  # load ~/.woke/config.toml and ./woke.toml
#
#     asyncio.run(run_server(config, port))
#
# import json
# from pathlib import Path
# from typing import List, Optional
#
# import rich_click as click
# from click.core import Context
# from rich_click.rich_group import RichGroup
#
# from woke.cli.console import console
# from woke.config import WokeConfig


@click.group(name="lsp")
@click.pass_context
def run_lsp(ctx: click.core.Context):
    ...


@run_lsp.command(name="shell")
# @click.option("--language", "--lang", default="english", help="Mnemonic language")
# @click.argument("alias")
@click.pass_context
def lsp_shell(
    ctx: click.core.Context,
):
    """
    Start the LSP shell.
    """
    print("lsp shell")
