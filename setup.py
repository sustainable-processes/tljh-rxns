from setuptools import setup

setup(
    name="tljh-rxns",
    entry_points={"tljh": ["rxns = tljh_rxns"]},
    py_modules=["tljh_rxns"],
)