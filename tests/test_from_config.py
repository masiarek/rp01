import importlib
import pathlib

import pytest
import tomli


def _construct_tests():
    """Convert dictionary of tests into a sequence of tuples"""
    test_configs = _read_tests_from_config()
    for function_name, tests in test_configs.items():
        func = _dynamically_load_function(function_name)
        for test_info in tests:
            params, expected = _split_params_and_expected(**test_info)
            yield func, params, expected


def _read_tests_from_config():
    test_configs = {}
    config_path = pathlib.Path(__file__).parent / "config"
    for toml_path in config_path.glob("*.toml"):
        config = tomli.loads(toml_path.read_text(encoding="utf-8"))
        test_configs[config["function"]] = config["tests"]

    return test_configs


def _dynamically_load_function(function_name):
    module_name, _, func_name = function_name.rpartition(".")
    module = importlib.import_module(module_name)
    return getattr(module, func_name)


def _split_params_and_expected(expected, **params):
    return params, expected


def _repr_params(value):
    """Add a nice representation of test parameters"""
    if isinstance(value, dict):
        return ",".join(f"{k}={v!r}" for k, v in value.items())
    else:
        return value


TESTS = _construct_tests()


@pytest.mark.parametrize(("func", "parameters", "expected"), TESTS, ids=_repr_params)
def test_from_config(func, parameters, expected):
    actual = func(**parameters)
    assert actual == expected
