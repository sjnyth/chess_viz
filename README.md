# Chess Gameplay Analysis ♟
In this project, I analyzed gameplay data of approximately 4800 chess games I played on chess.com using pandas, pyvis, matplotlib and more. 
## Features
### Graph-Based Move Visualization 📈: 
Understand the flow of the game through moves visualized as a network graph.
### Endgame Heatmap 🗺: 
Discover the most common end positions in the games played.
### Interactive Features 📍: 
Interact with the visualizations to get a better understanding of specific nodes and connections.

## Requirements

```
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx
from pyvis.network import Network
from pyvis.physics import Physics
import chess
import json
import re
```
