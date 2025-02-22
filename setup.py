from setuptools import setup, find_packages

setup(
    name="pacote_de_ingestao_de_dados",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "boto3",
        "pytest"
    ]
)