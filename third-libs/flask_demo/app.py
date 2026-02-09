from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    # 监听所有地址，便于在容器或远程环境中访问
    app.run(host='0.0.0.0', port=5000, debug=True)
