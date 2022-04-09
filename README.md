# Pyfaceit

Pyfaceit is a Python Package that makes it easy to retrieve data from Faceit API for Counter Strike Developers. Faceit API docs can be confusing and hard to implement, 
this Python package does all the hard work behind the scenes, simply input the faceit name and retrieve all dat from a player, you can even retrieve specific map data.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pyfaceit.

```bash
pip install pyfaceit
```

## Usage

```python
import pyfaceit

# Creates Instance of Pyfaceit Class with API_KEY
instance = pyfaceit.Pyfaceit(API_KEY, <faceit name as string>)
# returns python Dict of all player data
instance.player_stats()

# returns Python dict information of player information for specific map.
instance.player_stats_map(<map_name(can be without de_ eg. 'mirage' or 'de_mirage')>)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
