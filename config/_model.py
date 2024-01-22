import numpy as np


inertia_tensor_digits = {
    0: np.array(
        [[ 2.88888889, -0.        ],
        [-0.,          6.02777778]]
    ),
    1: np.array(
        [[ 0.26446281, -0.26446281],
        [-0.26446281,  6.44628099]]
    ),
    2: np.array(
        [[2.,         0.66666667],
        [0.66666667, 8.02666667]]
    ),
    3: np.array(
        [[ 1.98222222, -0.04888889],
        [-0.04888889,  6.91555556]]
    ),
    4: np.array(
        [[ 1.39555556, -0.17777778],
        [-0.17777778,  3.42222222]]
    ),
    5: np.array(
        [[ 2.32098765, -0.68518519],
        [-0.68518519,  6.69444444]]
    ),
    6: np.array(
        [[ 2.1799308,  -0.26643599],
        [-0.26643599,  5.0449827 ]]
    ),
    7: np.array(
        [[1.47222222, 0.88888889],
        [0.88888889, 6.22222222]]
    ),
    8: np.array(
        [[ 2.42105263, -0.        ],
        [-0.,          5.72299169]]
    ),
    9: np.array(
        [[ 2.1799308,  -0.26643599],
        [-0.26643599,  5.0449827 ]]
    )
}

digit_centroids = {
    "0": [3.5, 2. ],
    "1": [3.90909091, 0.90909091],
    "2": [3.8, 2. ],
    "3": [3.46666667, 2.46666667],
    "4": [3.33333333, 2.26666667],
    "5": [3.16666667, 1.88888889],
    "6": [3.88235294, 1.76470588],
    "7": [2.33333333, 2.16666667],
    "8": [3.47368421, 2.        ],
    "9": [3.11764706, 2.23529412],    
}