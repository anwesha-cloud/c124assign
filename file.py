from flask import Flask,jsonify,request

app=Flask(__name__)
data=[
    {
        'Contact':2458464985,
        'Name':'Raju',
        'done':False,
        'id':1
    },
    {
        'Contact':8955475321,
        'Name':'Sonu',
        'done':False,
        'id':2
        
    }
]

@app.route('/get-contacts')
def getData():
    return jsonify({
        'data':data,
        })

@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'ERROR',
            'message':"Request Unsuccessful! Please provide the data!"
        },400)
    
    contact={
        'id':data[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json['Contact'],
        'done':False
    }

    data.append(contact)
    return jsonify({
        'status':'SUCCESS',
        'message':"Request Successful! Task added successfully"
    })

if __name__ == '__main__':
    app.run(debug=True)