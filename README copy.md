# Echo Bot

A simple API to introduce the concepts of Fetching and REST APIs.

## Usage

### `POST /echo`

#### Parameters

- `text` (str): The text to transform

#### Returns

- `text` (str): The transformed string.

#### Example

```sh
curl -X POST https://echo-bot-shy-sea-4425.fly.dev/echo -d '{"text": "My text"}' -H "Content-Type: application/json"
# => {"text":"MY  TEXT"}
```
