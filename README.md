## SOM Graphical User Interface (GUI)

In this GUI we are going to embed the SOM workflow inside GUI to make it easier to use for people who want to use but have no experience in coding.

##### Fields in Data Preprocessing --> coming 
1. Data Cleaning
2. Feature Extraction

##### Fields in SOM:
1. Training
   * Choose the mapsize and SOMFactory build hyperparameters, including:

    | SOMFactory    | sm.train                 |
    | ------------- | -------------            |
    | value         | n_job = 1                |
    | mapsize       | shared_memory = False    |
    | normalization | verbose = "info"         |
    | initialization| train_rough_len          |
    | component_name| train_rough_radiusin     |
    |               | train_rough_radiusfin    |
    |               | train_finetune_len       |
    |               | train_finetune_radiusin  |
    |               | train_finetune_radiusfin |
    |               | train_len_factor = 1     |
    |               | maxtrainlen = inf        |

2. Visualization
   * Heatmaps
   * Cluster Map 
   * UMatrix Map

### Milestones 

##### MVP

This MVP should include the following functions:

1. choose files from local directory (csv format only)
2. choose hyperparameters, following the table above

This MVP is built on the assumption that the csv feed is nxm matrix with valid numerical values for properties users want to train. So the entire dataset is the design matrix that does not need further processing.