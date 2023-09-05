import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

data_limit = 10

def fetch_and_categorize_data(limit):
    external_api = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(external_api)

    if response.status_code == 200:
        data = response.json()
        categorized_data = {}
        for item  in data[:limit]:
            category = item['userId'] % 2
            if category not in categorized_data:
                categorized_data[category] = []
            categorized_data[category].append(item)

        return categorized_data
    else:
        return None

@app.route('/api/categorized_data', methods=['GET'])
def get_categorized_data():
    limit = int(request.args.get('limit', data_limit))
    categorized_data = fetch_and_categorize_data(limit)
    if categorized_data:
        return jsonify(categorized_data)
    else:
        return jsonify({'Error': 'Failed to fetch data from external API'})

@app.route('/api/set_limit/<int:limit>', methods=['GET'])
def set_data_limit(limit):
    global data_limit
    data_limit = limit
    return jsonify({'message': f'Data limit set to {limit}'})

if __name__ == '__main__':
    app.run(debug=True)
