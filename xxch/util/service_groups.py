from __future__ import annotations

from typing import Generator, KeysView

SERVICES_FOR_GROUP = {
    "all": [
        "xxch_harvester",
        "xxch_timelord_launcher",
        "xxch_timelord",
        "xxch_farmer",
        "xxch_full_node",
        "xxch_wallet",
        "xxch_data_layer",
        "xxch_data_layer_http",
    ],
    # TODO: should this be `data_layer`?
    "data": ["xxch_wallet", "xxch_data_layer"],
    "data_layer_http": ["xxch_data_layer_http"],
    "node": ["xxch_full_node"],
    "harvester": ["xxch_harvester"],
    "farmer": ["xxch_harvester", "xxch_farmer", "xxch_full_node", "xxch_wallet"],
    "farmer-no-wallet": ["xxch_harvester", "xxch_farmer", "xxch_full_node"],
    "farmer-only": ["xxch_farmer"],
    "timelord": ["xxch_timelord_launcher", "xxch_timelord", "xxch_full_node"],
    "timelord-only": ["xxch_timelord"],
    "timelord-launcher-only": ["xxch_timelord_launcher"],
    "wallet": ["xxch_wallet"],
    "introducer": ["xxch_introducer"],
    "simulator": ["xxch_full_node_simulator"],
    "crawler": ["xxch_crawler"],
    "seeder": ["xxch_crawler", "xxch_seeder"],
    "seeder-only": ["xxch_seeder"],
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
