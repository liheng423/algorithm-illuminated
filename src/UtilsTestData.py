import UtilsData as Data
import os

if __name__ == "__main__":
    path = "/Users/blow/PycharmProjects/Algorithms/testcases"
    os.chdir(path)
    print(Data.graph_data_loader("./bellman-ford-test.csv"))
