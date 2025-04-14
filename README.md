# Azure Container Apps remote MCP server example

This MCP server uses SSE transport and is authenticated with an API key.

---

## Project Overview

This project is a FastAPI-based Model Context Protocol (MCP) server designed for Azure Container Apps. It provides weather-related tools (such as alerts and forecasts) via a secure, API-key-protected Server-Sent Events (SSE) interface. The server is intended for integration with MCP-compatible clients, such as Visual Studio Code or custom scripts.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KRVaghani/Azure-MCP-Server.git
   cd Azure-MCP-Server
   ```
2. **Install prerequisites:**
   - Python 3.11 or later
   - [uv](https://docs.astral.sh/uv/getting-started/installation/)
3. **Set up the virtual environment and dependencies:**
   ```bash
   uv venv
   uv sync
   ```
4. **Set the API key:**
   ```bash
   export API_KEYS=devkey  # or your chosen key
   ```
5. **Run the server:**
   ```bash
   uv run fastapi dev main.py
   ```

## Client Usage

A sample Python client (`model_request_client.py`) is included for command-line interaction:

```bash
python model_request_client.py
```
- Enter your API key (default: devkey)
- Choose a tool: `get_alerts` (by US state) or `get_forecast` (by latitude/longitude)
- Enter the required parameters
- The server response will be displayed in your terminal

## API Endpoints

- `/sse` (GET): Main SSE endpoint for MCP protocol communication. Requires `x-api-key` header.
- `/messages` (SSE): Used internally for message streaming (session-based).

## Example curl Test

```bash
curl -H "x-api-key: devkey" http://localhost:8000/sse
```

## Troubleshooting

- If you see `ModuleNotFoundError`, ensure your virtual environment is activated and dependencies are installed.
- If the client hangs, check that the server is running and the API key matches.
- For pip issues in the venv, run:
  ```bash
  python -m ensurepip --upgrade
  python -m pip install --upgrade pip
  ```

## Contributing

Pull requests are welcome! Please open an issue first to discuss major changes.

## License

MIT License (add LICENSE file if needed)

## Running locally

Prerequisites:
* Python 3.11 or later
* [uv](https://docs.astral.sh/uv/getting-started/installation/)

Run the server locally:

```bash
uv venv
uv sync

# linux/macOS
export API_KEYS=<AN_API_KEY>
# windows
set API_KEYS=<AN_API_KEY>

uv run fastapi dev main.py
```

VS Code MCP configuration (mcp.json):

```json
{
    "inputs": [
        {
            "type": "promptString",
            "id": "weather-api-key",
            "description": "Weather API Key",
            "password": true
        }
    ],
    "servers": {
        "weather-sse": {
            "type": "sse",
            "url": "http://localhost:8000/sse",
            "headers": {
                "x-api-key": "${input:weather-api-key}"
            }
        }
    }
}
```

## Deploy to Azure Container Apps

```bash
az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
```

If the deployment is successful, the Azure CLI returns the URL of the app. You can use this URL to connect to the server from Visual Studio Code.

If the deployment fails, try again after updating the CLI and the Azure Container Apps extension:

```bash
az upgrade
az extension add -n containerapp --upgrade
```

