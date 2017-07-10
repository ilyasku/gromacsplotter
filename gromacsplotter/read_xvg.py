import numpy as np
from matplotlib.axes._axes import Axes
from .exceptions.unsupported_data_format_exception import UnsupportedDataFormatException


def read_xvg(file_name):
    f = open(file_name, "r")
    lines = f.readlines()

    plot_kwargs = {}
    plot_operations = {}
    for i in range(len(lines)):
        line = lines[i]
        if line.startswith("@TYPE"):
            _type = line.split()[-1]
            if _type != "xy":
                raise UnsupportedDataFormatException()
        if line.startswith("#"):
            continue
        if line.startswith("@ s0 "):
            break
        if line.startswith("@"):
            _update_plot_kwargs_and_operations(plot_kwargs, plot_operations, line)
        else:
            break

    lines = lines[i:]

    dtypes = [("time", np.float)]
    
    for i in range(len(lines)):
        line = lines[i]
        if not line.startswith("@ s" + str(i)):
            break
        label = _extract_value_from_line("legend", line)
        dtypes.append((label, np.float))        

    data_lines = lines[i:]

    data = np.empty(len(data_lines), dtype=dtypes)

    for j in range(len(data_lines)):
        data_line_j = np.fromstring(data_lines[j], dtype=float, sep=" ")
        for k in range(len(dtypes)):
            data[dtypes[k][0]][j] = data_line_j[k]
    return data, plot_kwargs, plot_operations


def _update_plot_kwargs_and_operations(plot_kwargs: dict, plot_operations: dict, line: str):
    line = " ".join(line.split())
    if line.count("title"):
        title = _extract_value_from_line("title", line)
        plot_operations["title"] = [Axes.set_title, [title]]
        return

    if line.count("xaxis label"):
        xaxis_label = _extract_value_from_line("xaxis label", line)
        plot_operations["xaxis_label"] = [Axes.set_xlabel, [xaxis_label]]
        return

    if line.count("yaxis label"):
        yaxis_label = _extract_value_from_line("yaxis label", line)
        plot_operations["yaxis_label"] = [Axes.set_ylabel, [yaxis_label]]
        return


def _extract_value_from_line(key: str, line: str):
    value = line.split(key)[-1]
    value = value.strip().replace("\"", "")
    return value
