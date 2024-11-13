#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "isaacsim==4.2.0.2",
#   "isaacsim-extscache-kit==4.2.0.2",
#   "isaacsim-extscache-kit-sdk==4.2.0.2",
#   "isaacsim-extscache-physics==4.2.0.2"
# ]
# ///

import os
import subprocess


def main() -> None:
    try:
        os.environ["OMNI_KIT_ACCEPT_EULA"] = "yes"
        subprocess.run(["isaacsim", "omni.isaac.sim.python.kit"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command 'isaacsim' failed with exit code {e.returncode}")
    else:
        print("isaacsim command executed successfully!")


if __name__ == "__main__":
    main()
