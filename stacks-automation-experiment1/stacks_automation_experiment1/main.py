from textwrap import dedent
from .crew import StacksAutomationExperiment1Crew
from IPython.display import Markdown
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/kickoff', methods=['POST'])
def kickoff():
    data = request.json
    #topic = data.get('customer')
    #topic = data.get('topic')
    #data = request.json
    #data = data.get('topic')

    print('===============================')
    print(data)

    if not data:
        return jsonify({'error': 'Topic is required'}), 400

    # Kickoff the crew process
    result = StacksAutomationExperiment1Crew().crew().kickoff(inputs=data)
    #return jsonify({'result': result})
    #result = "success"
    print('===============================')
    return jsonify({'data': result})

def run():
    app.run(debug=True)
