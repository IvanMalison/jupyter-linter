from setuptools import setup, find_packages

setup(
    name='jupyter-linter',
    version='0.0.0',
    description=("Lint jupyter cells."),
    url='https://github.com/kevin1024/vcrpy',
    packages=find_packages(exclude=[]),
    install_requires=["jupyter", "flake8"],
)
