from flask import Flask, render_template, request
import pickle
app = Flask(__name__)

file = open('model.pkl','rb')
clf = pickle.load(file)
file.close()

@app.route('/', methods = ["GET","POST"])
def hello_world():
    if request.method == "POST":
        myDict = request.form
        print(myDict)
        name = myDict['name']
        cp = int(myDict['cp'])
        trestbps = int(myDict['trestbps'])
        sex = int(myDict['sex'])
        age = int(myDict['age'])
        fbs= int(myDict['fbs'])
        chol = int(myDict['chol'])
        restecg = int(myDict['restecg'])
        slope = int(myDict['slope'])
        ca = int(myDict['ca'])
        thalach = int(myDict['thalach'])
        exang = int(myDict['exang'])
        oldpeak = float(myDict['oldpeak'])
        thal = int(myDict['thal'])
        print(myDict)
        enter = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        print(enter)
        infProb = clf.predict_proba([enter])
        x = infProb[0][1]*100
        result=''
        if x>50: result='you need to consult a doctor asap'
        else: result='No need to worry'
        return render_template('show.html',name=name,inf = int(x),age=age,sex='male' if sex==1 else 'female',result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
