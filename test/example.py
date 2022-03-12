import sys
import logging
import commonutil_jsonstdioipc

_log = logging.getLogger(__name__)


def main():
	logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)
	ipcfp = commonutil_jsonstdioipc.JSONStandardIOIPC()
	i0 = ipcfp.read()
	_log.info("i0 = %r", i0)
	o0 = {
			"x": 1,
			"y": "two",
	}
	ipcfp.write(o0)
	i1 = ipcfp.read()
	_log.info("i1 = %r", i1)
	ipcfp.write(i1)
	_log.info("stop.")


if __name__ == '__main__':
	main()
