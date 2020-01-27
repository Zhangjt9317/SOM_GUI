# read data
import pandas as pd

def read_data(data_file):
    """
    input: csv file chosen from the directory
    """
    # data_file = self.Data_entry.get()
    try:
        f = open(str(data_file))
    except IOError:
        print("File not accessible")
    finally:
        return pd.read_csv(data_file)

if __name__ == "__main__":
    d = read_data("virtdata.csv")
    print(d)