# Copyright 2013 Gedare Bloom (gedare@rtems.org)
#
# This file's license is 2-clause BSD as in this distribution's LICENSE.2 file.
#

# Waf build script for an RTEMS Hello
import rtems_waf.rtems as rtems

def build(bld):
    rtems.build(bld)

    bld(features = 'c cprogram',
        target = 'ticker.exe',
        source = ['init.c'])

