#!/usr/bin/python

import pyanaconda.iutil

def _getSysroot():
	return "/"

pyanaconda.iutil.getSysroot=_getSysroot

from pyanaconda.kexec import setup_kexec

setup_kexec()
