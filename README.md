# Stop Clickbaits

A project aimed at combating 'clickbaits' through the use of Language Models (LLMs).

## Description

The primary goal of this project is to develop a bot, initially on Twitter, capable of being mentioned in a tweet containing clickbait. Upon being triggered, the bot will retrieve the tweet and extract the URL linking to the full article mentioned in the tweet's header. Utilizing this information, an LLM model will complete the header by adding the missing data, and the bot will respond to the user with the article header, providing all the necessary information and thwarting the clickbait.

## Getting Started

### Dependencies

* Python 3.11.6
* A valid API key from together_ai (https://www.together.ai/) (A free 25$ trial is available)

### Installing

1. Create a .env file for dotenv with two environment variables:

```txt
together_key="<YOUR TOGETHER API KEY HERE>"
debug=True
```

* Setting debug=True is convenient for debugging the main.py file by manually selecting a URL and a header. When debug=False, the main.py file prompts for these two arguments from the console, and argparse is used.

2. Install the requirements using:

```shell
pip install -r requirements.txt
```

### Executing program


```
python src/main.py --url <URL with full article> --header <Header with the clickbait>
```


## Authors

Alberto Solano

## Version History

* 0.0

## License

This project is licensed under the Apache License - see the LICENSE.md file for details

## Acknowledgments
