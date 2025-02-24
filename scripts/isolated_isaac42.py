#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "isaacsim==4.2.0.2",
#   "isaacsim-extscache-kit==4.2.0.2",
#   "isaacsim-extscache-kit-sdk==4.2.0.2",
#   "isaacsim-extscache-physics==4.2.0.2",
# ]
# [[tool.uv.index]]
# url = "https://pypi.nvidia.com"
# ///

import os
import subprocess

os.environ["OMNI_KIT_ACCEPT_EULA"] = "yes"
subprocess.run(["isaacsim", "omni.isaac.sim.kit"], check=True)

# # raw commands
# isaacsim omni.isaac.sim.kit
# isaacsim omni.isaac.sim.python.kit
