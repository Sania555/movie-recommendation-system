from flask import Flask, render_template, request, jsonify
from model import make_recommendation

app = Flask(__name__, template_folder='./')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/get')
def get_from_api():
    try:
        # Get user message from URL param
        query = request.args.get('msg', '')

        if not query:
            return jsonify({"error": "No query provided"}), 400

        # Call your model function
        recommendations = make_recommendation(str(query))

        # Return JSON response
        return jsonify(recommendations)

    except Exception as e:
        # Print error to console and return JSON error
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
