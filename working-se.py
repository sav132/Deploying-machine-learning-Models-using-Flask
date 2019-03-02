from flask import Flask, request, render_template
import numpy as np
import pickle



app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
	    #temperature = request.form['temperature']
	a = request.form['temperature']
	b = request.form['thal']
	c = request.form['resting_blood_pressure']
	d = request.form['chest_pain_type']
	e = request.form['num_major_vessels']
	f = request.form['fasting_blood_sugar']
	g = request.form['resting_ekg_results']
	h = request.form['serum_cholesterol']
	i = request.form['oldpeak_eq_st_depression']
	j = request.form['sex']
	k = request.form['age']
	l = request.form['max_heart_rate_achieved']
	m = request.form['exercise_induced_angina']
	         

	testData = np.array([a,b,c,d,e,f,g,h,i,j,k,l,m]).reshape(1,13)
	class_prediced = int(heartModel.predict(testData)[0])
	output = "Predicted Class: " + str(class_prediced)
	



	if class_prediced==0:
		output = "Patient has no heart disease"
		return (output)

	elif class_prediced ==1:
		output = "Patient has heart disease"	
		return (output)	

	return "error"





def load_model():
	global heartModel
	
	heartFile = open('models/model.pckl', 'rb')
	heartModel = pickle.load(heartFile)
	heartFile.close()





if __name__ == "__main__":
	print("**Starting Server...")
	load_model()
	# Run Server
	app.run()

