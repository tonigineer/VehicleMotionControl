"""Run an open loop maneuver."""

from vmc.models import FSVehSingleTrack
from vmc.simulation import Simulator, Scenario
from vmc.controller import SteerRamp


def main():
    """Run simulation with steering ramp as control input."""
    scenario_open_loop_ctrl = Scenario(SteerRamp(derivative=False))
    fs_veh_model = FSVehSingleTrack()

    Sim = Simulator(model=fs_veh_model, scenario=scenario_open_loop_ctrl)
    Sim.run()
    Sim.show_states_and_input()


if __name__ == "__main__":
    main()
