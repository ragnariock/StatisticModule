import math
import matplotlib.pyplot as plt
import numpy as np


class Stat:
    def __init__(self):
        pass

    @staticmethod
    def draw_plot_hist(x, discrt='plot'):
        plt.hist(x)
        plt.ylabel(discrt)
        plt.show()

    @staticmethod
    def normal():
        return np.random.normal(0, 0.1, 1000)

    @staticmethod
    def get_ave_value(x: list):
        return sum(x) / len(x)

    @staticmethod
    def most_frequent(X):
        return max(set(X), key=X.count)

    def get_mod_value(self, x: list, num_mods: int = 1):
        result_mods = []
        x = x.copy()
        for i in range(num_mods):
            mod_value = self.most_frequent(x)
            while True:
                try:
                    x.remove(mod_value)
                except:
                    break
            result_mods.append(mod_value)

        return result_mods

    @staticmethod
    def get_median(X: list):
        X = X.copy()
        X.sort()
        median_index = len(X) / 2

        if type(median_index) != int():
            median_index = len(X) // 2
            addition_index_left = median_index - 1
            return (X[median_index] + X[addition_index_left]) / 2

        return X[median_index]

    def get_dirs(self, x: list):
        avg_value = self.get_ave_value(x)
        result = 0
        for i in range(len(x)):
            result += math.pow((x[i] - avg_value), 2)
        return result

    def avg_deviation(self, x):
        disp = self.get_dirs(x)
        return math.sqrt(disp)

    def standard_z(self, x: list):
        avg = self.get_ave_value(x)
        disp = self.avg_deviation(x)
        z_list = []
        for i, value in enumerate(x):
            z_list.append((value - avg) / disp)
        return z_list

    def standard_mistake(self, x: list):
        return self.avg_deviation(x) / math.sqrt(len(x))


stat_module = Stat()

list_x = [1, 2, 3, 4, 5, 5, 3, 3, 3, 100]

print("Mod = ", stat_module.get_mod_value(list_x, num_mods=3))
print("Median = ", stat_module.get_median(list_x))
print("Ave value - ", stat_module.get_ave_value(list_x))
print("Disp - ", stat_module.get_dirs(list_x))
print("avg_deviation - ", stat_module.avg_deviation(list_x))
print("standard_mistake - ", stat_module.standard_mistake(list_x))

z_list = stat_module.standard_z(list_x)

print("\nMod z_list= ", stat_module.get_mod_value(z_list, num_mods=1))
print("Median z_list= ", stat_module.get_median(z_list))
print("Ave value z_list = ", stat_module.get_ave_value(z_list))
print("Disp z_list =  ", stat_module.get_dirs(z_list))
print("avg_deviation z_list = ", stat_module.avg_deviation(z_list))
print("standard_mistake z_list - ", stat_module.standard_mistake(z_list))

normal_distr = stat_module.normal()

stat_module.draw_plot_hist(z_list, discrt='z_values')
stat_module.draw_plot_hist(list_x, discrt='x_values')
stat_module.draw_plot_hist(normal_distr, discrt='normal')