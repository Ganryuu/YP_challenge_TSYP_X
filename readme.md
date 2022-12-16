# Phoebe RL Agent 

Phoebe is a reinforcement learning agent designed to optimize and help astronauts and NASA ground control to perform various decision-making tasks on the ARTEMIS Lunar Mission. 

Phoebe is built with Python, Flask, and Vue.js, it is built to be compatible with NASAs open mission control platform, see more [here](https://github.com/nasa/openmct)

Phoebe performs Multiple Tasks 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages from requirements.txt.

```bash
pip install -r requirements.txt
```

## Usage

This section is a flask API for the Phoebe computation and responses 
Phoebe takes an image as in input, which is the mars surface seen by the VIPER rover 
This image is segmented into multiple tiles and converted to a Numpy array taking into consideration the terrain changes 
Phoebe agent then tries different policies on each segment to deduct the optimal path between each tile on that image corresponding to the moon surface zones. 


Phoebe also has a simple task rearrangement based on priority and given conditions like ( sun position, atmosphere state, astronaut physiological shape, priority, and unexpected conditions ) to change the order and priority of the different tasks required to be done by the astronauts. 

```python
API endpoints

# '/'
Returns a JSON response of basic info about the Phoebe project

# '/path/'
Returns the optimal path for each segment of the last inputted image by the VIPER rover

# '/tasks/'
Updates the last tasks updates depending on the various inputs and conditions given 
and returns newly updated task lists to arrange them in the interface
```

## Contributing

Pull requests are welcome. For significant changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Reinforcement Learning Approach for the Phoebe Agent
Simplified Image for how Reinforcement Learning agents work 

<img src="files\moon_sun_positions\images\rl.jpg" alt="RL" title="Reinforcment Learning simplified">

Phoebe was based on the Monte Carlo algorithm

<img src="files\moon_sun_positions\images\monte-carlo.png" alt="Algorithm" title="Monte-Carlo">

Policy Iterations help us pick the optimal policy for each tile
<img src="files\moon_sun_positions\images\policy_iter.png" alt="Policy" title="Policy Iterations">


## External Sources 

LUNANET:
Openmct:
Open MCT (Open Mission Control Technologies) is a next-generation mission control framework for visualization of data on desktop and mobile devices

[1]https://www.nasa.gov/feature/goddard/2021/lunanet-empowering-artemis-with-communications-and-navigation-interoperability
[2]https://independentaustralia.net/business/business-display/lunanet-developing-internet-for-the-moon,16716
[3]https://github.com/nasa/openmct

Volatiles Investigating Polar Exploration Rover (VIPER)
[4]https://www.nasa.gov/viper/lunar-operations#route
[5]https://www.nasa.gov/feature/ames/nasas-viper-prototype-motors-through-moon-like-obstacle-course

Base Camp Management
[6]https://www.smithsonianmag.com/science-nature/four-things-weve-learned-about-nasas-planned-base-camp-on-the-moon-180980589/
[7]https://www.smithsonianmag.com/air-space-magazine/tools-of-the-astronaut-trade-15273242/
[8]https://blogs.nasa.gov/artemis/2020/10/28/lunar-living-nasas-artemis-base-camp-concept/

## License

[MIT](https://choosealicense.com/licenses/mit/)
