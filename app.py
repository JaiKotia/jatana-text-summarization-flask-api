#!flask/bin/python

from flask import Flask, request, jsonify
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.html import HtmlParser

app = Flask(__name__)

@app.route('/summarize_url', methods=['POST'])
def summarize_url():
    if not request.json or not 'url' in request.json:
        abort(400)
    url = request.json['url']

    LANGUAGE = "english"
    summary = ''
    stemmer = Stemmer(LANGUAGE)
    tokenized = Tokenizer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

    for sentence in summarizer(parser.document, 5):
        summary += str(sentence)

    return summary

if __name__ == '__main__':
    app.run(debug=True)
