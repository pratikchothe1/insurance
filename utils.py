# This file is created to write all functions 
import numpy as np
import json
import pickle 
import config 
import os

class MedicalInsurance():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = "region_" + region

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)           # Here pickle file named as model
        # Here instead of calling linear mode.pkl file directly we have given path of it via config.py file where path is mentioned 
        # This is done for standard practice and to avoid conflits in debugging
            
        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)    # Here project data or label encoded data file is named as json_data
        # Here instead of calling project_data.json file directly we have given path of it via config.py file where path is mentioned 
        # This is done for standard practice and to avoid conflits in debugging

    def get_predict_charges(self): # This is similar to addition function 
        self.load_model() # Here load_model function has been called to run below predicted charges 

        region_index = self.json_data["columns"].index(self.region)
        # here self.region is input received from user like region_northwest
        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.age
        test_array[1] = self.json_data['sex'][self.sex]   # similar to data accessed from project data or label ENCDED Data file
        # here self.sex is input received from user
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.json_data["smoker"][self.smoker]
        test_array[region_index] = 1

        print ("test_array:",test_array)  # 9 values 
        # Here region have 4 columns hence total 9 values comes 

        predicted_charges = np.around(self.model.predict([test_array])[0],2)
        # here test array is 1D hence it is converted to 2D using []
        # here self.model is pickle file name

        return predicted_charges

if __name__ == "__main__":
    age  = 19
    sex  = 'male'
    bmi  = 25 
    children = 2
    smoker = 'yes'
    region = 'southwest'

    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    med_ins.get_predict_charges()
    











