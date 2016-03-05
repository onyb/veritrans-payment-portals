#! /usr/bin/env python
# coding:utf-8

import os

from core.api import API

API.init()

if __name__ == "__main__":
    port = int(
        os.environ.get(
            'PORT',
            5000
        )
    )
    API.app.run(
        host='0.0.0.0',
        port=port
    )
