from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/Beat_Report_Final', methods=['GET'])
def get_manday():
    return process_report_1('CP_Master.csv')

@app.route('/Beat_Report_Final_2', methods=['GET'])
def get_manday_2():
    return process_report_2('CP_Master2.csv')

@app.route('/Beat_Report_By_BeatName', methods=['GET'])
def get_beat_name_report():
    return process_beat_report('Beat_Salesman_Name.csv')

def process_report_1(filename):
    try:
        df = pd.read_csv(filename, sep='|', quotechar='"', skipinitialspace=True, encoding='utf-8').fillna('')

        df['contact'] = df['contact'].astype(str).str.split('.').str[0].str.strip()
        df['Customer_Name'] = df['Customer_Name'].astype(str).str.strip()
        df['Beat_Index_No'] = df['Beat_Index_No'].astype(str).str.split('.').str[0].str.strip()
        df['Outlet_Index_No'] = df['Outlet_Index_No'].astype(str).str.split('.').str[0].str.strip()

        contact = request.args.get('contact', '').strip()
        customer_name = request.args.get('Customer_Name', '').strip()
        Beat_Index_No = request.args.get('Beat_Index_No', '').strip()
        Outlet_Index_No = request.args.get('Outlet_Index_No', '').strip()


        if contact:
            df = df[df['contact'] == contact]

        if customer_name:
            name_list = [name.strip().lower() for name in customer_name.split(',')]
            df = df[df['Customer_Name'].str.lower().isin(name_list)]

        if Beat_Index_No:
            df = df[df['Beat_Index_No']==Beat_Index_No]
            
        if Outlet_Index_No:
            df = df[df['Outlet_Index_No']==Outlet_Index_No]

        return jsonify(df.to_dict(orient='records'))

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
def process_report_2(filename):
    try:
        df = pd.read_csv(filename, sep='|', quotechar='"', skipinitialspace=True, encoding='utf-8').fillna('')

        df['contact'] = df['contact'].astype(str).str.split('.').str[0].str.strip()
        df['Customer_Name'] = df['Customer_Name'].astype(str).str.strip()
        df['Beat_Index_No'] = df['Beat_Index_No'].astype(str).str.split('.').str[0].str.strip()
        df['Outlet_Index_No'] = df['Outlet_Index_No'].astype(str).str.split('.').str[0].str.strip()

        contact = request.args.get('contact', '').strip()
        customer_name = request.args.get('Customer_Name', '').strip()
        Beat_Index_No = request.args.get('Beat_Index_No', '').strip()
        Outlet_Index_No = request.args.get('Outlet_Index_No', '').strip()


        if contact:
            df = df[df['contact'] == contact]

        if customer_name:
            name_list = [name.strip().lower() for name in customer_name.split(',')]
            df = df[df['Customer_Name'].str.lower().isin(name_list)]

        if Beat_Index_No:
            df = df[df['Beat_Index_No']==Beat_Index_No]
            
        if Outlet_Index_No:
            df = df[df['Outlet_Index_No']==Outlet_Index_No]

        return jsonify(df.to_dict(orient='records'))

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def process_beat_report(filename):
    try:
        df = pd.read_csv(filename, sep='|', quotechar='"', skipinitialspace=True, encoding='utf-8').fillna('')

        df['contact'] = df['contact'].astype(str).str.split('.').str[0].str.strip()
        df['Beat_Index_No'] = df['Beat_Index_No'].astype(str).str.split('.').str[0].str.strip()

        contact = request.args.get('contact', '').strip()
        Beat_Index_No = request.args.get('Beat_Index_No', '').strip()

        if contact:
            df = df[df['contact'] == contact]

        if Beat_Index_No:
            df = df[df['Beat_Index_No']==Beat_Index_No]

        return jsonify(df.to_dict(orient='records'))

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
