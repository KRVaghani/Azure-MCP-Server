# model_request_client.py
"""
A simple command-line client to interact with the running MCP server via SSE.
Allows you to call 'get_alerts' or 'get_forecast' tools and prints the server response.
"""
import requests
import sseclient
import json

# def get_sse_response(api_key, tool, params):
#     import urllib.parse
#     url = "http://localhost:8000/sse"
#     headers = {"x-api-key": api_key}
#     # Add tool and params as query parameters
#     query = {"tool": tool, **params}
#     full_url = url + "?" + urllib.parse.urlencode(query)
#     # Open SSE connection
#     client = sseclient.SSEClient(requests.get(full_url, headers=headers, stream=True))
#     print(f"\n--- Server response for {tool} ---")
#     for event in client.events():
#         print(event.data)
#         break  # Print only the first event for demo

def get_sse_response(api_key, tool, params):
    import urllib.parse
    url = "http://localhost:8000/sse"
    headers = {"x-api-key": api_key}
    query = {"tool": tool, **params}
    full_url = url + "?" + urllib.parse.urlencode(query)
    # Pass the URL and headers directly to SSEClient
    client = sseclient.SSEClient(full_url, headers=headers)
    print(f"\n--- Server response for {tool} ---")
    for event in client:
        print(event.data)
        break  # Print only the first event for demo

def main():
    print("MCP Model Request Client\n-------------------------")
    api_key = input("Enter API key (default: devkey): ") or "devkey"
    print("Choose a tool to call:")
    print("1. get_alerts (by US state)")
    print("2. get_forecast (by latitude/longitude)")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        state = input("Enter US state code (e.g., CA): ")
        get_sse_response(api_key, "get_alerts", {"state": state})
    elif choice == "2":
        lat = float(input("Enter latitude: "))
        lon = float(input("Enter longitude: "))
        get_sse_response(api_key, "get_forecast", {"latitude": lat, "longitude": lon})
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
