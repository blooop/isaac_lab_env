#!/usr/bin/env -S uv run
# /// script
# requires-python = "==3.10"
# dependencies = [
#   "isaacsim[all,extscache]==4.5.0"
# ]
# [[tool.uv.index]]
# url = "https://pypi.nvidia.com"
# ///

import os
import subprocess

os.environ["OMNI_KIT_ACCEPT_EULA"] = "yes"
# subprocess.run(["isaacsim", "isaacsim.sim.kit"], check=True)
subprocess.run(["isaacsim"], check=True)

# # raw commands
# isaacsim omni.isaac.sim.kit
# isaacsim omni.isaac.sim.python.kit
