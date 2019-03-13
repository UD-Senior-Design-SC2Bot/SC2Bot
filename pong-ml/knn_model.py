import data_collect

def euclidean_distance(vec1, vec2):
    '''
    Calculates and returns the euclidian distance 
    between vec1 and vec2
    '''
    if (len(vec1) != len(vec2)):
        raise Exception("Vector dimension mismatch: " +
            "vec1 has a dimension of {} but ".format(len(vec1)) +
            "vec2 has a dimension of {}".format(len(vec2)) )
    
    square_sum = 0
    for i in range(0, len(vec1)):
        square_sum += (vec2[i] - vec1[i])**2
    
    return square_sum**(1/2)

class KNNModel():
    '''
    A K-Nearest-Neighbors implementation of ML for
    Pong

    Usage:
        model = KNNModel()
        model.train()

        for frame in game:
            next_move = model.get_next_move(bar_y, ball_x, ball_y)
    '''
    def __init__(self):
        self.training_data = data_collect.deserialize_all_data()
    
    # def train():
    #     # TODO - implement
    #     pass
    
    def get_next_move(bar_y, ball_X, ball_y):
        # TODO - Implement
        pass

# training_data = data_collect.deserialize_all_data()

# dummy_frame = data_collect.FrameData(100, 0, 100, 200, 200)

# distances = []
# for data_set in training_data:
#     for frame in data_set:
#         distances.append(euclidean_distance(frame.to_knn_tensor(), dummy_frame.to_knn_tensor()))

# distances.sort()

# print(distances)
