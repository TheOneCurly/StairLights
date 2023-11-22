import network
import time

from credentials import WIFI_SSID, WIFI_Password


def generate_webpage():
    html = f"""
    <!DOCTYPE html>
    <html>

        <head>
            <title>Stair Lights Color Selector</title>
        </head>
        <body>
            <form action="/">
                <select id="colortype">
                    <option>Default(white)</option>
                    <option>Christmas</option>
                    <option>Chaunakah</option>
                    <option>Halloween</option>
                    <option>Valentine's Day</option>
                    <option>Off</option>
                    <option>Custom</option>
                </select>
                <input id="customcolor" type="color">Custom Color</input>
                <button type="submit">Submit</button>
            </form>
        </body>
    </html>
    """


def serve():
    ip = connect()
    connection = open_socket(ip)
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        
        try:
            request = request.split()[1]
        except IndexError:
            pass
        
        print(request)
        
        html = generate_webpage()
        client.send(html)
        client.close()


def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_Password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)

    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    
    
def start():
    connect()
    serve()

