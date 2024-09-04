from flask import Flask,request,render_template,send_file, jsonify
from inserter import mongo_retriever
from main import nearby_people
from matching import model

application=Flask(__name__)

app=application

@app.route('/')
def ab():
    return 'welcome to roomy'

@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        Name= request.form.get('Name')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        location = (float(latitude), float(longitude))
        Budget= float(request.form.get('Budget'))
        Hobbies = request.form.get('Hobbies')
        Is_Vegetarian = request.form.get('Is_Vegetarian')
    
        mret = mongo_retriever()
        collection = mret.mongo_setup()
        number = collection.count_documents({}) +1
        user_number = 'user'+ str(number)
        collection.insert_one({'user': user_number, 'Name': Name, 'location': (location), 'Budget': Budget, 'Hobbies': Hobbies, 'Is_Vegetarian': Is_Vegetarian})
        loc = nearby_people() 
        collection.drop_indexes()
        cursor = collection.find({}, {'_id': 0})

        nearby_users = loc.find_nearby_users(cursor=cursor, current_user_id=user_number, current_location=location, max_distance=10000)

        ml = model()
        result = ml.fit_it(user_number, nearby=nearby_users)

    return jsonify(result)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)