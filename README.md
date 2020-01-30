## SOM Graphical User Interface (GUI)

In this GUI we are going to embed the SOM workflow inside GUI to make it easier to use for people who want to use but have no experience in coding.

##### Fields in Data Preprocessing --> coming 
1. Data Cleaning
2. Feature Extraction

##### Fields in SOM:
1. Training
   * Choose the mapsize and SOMFactory build hyperparameters, including:

    | SOMFactory           | sm.train                 |
    | -------------------- | ------------------------ |
    | data                 | n_job = 1                |
    | mapsize=None         | shared_memory = False    |
    | normalizer=None      | verbose = "info"         |
    | initialization='pca' | train_rough_len          |
    | lattice='rect'       | train_rough_radiusin     |
    | neighborhood         | train_rough_radiusfin    |
    | mask=None            | train_finetune_len       |
    | mapshape='planar'    | train_finetune_radiusin  |
    | training='batch'     | train_finetune_radiusfin |
    | name='sompy'         | train_len_factor = 1     |
    | component_names=None | maxtrainlen = inf        |


2. Visualization
   * Heatmaps
   * Cluster Map 
   * UMatrix Map

##### MVP

This MVP should include the following functions:

1. choose files from local directory (csv format only)
2. choose hyperparameters, following the table above

This MVP is built on the assumption that the csv feed is nxm matrix with valid numerical values for properties users want to train. So the entire dataset is the design matrix that does not need further processing.


### Milestone

##### Milestone 1 (1/23/2020):

In the one_page_all.py I have designed a one-page frame for people to input hyperparameters of SOM model and click to train. I consider the output of visualizations and export them to png files. The click events need to be embedded. The tool I used is a tkinter GUI designer called PAGE, one can be found on sourceforge: http://page.sourceforge.net/. 

In order to run that you need to download ActiveTcl, one can be found here: https://www.activestate.com/products/tcl/ 

In this repository, the user can create a working environment first, then install tkinter. One then can run command to start the GUI:
`
python one_page_all.py
`

##### 1/27/2020

For some reason jupyter does not start successfully based on the current environment.yml, but the rest of them function normally. I would ignore this issue right now and focus getting the MVP done soon. 

1. I have successfully trained the model using GUI
2. I need to automate visualization generation
3. Make the progress bar work


The training phase and visualization phase are separated. After training the model we can select any of them (if you trained multiple) and generate visualization based on them.