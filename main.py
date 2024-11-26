print("Let's have some fun!")

import http.client

def make_request():
    # Define the host and port
    host = "localhost"
    port = 5007

    # Create a connection to the server
    connection = http.client.HTTPConnection(host, port)

    try:
        connection.request("GET", "/")
        response = connection.getresponse()
        print(f"Status: {response.status} {response.reason}")
        body = response.read().decode('utf-8')
        print(f"Response body:\n{body}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    make_request()
