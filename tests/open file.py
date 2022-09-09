import importlib
import pathlib
import pytest
import tomli


def _read_tests_from_config():
    test_configs = {}
    config_path = pathlib.Path(__file__).parent / "test_multi_winner"
    for toml_path in config_path.glob("*.toml"):
        config = tomli.loads(toml_path.read_text(encoding="utf-8"))
        test_configs[config["Ballot_Data"]] = config["Election_Parameters"]
    print(test_configs)
    return test_configs


_read_tests_from_config()
