import pickle
import os
import logging
from sklearn.tree import DecisionTreeClassifier
def prediction(feature):
    try :
        predictor_load = pickle.load(open(os.path.join("model", "model_tree.pkl"), "rb"))
        result = predictor_load.predict([feature])
        logging.info('prediction load')
        return result
    except Exception as e:
        logging.error(f"could not insert data due to {e}")

