import matplotlib.pyplot as plt
import numpy as np
from matplotlib.hatch import Shapes, _hatch_types
from matplotlib.patches import Rectangle


class SquareHatch(Shapes):
    """
    Square hatch defined by a path drawn inside [-0.5, 0.5] square.
    Identifier 's'.
    """
    def __init__(self, hatch, density):
        self.filled = False
        self.size = 1
        self.path = Rectangle((-0.25, 0.25), 0.5, 0.5).get_path()
        self.num_rows = (hatch.count('s')) * density
        self.shape_vertices = self.path.vertices
        self.shape_codes = self.path.codes
        Shapes.__init__(self, hatch, density)


def main():
    # attach our new hatch
    _hatch_types.append(SquareHatch)
    
    # plot random bars
    np.random.seed(101)
    num = 10
    y_values = np.random.rand(num)
    x_values = np.arange(num)
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    color_blue = np.asarray([0, 107, 164]) / 255
    width = 0.5

    # group bars
    ax.bar(x_values[::2] - width / 2, y_values[::2], color='w', edgecolor=color_blue, hatch='s', width=width)
    ax.bar(x_values[::2] + width / 2, y_values[1::2], color='w', edgecolor=color_blue, hatch='sss', width=width)

    # set labels and ticks
    ax.set_title("Bar Chart")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    y_ticks = np.linspace(0, np.round(max(y_values), 0), 5)
    ax.set_yticks(y_ticks)
    ax.set_xticks(x_values[::2])
    ax.set_xticklabels(['a', 'b', 'c', 'd', 'e'])

    # clear spines and set color
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_bounds(y_ticks[0], y_ticks[-1])
    ax.spines['bottom'].set_bounds(x_values[0], x_values[-2])
    ax.spines['left'].set_color('darkorange')
    ax.spines['bottom'].set_color('darkorange')

    plt.show()


if __name__ == '__main__':
    main()
