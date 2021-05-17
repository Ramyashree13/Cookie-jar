
from cookiejar import *
import flask as f
app = f.Flask(__name__)

@app.route("/MRA/insert", methods=['POST'])
def create_patient_details():
    if f.request.method == 'POST':
        info = f.request.get_json(force=True)
        insert_patient_details(info)
        return f.jsonify({'status': 'success'}), 201

if __name__ == '__main__':
    app.run(debug=True)