#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from invoke import task
from invoke import run

@task
def check(c):
    cmd= "python -m compileall -q source"
    print("Realizando check de la sintaxis...\n\n")
    result = c.run(cmd, hide=False, warn=False)
    if result.ok:
        print("Check realizado exitosamente")

# =============================================================================
# @task
# def run(c):
#
# @task
# def tests(c):
#   cmd = "python -m pytest"
#
# =============================================================================
