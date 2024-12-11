import requests

'''
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Successfully created issue #123"
      }
    ]
  }
}
'''

def ask_mcp_server(server_url, tool_call, data):
    # Create the MCP protocol blob to request a given toolcall
    body = {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": tool_call,
        "arguments": {
          "title": "User Has Question",
          "body": data,
          "labels": ["health"]
        }
      }
    }
    # Makes the http request
    res = requests.post(f'{server_url}', json=body) 
    print(res.text)
    data = res.json()

    # Extract the data from the response
    return data.get('result',{}).get('content',[])[0].get('text')



if __name__ == '__main__':
    ask_mcp_server("http://localhost:5000", "ask_personal_trainer", "What should I do for my weight?")
