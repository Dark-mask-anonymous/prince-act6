from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html")


@app.route("/student")
def get_student():
	return jsonify(
		{
			"student_id": "24-00310",
			"name": "Prince Reniel Matutina",
			"program": "BSIT",
			"year": 3,
			"section": "b",
		}
	)


@app.route("/hello")
def say_hello():
	name = request.args.get("name", "Student")
	return jsonify({"message": f"Hello, {name}!"})


@app.route("/academic")
def get_academic_profile():
	return jsonify(
		{
			"student_id": "24-00310",
			"program": "BSIT",
			"year": 3,
			"section": "b",
		}
	)


if __name__ == "__main__":
	app.run(debug=True)