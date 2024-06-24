import pickle
import os
import logging
from sklearn.exceptions import InconsistentVersionWarning

def prediction(feature):
    try :
        predictor_load = pickle.load(open(os.path.join("model", "model_tree.pkl"), "rb"))
        result = predictor_load.predict(feature)
        print('prediction load:', predictor_load)
        return result
    except InconsistentVersionWarning as w:
        logging.error(f"could not load predictor {w}")



StudyTimeWeekly = 19
Absences = 11 
Tutoring  = 1
ParentalSupport = 4 
Sports = 1
Music  = 1
Volunteering = 0
save = [StudyTimeWeekly, Absences, Tutoring, ParentalSupport, Sports, Music, Volunteering]
print(prediction(save))
# decision_tree_pkl_filename = "model/model_tree.pkl"
# decision_tree_model_pkl = open(decision_tree_pkl_filename, 'rb')
# decision_tree_model = pickle.load(decision_tree_model_pkl)
# print("Loaded Decision tree model :: ", decision_tree_model)