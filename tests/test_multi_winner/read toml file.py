import toml

all_data_from_toml = toml.load("mw01.toml")
election_parameters = all_data_from_toml["Election_Parameters"]

for k, v in election_parameters.items():
    print(k, "=", v)
