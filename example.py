#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import logging
import sys
import time

from commonutil_jsonstdioipc import JSONStandardIOIPC


def main() -> None:
	logging.basicConfig(level=logging.INFO, stream=sys.stderr)
	jsonstdioipc = JSONStandardIOIPC()
	jsonstdioipc.write(
		{
			"message": "Hello World",
			"t": time.time(),
		}
	)
	logging.info('please response with: {"response": "Hi"}')
	resp = jsonstdioipc.read()
	response_message = resp.get("response")
	logging.info("response is: %r", response_message)


if __name__ == "__main__":
	main()
