# slack-block-convertor
This is a set of tools for converting Slack blocks from json to Python Models


# Development Server
Setup a virtual environment for the project using the following command

```
python3.9 -m venv slackconv-39
```

Activate the virtual environment using

```
source slackconv-39/bin/activate
```

Install the required libraries using

```
pip install -r requirements.txt
```

Go to the converter directory and execute the following command

```
uvicorn main:app --host 0.0.0.0 --port 8080
```

The server should be available at http://localhost:8080/

# API Docs

This can be viewed at http://localhost:8080/docs

## Example payload

### Request
```
{
  "blocks": [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "New request"
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*Type:*\nPaid Time Off"
            },
            {
                "type": "mrkdwn",
                "text": "*Created by:*\n<example.com|Fred Enriquez>"
            }
        ]
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*When:*\nAug 10 - Aug 13"
            }
        ]
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "<https://example.com|View request>"
        }
    }
  ]
}
```

### Response

```
{
  "output": [
    "HeaderBlock(text=PlainTextObject(text=\"New request\"))",
    "SectionBlock(fields=[MarkdownTextObject(text=\"*Type:*\nPaid Time Off\"), MarkdownTextObject(text=\"*Created by:*\n<example.com|Fred Enriquez>\")])",
    "SectionBlock(fields=[MarkdownTextObject(text=\"*When:*\nAug 10 - Aug 13\")])",
    "SectionBlock(text=MarkdownTextObject(text=\"<https://example.com|View request>\"))"
  ],
  "errors": ""
}
```
