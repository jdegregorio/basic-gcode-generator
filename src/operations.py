import os
import numpy as np
import fire

# gcode header
header = 'G90 G94\nG17\nG20\nG28 G91 X0 Y0 Z1.0\nG90\nT1\nS15000 M3\nG54\n'

# Delete existing nc file if it exists
if os.path.exists("./out/path.nc"):
  os.remove("./out/path.nc")

def channel(x_location: float, width: float, depth: float, length: float, 
            cutter_diameter: float = 0.25, overlap: float = 0.1, 
         step_down_max: float = None, z_safe: float = 0.075, feed_rate: float = 40):

    # Initialize string for gcode
    x_start = x_location + (cutter_diameter / 2)
    nc = header + f'G0 X{x_start} Y0 Z{z_safe}\n'

    # Set max step-down to cutter diameter if not specified
    if step_down_max is None:
        step_down_max = cutter_diameter

    # Determine number of paths and step-over distance
    step_over_max = cutter_diameter*(1 - overlap)
    n_steps_over = np.ceil((width - cutter_diameter) / step_over_max)
    step_over = (width - cutter_diameter) / n_steps_over

    # Determine number of z-depths and step-down distance
    n_steps_down = np.ceil(depth / step_down_max)
    step_down = depth / n_steps_down

    # Iterate through horizontal and depth paths to cut channel
    for j in range(int(n_steps_down)):
        z = -(j + 1)*step_down
        nc = nc + f'G1 Z{z} F{feed_rate}\n'
        for i in range(int(n_steps_over)):
            x = x_start + i*step_over
            y = ((i + 1) % 2)*length
            nc = nc + f'G1 X{x} Y{y} F{feed_rate}\n'
        nc = nc + f'G0 Z{z_safe}\nG0 X{x_start} Y0\n'

    # Write gcode to file
    with open('./out/path.nc', 'w') as f:
            f.writelines(nc)

if __name__ == "__main__":

    fire.Fire(channel)
