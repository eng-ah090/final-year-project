def make_line_plot(x, y, title: str = "Response"):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel("Frequency")
    ax.set_ylabel("Absorption")
    return fig
