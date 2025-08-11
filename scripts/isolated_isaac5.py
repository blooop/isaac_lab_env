#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11,<3.12"
# dependencies = [
#   "isaacsim[all,extscache]>=5.0.0.0",
# ]
# # You may need this
# [[tool.uv.index]]
# url = "https://pypi.nvidia.com"
# ///

import os
import subprocess

os.environ["OMNI_KIT_ACCEPT_EULA"] = "yes"
subprocess.run(["isaacsim"], check=True)

# subprocess.run(["isaacsim", "isaacsim.sim.kit"], check=True)
# # raw commands
# isaacsim omni.isaac.sim.kit
# isaacsim omni.isaac.sim.python.kit
