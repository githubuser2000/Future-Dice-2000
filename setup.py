#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name="dice",
    version="0.5.0",
    description="dice",
    author="Jupiter 3.0 alias trace",
    packages=find_packages(include=["dicegui.py"]),
    install_requires=[
        "PyQt5==5.13.1",
    ],
    package_data={
        ".": [
            "*.txt",
            "*.sh",
            "*.qm",
            "*.png",
            "*.ts",
            "*.json",
            "*.ui",
            "*.spec",
            "*.qml",
            "*.cfg",
        ]
    },
)
