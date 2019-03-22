#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 22:02:01 2019

@author: jai
"""

from sumy.summarizers.lsa import LsaSummarizer as Summarizer

text = '“This was round about the time when I was doing a lot of thinking about what’s next for me because I’d had a couple of initial chats with Brendan saying to me, ‘I’m going to start managing your games and I have to look after you and I want you to be fresh and I don’t want you to be playing three games in a week because you may be tired’ and stuff like that,” said Gerrard. “But this situation was a bit unique because it was Real Madrid and I wanted to play. I sat on that bench devastated because I wanted to play so, it is one of those situations. It sort of pushed me into making a decision to move on and try something different.”'

from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.html import HtmlParser

url = 'https://www.spotboye.com/television/television-news/kasautii-zindagii-kay-2-that-s-how-hina-khan-aka-komolika-will-exit-from-the-show/5c89eec7aa234148f280f2af'

LANGUAGE = "english"
stemmer = Stemmer(LANGUAGE)

tokenized = Tokenizer(LANGUAGE)

summarizer = Summarizer(stemmer)
summarizer.stop_words = get_stop_words(LANGUAGE)
parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

for sentence in summarizer(parser.document, 5):
    print(sentence)


# SUMMA
    
from summa.summarizer import summarize

summarize(text, words=10)
