from isaacsim import SimulationApp

simulation_app = SimulationApp({
    "headless": False,
    "exts": [
        "omni.kit.capture"  # Enable the video capture extension
    ]
})
from omni.isaac.core import World
from omni.isaac.core.objects import DynamicCuboid
import bencher as bch
import numpy as np
import omni.kit.capture  # Import the capture module


class BenchIsaacBase(bch.ParametrizedSweep):
    spawn_x = bch.FloatSweep(default=0, bounds=[-1, 1])

    def __init__(self, simulation_app, **params):
        super().__init__(**params)
        self.simulation_app = simulation_app
        self.world = None

    def __call__(self, **kwargs):
        self.update_params_from_kwargs(**kwargs)
        # Destroy any existing world before creating a new one
        if self.world is not None:
            self.world.clear_instance()
            self.world = None

        # Create a fresh world instance
        self.world = World()
        self.world.scene.add_default_ground_plane()

        # Add the cube to the world
        fancy_cube = self.world.scene.add(
            DynamicCuboid(
                prim_path="/World/random_cube",
                name="fancy_cube",
                position=np.array([self.spawn_x, 0, 1.0]),
                scale=np.array([0.5015, 0.5015, 0.5015]),
                color=np.array([0, 0, 1.0]),
            )
        )

        self.world.reset()
        for i in range(50):
            position, orientation = fancy_cube.get_world_pose()
            linear_velocity = fancy_cube.get_linear_velocity()
            print("Cube position is : " + str(position))
            print("Cube's orientation is : " + str(orientation))
            print("Cube's linear velocity is : " + str(linear_velocity))
            # Execute one physics step and one rendering step
            self.world.step(
                render=True
            )  

        return super().__call__(**kwargs)

    def exit(self):
        if self.world is not None:
            self.world.clear_instance()
        self.simulation_app.close()  # Close Isaac Sim


if __name__ == "__main__":
    run_cfg = bch.BenchRunCfg()
    run_cfg.level = 3
    bench = BenchIsaacBase(simulation_app).to_bench()
    bench.plot_sweep()
    bench.report.show()
