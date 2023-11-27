import asyncio
import sys
from decimal import Decimal
from typing import Optional

import click

from xxch.wallet.transaction_sorting import SortKey


@click.group("stake", short_help="Manage your stake")
@click.pass_context
def stake_cmd(ctx: click.Context) -> None:
    pass


@stake_cmd.command("info", short_help="Query stake info")
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which wallet to use", type=int)
@click.argument("stake_category", type=click.Choice(["farm", "lock"]), nargs=1, required=True)
def stake_info_cmd(
    wallet_rpc_port: Optional[int],
    fingerprint: int,
    stake_category: str,
) -> None:
    from .stake_funcs import stake_info

    asyncio.run(
        stake_info(
            wallet_rpc_port=wallet_rpc_port,
            fp=fingerprint,
            stake_category=stake_category,
        )
    )


@stake_cmd.command("get_transactions", help="Get stake transactions")
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which key to use", type=int)
@click.option("-i", "--id", help="Id of the wallet to use", type=int, default=1, show_default=True, required=True)
@click.option(
    "-o",
    "--offset",
    help="Skip transactions from the beginning of the list",
    type=int,
    default=0,
    show_default=True,
    required=True,
)
@click.option(
    "-l",
    "--limit",
    help="Max number of transactions to return",
    type=int,
    default=(2**32 - 1),
    show_default=True,
    required=False,
)
@click.option("--verbose", "-v", count=True, type=int)
@click.option(
    "--paginate/--no-paginate",
    default=None,
    help="Prompt for each page of data.  Defaults to true for interactive consoles, otherwise false.",
)
@click.option(
    "--sort-by-height",
    "sort_key",
    flag_value=SortKey.CONFIRMED_AT_HEIGHT,
    type=SortKey,
    help="Sort transactions by height",
)
@click.option(
    "--sort-by-relevance",
    "sort_key",
    flag_value=SortKey.RELEVANCE,
    type=SortKey,
    default=True,
    help="Sort transactions by {confirmed, height, time}",
)
@click.option(
    "--reverse",
    is_flag=True,
    default=False,
    help="Reverse the transaction ordering",
)
def get_transactions_cmd(
    wallet_rpc_port: Optional[int],
    fingerprint: int,
    id: int,
    offset: int,
    limit: int,
    verbose: bool,
    paginate: Optional[bool],
    sort_key: SortKey,
    reverse: bool,
) -> None:  # pragma: no cover
    from .stake_funcs import stake_transactions

    asyncio.run(
        stake_transactions(
            wallet_rpc_port=wallet_rpc_port,
            fp=fingerprint,
            wallet_id=id,
            verbose=verbose,
            paginate=paginate,
            offset=offset,
            limit=limit,
            sort_key=sort_key,
            reverse=reverse,
        )
    )

    # The flush/close avoids output like below when piping through `head -n 1`
    # which will close stdout.
    #
    # Exception ignored in: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
    # BrokenPipeError: [Errno 32] Broken pipe
    sys.stdout.flush()
    sys.stdout.close()


@stake_cmd.command("send", short_help="Send xxch to stake stake-hash")
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which wallet to use", type=int)
@click.option("-i", "--id", help="Id of the wallet to use", type=int, default=1, show_default=True, required=True)
@click.option("-a", "--amount", help="How much xxch to stake, in XXCH, must be a positive integer", type=int, required=True)
@click.option(
    "-m",
    "--fee",
    help="Set the fees for the stake transaction, in XXCH",
    type=str,
    default="0",
    show_default=True,
    required=True,
)
@click.option("-t", "--address", help="stake address", type=str, default="", required=True)
@click.option("-s", "--stake-type", help="Set the stake type", type=int, default=None)
@click.argument("stake_category", type=click.Choice(["farm", "lock"]), nargs=1, required=True)
def stake_send_cmd(
    wallet_rpc_port: Optional[int],
    fingerprint: int,
    id: int,
    amount: int,
    fee: str,
    address: str,
    stake_type: Optional[int],
    stake_category: str,
) -> None:
    from .stake_funcs import stake_send

    asyncio.run(
        stake_send(
            wallet_rpc_port=wallet_rpc_port,
            fp=fingerprint,
            wallet_id=id,
            stake_type=stake_type,
            stake_category=stake_category,
            address=address,
            amount=amount,
            fee=Decimal(fee),
        )
    )


# @stake_cmd.command(
#     "withdraw",
#     help="withdraw a Stake transaction."
#     " The wallet will automatically detect if you are able to withdraw.",
# )
# @click.option(
#     "-wp",
#     "--wallet-rpc-port",
#     help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
#     type=int,
#     default=None,
# )
# # TODO: Remove unused wallet id option
# @click.option("-i", "--id", help="Id of the wallet to use", type=int, default=1, show_default=True, required=True)
# @click.option("-f", "--fingerprint", help="Set the fingerprint to specify which key to use", type=int)
# @click.option(
#     "-ids",
#     "--tx_ids",
#     help="IDs of the Stake transactions you want to withdraw. Separate multiple IDs by comma (,).",
#     type=str,
#     default="",
#     required=True,
# )
# @click.option(
#     "-m", "--fee", help="A fee to add to the offer when it gets taken, in XXCH", default="0", show_default=True
# )
# def stake_withdraw_cmd(
#     wallet_rpc_port: Optional[int], id: int, fingerprint: int, tx_ids: str, fee: str
# ) -> None:  # pragma: no cover
#     from .stake_funcs import spend_stake_coins
#
#     asyncio.run(
#         spend_stake_coins(
#             wallet_rpc_port=wallet_rpc_port,
#             fp=fingerprint,
#             fee=Decimal(fee),
#             tx_ids_str=tx_ids,
#         )
#     )
