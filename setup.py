from setuptools import setup, find_packages

reqs = [
    "jupyterlab",
    "matplotlib",
    "plotly",
    "numpy",
    "pandas",
    "yaml",
    "pygame"
]

conda_reqs = [
    "jupyterlab",
    "matplotlib",
    "plotly",
    "numpy",
    "pandas",
    "yaml",
    "pygame"
]

test_pkgs = []

setup(
    name="gametutorial",
    python_requires='>3.6',
    description="game tutorial",
    url="https://github.com/neumj/gametutorial",
    install_requires=reqs,
    conda_install_requires=conda_reqs,
    test_requires=test_pkgs,
    packages=find_packages(),
    include_package_data=True
)