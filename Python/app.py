from flask import Flask, render_template,jsonify, request,send_file
from flask_cors import CORS, cross_origin
import json
import pandas as pd

user_df = pd.read_excel("Data/customer_db.xlsx")

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/get_customers", methods=["GET","POST"])
@cross_origin()
def get_cutomers():
    """
    Get customer list

    get:
        fetch customer list
        responses:
            200:
                customer_dict: json of customers
    """
    cutomer_list = list()
    for i, row in user_df.iterrows():
        cutomer_list.append({
            "id": int(row["ID"]),
            "name": row["Name"],
            "email": row["Email"],
            "phone": str(row["Phone"])
        })

    return cutomer_list 


@app.route("/get_customer_details", methods=["GET","POST"])
@cross_origin()
def get_customer_details():
    """
    Get customer details

    get:
        fetch customer details
        responses:
            200:
                customer_detail: json of customer details
    """
    payload = json.loads(request.data)
    id = payload["id"]
    value_dict = user_df.loc[user_df['ID'] == id].iloc[0].to_dict()

    return {
        "id": int(value_dict['ID']),
        "name": value_dict["Name"],
        "email": value_dict["Email"],
        "phone": str(value_dict["Phone"]),
        "city": value_dict["City"],
        "state": value_dict["State"],
        "country": value_dict["Country"],
        "organization": value_dict["Organization"],
        "jobProfile": value_dict["Job Profile"],
        "additionalInfo": value_dict["Comments"]
        }


@app.route("/")
def home():
    print("Calchas")
    return "Backend online!"


if __name__ == "__main__":
    app.run(debug=True)