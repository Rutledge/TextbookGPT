# TextbookGPT (developer access only)

A ChatGPT plugin to chat with textbooks, with support for **textbook diagrams**.

See [DEMO VIDEO](https://youtube.com/shorts/8E2pUd9RiGQ?feature=share) and follow author on twitter <https://twitter.com/lessand_ro> to get updated for our next release!

## Diagram

ChatGPT answers your questions with diagram from textbook, citing sources!

![](./demo1.png)
![](./demo2.png)


## Text Only

This is an example of asking the "Deep Learning Textbook" for exact quotes on backpropagation. This is from the `text-only` branch of the repo.

![](./demo3.png)
![](./demo4.png)

Watch the [demo video with more prompts](https://www.loom.com/share/d1705c068a2141c5934d25211477d21a) 

## Usage

To use the plugin you need to be in the OpenAI Plugins early access allowlist.

*Deploy this repo on replit to use it or DM me at <https://twitter.com/lessand_ro> to have access!*

## Developer Access Quickstart

This is a fork of https://github.com/openai/chatgpt-retrieval-plugin. 

1. Follow that tutorial to set up your vector database

To add your own textbook you will need (beside the standard repo setup explained in OpenAI repo readme)
2. a file in the form `scripts/process_books/deeplearning.json` 
3. call the command `python scripts/process_books/process_json.py --filepath deeplearning.json`

4. deploy the plugin and use it!


This repo adds from the original

- scripts for book manipulation under `scripts/process_book`
- updated textbook datamodel (e.g. chapters and diagrams)
- updated textbook queries and api prompting 



