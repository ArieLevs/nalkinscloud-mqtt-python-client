import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nalkinscloud_mqtt_python_client",
    version="0.0.2",
    author="Arie Lev",
    author_email="levinson.arie@gmail.com",
    description="Simple MQTT client implementation that fits nalkinscloud projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArieLevs/nalkinscloud-mqtt-python-client",
    packages=setuptools.find_packages(),
    install_requires=[
        'paho-mqtt==1.5.1',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
