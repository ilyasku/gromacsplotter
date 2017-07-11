def plot_xvg_data(ax, data, plot_kwargs, plot_operations):

    names = data.dtype.names

    if names:
        for i in range(1, len(names)):
            ax.plot(data[names[0]], data[names[i]], label=names[i], **plot_kwargs)
    else:
        for i in range(1, data.shape[0]):
            ax.plot(data[0, :], data[i, :])

    for function, arguments in plot_operations.values():
        function(ax, *arguments)


def main():

    import os
    import sys
    if len(sys.argv) != 2:
        msg = "Requires exactly one argument: an xvg file name!"
        raise RuntimeError(msg)
    xvg_file_name = sys.argv[1]

    if not os.path.isfile(xvg_file_name):
        msg = "file \"%s\" not found!" % xvg_file_name
        raise IOError(msg)

    import matplotlib.pyplot as plt    
    from gromacsplotter.read_xvg import read_xvg

    f, ax = plt.subplots(1, 1)

    data, kwargs, operations = read_xvg(xvg_file_name)

    plot_xvg_data(ax, data, kwargs, operations)
    ax.legend()
    plt.show()
