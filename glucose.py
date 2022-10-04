from flask import Flask, jsonify, request

app = Flask(__name__)

glucose = [
    {
        "glucose_id" : "01",
        "date" : ["10-04-22"],
        "glucose_rate" : [ "140"]
    },
    {
        "glucose_id" : "02",
        "date" : ["11-04-22"],
        "glucose_rate" : [ "130"]
    },
    {
        "glucose_id" : "03",
        "date" : ["10-04-22"],
        "glucose_rate" : [ "160"]
    },
]
@app.route ('/glucose', methods=['GET'])
def getGlucose():
    return jsonify(glucose)
@app.route('/glucose', methods=['POST'])
def addGlucose():
    glucose = request.get_json()
    glucose.append(glucose)
    return {'id': len(glucose)},200

@app.route('/glucose/<int:index>', methods=['DELETE'])
def deleteGlucose(index):
    glucose.pop(index)
    return ' ID was deleted successfully' , 200

if __name__ ==  '__main__':
    app.run()