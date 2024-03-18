from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def proxy(path):
    while True:
        try:
            target_url = f"{TARGET_URL}{path}"

            response = requests.request(
                method=request.method,
                url=target_url,
                headers=request.headers,
                data=request.get_data(),
                cookies=request.cookies,
                allow_redirects=False,
                timeout=(3, 3)
            )

            return response.text
        except Exception as e:
            print(e)


if __name__ == '__main__':
    TARGET_URL = input("Please enter the target rpc: ")
    app.run(port=5000)