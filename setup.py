import setuptools
from pkg_resources import parse_requirements

with open("requirements.txt") as f:
    requirements = [str(r) for r in parse_requirements(f)]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nalkinscloud_mqtt_python_client",
    version="1.0.1",
    author="Arie Lev",
    author_email="levinson.arie@gmail.com",
    description="Simple MQTT client implementation that fits nalkinscloud projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArieLevs/nalkinscloud-mqtt-python-client",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
