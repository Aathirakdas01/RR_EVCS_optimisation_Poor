import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, LpContinuous, PULP_CBC_CMD
import numpy as np