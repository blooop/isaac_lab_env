#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "isaacsim==4.2.0.2",
#   "isaacsim-extscache-kit==4.2.0.2",
#   "isaacsim-extscache-kit-sdk==4.2.0.2",
#   "isaacsim-extscache-physics==4.2.0.2",
# ]
# ///

import os
import subprocess

os.environ["OMNI_KIT_ACCEPT_EULA"] = "yes"
subprocess.run(["isaacsim", "omni.isaac.sim.kit"], check=True)
