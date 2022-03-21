from flask import Flask, jsonify, request


app = Flask(__name__)


contacts = [

    {

    "PhoneNum" : "9876543210",

    "Name" : "Raju",

    "done" : "false",

    "id" : 1

    },


    {
    "PhoneNum" : "0123456789",

    "Name" : "Rahul",

    "done" : "false",

    "id" : 2

    }
]

@app.route("/add_data", methods=["POST"])

def add_contact():

    if not request.json:

        return jsonify({

            "status": "error",

            "message": "Please provide the data!"

        }, 400)


    contact = {

        "id": contacts[-1]["id"]+1,

        "Name":request.json["Name"],

        "PhoneNum":request.json.get('PhoneNum',""),

        "done": False

    }


    contacts.append(contact)


    return jsonify({

        "status":"success",

        "message": "Contact added succesfully !!"

    })


@app.route('/getdata')


def get_contact():

    return jsonify({

        "data": contacts

    })


if(__name__ == '__main__'):

    app.run(debug = True)