from flask import Flask, request, jsonify

app = Flask(__name__)

# 상태를 저장하는 변수
led_state = False

@app.route('/endpoint', methods=['POST'])
def handle_request():
    global led_state
    message = request.json.get('message')
    
    if message == "stand in the blue part":
        led_state = not led_state  # LED 상태를 토글
        response_message = "Led on" if led_state else "Led off"
    elif message == "leave the blue part":
        led_state = False  # LED 상태를 끄기
        response_message = "Led off"
    else:
        response_message = "Unknown message"
    
    return jsonify(message=response_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)