# import sompy / tfprop_sompy related packages
import math
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import urllib
import random
import matplotlib as mpl
from sompy.sompy import SOMFactory
from sompy.visualization.plot_tools import plot_hex_map
import logging
import pickle
import os

import sklearn
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit
from sklearn import cluster
from sklearn.externals import joblib

import warnings
warnings.filterwarnings('ignore')

logging.getLogger('matplotlib.font_manager').disabled = True

def read_data(file):
    """
    input: csv file chosen from the directory
    """
    try:
        f = open(str(file))
        return pd.DataFrame(file)
    except IOError:
        print("File not accessible")
    finally:
        return pd.DataFrame(file)

def sm_training(data, mapsize, normalization, initialization, 
                component_names, lattice, n_job, verbose, 
                train_rough_len, train_finetune_len, file_name):
    """
    Train the model with different parameters.
    """
    dir_name = "Models/ "
    sm = SOMFactory().build(data, mapsize,normalization,initialization,component_names,lattice)
    sm.train(n_job,verbose,train_rough_len,train_finetune_len)
    topographic_error = sm.calculate_topographic_error()
    quantitization_error = np.mean(sm._bmu[1])

    # if multiple runs are required 
    #joblib.dump(sm, "model_{}.joblib".format(i))
    pickle.dump(sm, open(os.path.join(dir_name, file_name), "wb"))

def select_model(file):
    """
    The file should be the trained sm model in the directory
    This operation 
    """
    dir_name = "Models/ "

    sm = pickle.load(open(os.path.join(dir_name, file_name),"rb"))
    return sm

def vis(title, dir_name, file_name):
    """
    generate cluster map visualization
    """
    labels = labels = list(data.index)
    n_clusters = 5

    cmap = plt.get_cmap("tab20")
    n_palette = 20  # number of different colors in this color palette
    color_list = [cmap((i % n_palette)/n_palette) for i in range(n_clusters)]
    msz = sm.codebook.mapsize
    proj = sm.project_data(sm.data_raw)
    coord = sm.bmu_ind_to_xy(proj)

    fig, ax = plt.subplots(1, 1, figsize=(40,40))

    #cl_labels = som.cluster(n_clusters)
    cl_labels = sklearn.cluster.KMeans(n_clusters = n_clusters, random_state = 555).fit_predict(sm.codebook.matrix)

    # fill each rectangular unit area with cluster color
    # and draw line segment to the border of cluster
    norm = mpl.colors.Normalize(vmin=0, vmax=n_palette, clip=True)

    # borders
    ax.pcolormesh(cl_labels.reshape(msz[0], msz[1]).T % n_palette,
        cmap=cmap, norm=norm, edgecolors='face',
        lw=0.5, alpha=0.5)

    ax.scatter(coord[:, 0]+0.5, coord[:, 1]+0.5, c='k', marker='o')
    ax.axis('off')

    for label, x, y in zip(labels, coord[:, 0], coord[:, 1]):
        x += 0.2
        y += 0.2
        # "+ 0.1" means shift of label location to upperright direction

    # randomize the location of the label not to be overwrapped with each other
    # x_text += 0.1 * np.random.randn()
    y += 0.3 * np.random.randn()

    # wrap of label for chemical compound
    # label = str_wrap(label)

    #     ax.text(x+0.3, y+0.3, label,
    #             horizontalalignment='left', verticalalignment='bottom',
    #             rotation=30, fontsize=15, weight='semibold')
        
    plt.title(title)

    # save as png file
    plt.savefig(os.path.join(dir_name, file_name)+".png")