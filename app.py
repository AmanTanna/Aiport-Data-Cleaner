from flask import Flask, request, render_template, jsonify
import pandas as pd
from io import StringIO
import re
import json

app = Flask(__name__)

def cleanAirportData(data):
    # Load the raw semicolon-delimited string into a DataFrame
    df = pd.read_csv(StringIO(data), sep=';', engine='python')
    # 1) Split the combined "To_From" column into two new columns "From" and "To"
    df[["From", "To"]] = (
        df["To_From"].str.upper().str.split("_", n=1, expand=True)
    )
    # Drop the original composite column, since it is now in two parts
    df.drop(columns="To_From", inplace=True)
    # Clean up the "Airline Code" field by applying `cleanAirlineCode` function on the column
    cleanAirlineCode = lambda x: re.sub(r'[^A-Za-z ]+', "", x).strip().title()
    df["Airline Code"] = df["Airline Code"].apply(cleanAirlineCode)
    # Normalize "FlightCodes"
    # Interpolate missing values (default is linear) and remove floating points
    df["FlightCodes"] = pd.to_numeric(df["FlightCodes"], errors="coerce")
    df["FlightCodes"] = df["FlightCodes"].interpolate().astype(int)
    return df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clean-data', methods=['POST'])
def clean_data():
    raw_data = request.form['raw_data']
    try:
        cleaned_df = cleanAirportData(raw_data)
        # Convert DataFrame to JSON for passing to frontend
        columns = cleaned_df.columns.tolist()
        data = cleaned_df.values.tolist()
        return jsonify({
            'success': True,
            'columns': columns,
            'data': data
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)

app.debug = False
