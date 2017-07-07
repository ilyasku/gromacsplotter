import numpy as np
from matplotlib.axes._axes import Axes


def read_xvg(file_name):
    f = open(file_name, "r")
    lines = f.readlines()

    plot_kwargs = {}
    plot_operations = {}
    for i in range(len(lines)):
        line = lines[i]
        if line.startswith("#"):
            continue
        if line.startswith("@"):
            _update_plot_kwargs_and_operations(plot_kwargs, plot_operations, line)
        else:
            break
        
    data_lines = lines[i:]

    data = np.empty((2, len(data_lines)))
    
    for j in range(0, len(data_lines)):
        data[:, j] = np.fromstring(data_lines[j], dtype=float, sep=" ")
    return data, plot_kwargs, plot_operations


def _update_plot_kwargs_and_operations(plot_kwargs: dict, plot_operations: dict, line: str):  
    if line.count("title"):
        title = line.split("title")[-1]
        title = title.strip().replace("\"", "")
        plot_operations["title"] = [Axes.set_title, [title]]
        return
