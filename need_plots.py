import itertools
from matplotlib.legend_handler import HandlerTuple
import matplotlib.pyplot as plt
from matplotlib import cm, colors
import matplotlib.patches as mpatches
import numpy as np
from scipy.signal import find_peaks
from joblib import Parallel, delayed
import itertools
import random
import os


class figret:
    def __init__(self, fig, ax, pyplt, plots):
        self.fig = fig
        self.ax = ax
        self.pyplt = pyplt
        self.plots = plots


class dataset:
    plottype = "plot"
    scattertype = "scatter"
    def __init__(self):
        self.x = None
        self.y = None
        self.plot_type=None

        self.label = None
        self.color = None
        self.marker = None
        self.data_type = None
        self.x_data_type = None
        self.marker_size=None
        # usually a tuple of two. (a,b) where a goes with marker and b goes with color
        self.parameters = None
        self.colorparametername = None
        self.markerparametername = None


class Plotter:

    def __init__(self):
        self.scatter_type = "scatter"
        self.plot_type = "plot"
        self.markers = itertools.cycle((',', '+', '.', 'o', '*'))
        self.colors = itertools.cycle(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tab:purple', 'tab:gray', 'tab:orange'])

    def Plot(self, datasets: [dataset], title="Plot",
             xlabel=r"X-axis", ylable=r"Y-axis", xscale="log", yscale="log", figsize=15, maxy=None, miny=None,
             maxx=None, minx=None, fig=None, ax=None, pyplt=None):
        if (pyplt == None):
            pyplt = plt
        if (fig == None or ax == None):
            fig, ax = plt.subplots(figsize=(figsize, figsize))
        ax.set_xscale(xscale)
        ax.set_yscale(yscale)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylable)
        ax.set_title(title)

        if (miny != None or minx != None or maxx != None or maxy != None):
            ax.set_ylim(miny, maxy)
            ax.set_xlim(minx, maxx)

        for ds in datasets:
            if ds.color != None and ds.marker != None and ds.label != None and ds.marker_size != None:
                if ds.plot_type == dataset.plottype:
                    ax.plot(ds.x, ds.y, c=ds.color, marker=ds.marker, label=ds.label,s=ds.marker_size)
                else:
                    ax.scatter(ds.x, ds.y, c=ds.color, marker=ds.marker, label=ds.label,s=ds.marker_size)
            if ds.color != None and ds.marker != None and ds.label != None:
                if ds.plot_type==dataset.plottype:
                    ax.plot(ds.x, ds.y, c=ds.color, marker=ds.marker, label=ds.label)
                else:
                    ax.scatter(ds.x, ds.y, c=ds.color, marker=ds.marker, label=ds.label)

            if ds.color == None and ds.marker != None and ds.label != None:
                if ds.plot_type==dataset.plottype:
                    ax.plot(ds.x, ds.y, marker=ds.marker, label=ds.label)
                else:
                    ax.scatter(ds.x, ds.y, marker=ds.marker, label=ds.label)
            if ds.color != None and ds.marker == None and ds.label != None and ds.marker_size!=None:
                if ds.plot_type == dataset.plottype:
                    ax.plot(ds.x, ds.y, c=ds.color, label=ds.label,s=ds.marker_size)
                else:
                    ax.scatter(ds.x, ds.y, c=ds.color, label=ds.label,s=ds.marker_size)
            if ds.color != None and ds.marker == None and ds.label == None and ds.marker_size!=None:
                if ds.plot_type == dataset.plottype:
                    ax.plot(ds.x, ds.y, c=ds.color, label=ds.label,s=ds.marker_size)
                else:
                    ax.scatter(ds.x, ds.y, c=ds.color, label=ds.label,s=ds.marker_size)
            if ds.color != None and ds.marker == None and ds.label != None and ds.marker_size==None:
                if ds.plot_type==dataset.plottype:
                    ax.plot(ds.x, ds.y, c=ds.color, label=ds.label)
                else:
                    ax.scatter(ds.x, ds.y, c=ds.color, label=ds.label)
            if ds.color != None and ds.marker != None and ds.label == None:
                if ds.plot_type==dataset.plottype:
                    ax.plot(ds.x, ds.y, c=ds.color, linestyle=ds.marker)
                else:
                    ax.scatter(ds.x, ds.y, c=ds.color, marker=ds.marker)
            if ds.color == None and ds.marker == None and ds.label != None:
                if ds.plot_type==dataset.plottype:
                    ax.plot(ds.x, ds.y, label=ds.label)
                else:
                    ax.scatter(ds.x, ds.y, label=ds.label)
            if ds.color == None and ds.marker != None and ds.label == None:
                if ds.plot_type==dataset.plottype:
                    ax.plot(ds.x, ds.y, marker=ds.marker)
                else:
                    ax.scatter(ds.x, ds.y, marker=ds.marker)
            if ds.color != None and ds.marker == None and ds.label == None and ds.marker_size==None:
                if ds.plot_type==dataset.plottype:
                    ax.plot(ds.x, ds.y, c=ds.color)
                else:
                    ax.scatter(ds.x, ds.y, c=ds.color)
            if ds.color == None and ds.marker == None and ds.label == None:
                if ds.plot_type==dataset.plottype:
                    ax.plot(ds.x, ds.y)
                else:
                    ax.scatter(ds.x, ds.y)

        handles, labels = ax.get_legend_handles_labels()
        # if len(datasets) > 8:
        #     patches = []
        #     handles = []
        #     labels = []
        #     colorparameterssecond = []
        #     markerparametersfirst = []
        #     markers = []
        #     colors = []
        #     scatter_color=[]
        #     scatter_markers=[]
        #     for ds in datasets:
        #         # if (ds.parameters[0] not in markerparametersfirst):
        #         #     markerparametersfirst.append(ds.parameters[0])
        #         # if (ds.parameters[1] not in colorparameterssecond):
        #         #     colorparameterssecond.append(ds.parameters[1])
        #         if (ds.color not in colors):
        #             if(ds.plot_type==self.plot_type):
        #                 colors.append(ds.color)
        #             else:
        #                 scatter_color.append(ds.color)
        #         if (ds.marker not in markers):
        #             if(ds.plot_type==self.plot_type):
        #                 markers.append(ds.marker)
        #             else:
        #                 scatter_markers.append(ds.marker)
        #     for i in range(len(colors)):
        #         templine = plt.scatter([], [], marker=markers[0], c=colors[i])
        #         handles.append(templine)
        #     handles = tuple(handles)
        #     handles2 = []
        #     for i in range(len(markers)):
        #         templine = plt.scatter([], [], marker=markers[i], c=colors[0])
        #         handles2.append(templine)
        #     handles2 = tuple(handles2)
        #     handlelength = None
        #     if (len(colors) > len(markers)):
        #         handlelength = len(colors)
        #     else:
        #         handlelength = len(markers)
        #     colorlabel = ds.colorparametername
        #     if (colorlabel == None):
        #         colorlabel = ":"
        #     markerlabel = ds.markerparametername
        #     if (markerlabel == None):
        #         markerlabel = ":"
        #     else:
        #         markerlabel = markerlabel + ":"
        #     for c in colorparameterssecond:
        #         colorlabel = colorlabel + ", " + str(c)
        #     for c in markerparametersfirst:
        #         markerlabel = markerlabel + ", " + str(c)
        #     markerlabel = markerlabel.replace(',', "", 1)
        #     colorlabel = colorlabel.replace(',', "", 1)
        #     ax.legend([handles, handles2], [colorlabel, markerlabel], handlelength=handlelength + 3, loc="best",
        #               handler_map={tuple: HandlerTuple(ndivide=None)})
        #
        # else:
        ax.legend(handles, labels, loc="best", prop={'size': 10})

        return figret(fig, ax, pyplt, None)
