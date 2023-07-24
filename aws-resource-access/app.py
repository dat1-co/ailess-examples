import boto3
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def root():
    return jsonify("OK")


@app.route("/buckets", methods=["GET"])
def buckets():
    s3 = boto3.resource('s3')
    bucket_list = []
    for bucket in s3.buckets.all():
        bucket_list.append(bucket.name)
    return jsonify(bucket_list)


if __name__ == "__main__":
    from waitress import serve

    print("Starting server")
    serve(app, host="0.0.0.0", port=8080)
