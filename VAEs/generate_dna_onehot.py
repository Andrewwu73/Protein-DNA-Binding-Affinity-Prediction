import numpy as np
from sklearn.preprocessing import OneHotEncoder
from csv import reader
import re
from sklearn.preprocessing import LabelEncoder

class obtainDNAData():
    def __init__(self, directory):
        self.dataset_directory = directory
        self.label_encoder = LabelEncoder()
        self.label_encoder.fit(np.array(['a','c','g','t']))

    def special_match(self, strg, search=re.compile(r'[^atcgATCG]').search):
        return not bool(search(strg))

    def one_hot_encoder(self, my_array):
        integer_encoded = self.label_encoder.transform(my_array)
        onehot_encoder = OneHotEncoder(categories=[range(5)], sparse=False, dtype=int)
        integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
        onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
        onehot_encoded = np.delete(onehot_encoded, -1, 1)
        return onehot_encoded

    #Returns train_data, test_data
    def obtainData(self):

        # open file in read mode
        with open(self.dataset_directory, 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Iterate over each row in the csv using reader object
            dataset_no_repeats = set()
            for row in csv_reader:
                if (self.special_match(row[2])):
                    dataset_no_repeats.add(row[2].lower())
        # dataset_no_repeats = list(dataset_no_repeats)[:len(dataset_no_repeats)//5]
        dataset_no_repeats = list(dataset_no_repeats)[:2]
        print(len(dataset_no_repeats))
        # print(len(dataset_no_repeats))
        max = 0
        # A = np.pad(np.array([[0,1,0,0],[1,0,0,0]]), ((0,4-s.shape[0]),(0,0)), mode='constant')
        for i in dataset_no_repeats:
            if len(i) > max:
                max = len(i)
        data = []
        for i in dataset_no_repeats:
            arr = self.one_hot_encoder(np.array(list(i)))
            arr = np.pad(arr, ((0,max-arr.shape[0]),(0,0)), mode='constant')
            data.append(arr)

        test_index = round(len(data) * 0.9)
        return np.array(data[0:test_index]), np.array(data[test_index:])
