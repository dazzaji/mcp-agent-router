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

def ask_personal_trainer(question):
    body = {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "ask_personal_trainer",
        "arguments": {
          "title": "User Has Question",
          "body": question,
          "labels": ["health"]
        }
      }
    }
    res = requests.post('http://localhost:5000/mcp/v1', json=body) 
    print(res.text)
    data = res.json()

    return data.get('result',{}).get('content',[])[0].get('text')



if __name__ == '__main__':
    ask_personal_trainer("What should I do for my weight?")
