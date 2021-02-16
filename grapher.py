from matplotlib import pyplot as plt
from datetime import datetime
class Grapher():



    def read_data(self):

        # for line in open(self.file_name):
        self.x = []
        self.y = []
        with open(self.file_name, self.file_mode) as f:
            for line in f:
                arr = line.split()
                self.x.append( arr[0] )
                self.y.append( int(arr[1]) )


        # print(x)
        # print(y)


    def draw(self):
        
        # plt.plot(x, y)

        plt.xlabel('godzina')
        plt.ylabel('wspomnienia')
        plt.title('Czestotliwosc wzmianek niefiltrowanych')

        plt.xticks(rotation=85)
        plt.bar(self.x, self.y, width=0.4)

        # print (plt.rcParams.keys())
        plt.rcParams.update({
            'axes.facecolor':'red'
        })

        # ax = plt.gca()
        # ax.set_facecolor((0.2, 0.2, 0.2))
        plt.show()


    def __init__(self):

        self.file_name = "mentions.txt"
        self.file_mode = "r"
        self.x = []
        self.y = []




grapher = Grapher()
grapher.read_data()
grapher.draw()