from flask import Flask, jsonify, render_template, request, redirect,url_for
import config 
from utils import MedicalInsurance

app = Flask(__name__)

#############################################################################
#############################  Test API  ####################################
#############################################################################
## let's run HTML code file saved as home.html in folder

# @app.route("/")   ## Home API
# def hello_flask():
#     print ("welcome to flask")
#     return "Hello Pratik"

# Advance Method
@app.route('/')   # Home API
def student():
    print ("test executed")
    return render_template("user.html")

'''In above code with URL enter /result/name
It will print the result with the name in output 
like Hello pratik'''

## Extra knowledge code to be done by html developer
# @app.route("/medin_result",methods = ["POST","GET"])  
# def login():
#     if request.method == "POST":
#         data = request.form
#         prnt_name = data["name"]
#         print ("Name::",prnt_name)
#         return redirect(url_for('result',name = prnt_name))
         
'''In above code we have requested the input from login.html file into API by using redirect(url_for) in return
Here we have accessed the data from '''

@app.route("/predict_result",methods = ["POST","GET"]) 
def get_insurance_charges():
    # for rendering results on HTML GUI
    if request.method == "POST":
        data = request.form
        print (f"Data is {data}")
        age = data["age"]
        sex = data["sex"]
        bmi = data["bmi"]
        children = data["children"]
        smoker = data["smoker"]
        region = data["region"]

    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charge = med_ins.get_predict_charges()

    # return render_template ('login.html',prediction_text-f'predicted Class:{prediction}')
    return render_template("result.html",charge = charge)

if __name__ == "__main__":
    app.run ()   # Server start
 
 











    
