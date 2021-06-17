import websocket

socket = 'wss://stream.binance.com:9443/ws/btusdt@kline_1m'


def on_message(ws, message):
    print(ws, message)


def on_close(ws):
    print('Conn closed')


def on_error(ws, error):
    print(error)


ws = websocket.WebSocketApp(socket, on_message=on_message, on_close=on_close, on_error=on_error)

ws.run_forever()


