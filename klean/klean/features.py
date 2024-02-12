{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "81e1cc6b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import nltk\n",
    "nltk.download()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ea7e83cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = 'Students & Writers mostly look for some questions when coming to paragraph writing about any topic or thing or person. The questions raised by most of the students while thinking about writing a paragraph are Paragraph Writing' \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ff37e977",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Students & Writers mostly look for some questions when coming to paragraph writing about any topic or thing or person.',\n",
       " 'The questions raised by most of the students while thinking about writing a paragraph are Paragraph Writing']"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from nltk import sent_tokenize\n",
    "sent_tokenize(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0c41bf34",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Students',\n",
       " '&',\n",
       " 'Writers',\n",
       " 'mostly',\n",
       " 'look',\n",
       " 'for',\n",
       " 'some',\n",
       " 'questions',\n",
       " 'when',\n",
       " 'coming',\n",
       " 'to',\n",
       " 'paragraph',\n",
       " 'writing',\n",
       " 'about',\n",
       " 'any',\n",
       " 'topic',\n",
       " 'or',\n",
       " 'thing',\n",
       " 'or',\n",
       " 'person',\n",
       " '.',\n",
       " 'The',\n",
       " 'questions',\n",
       " 'raised',\n",
       " 'by',\n",
       " 'most',\n",
       " 'of',\n",
       " 'the',\n",
       " 'students',\n",
       " 'while',\n",
       " 'thinking',\n",
       " 'about',\n",
       " 'writing',\n",
       " 'a',\n",
       " 'paragraph',\n",
       " 'are',\n",
       " 'Paragraph',\n",
       " 'Writing']"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from nltk import word_tokenize\n",
    "word_tokenize(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "8ce2f34e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'go'"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from nltk.stem import WordNetLemmatizer\n",
    "wd=WordNetLemmatizer()\n",
    "wd.lemmatize('goes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "175c7097",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'people'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "wd.lemmatize(\"people\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "a6c50e88",
   "metadata": {},
   "outputs": [],
   "source": [
    "import nltk\n",
    "from nltk.corpus import stopwords"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "34cebd1d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['i',\n",
       " 'me',\n",
       " 'my',\n",
       " 'myself',\n",
       " 'we',\n",
       " 'our',\n",
       " 'ours',\n",
       " 'ourselves',\n",
       " 'you',\n",
       " \"you're\",\n",
       " \"you've\",\n",
       " \"you'll\",\n",
       " \"you'd\",\n",
       " 'your',\n",
       " 'yours',\n",
       " 'yourself',\n",
       " 'yourselves',\n",
       " 'he',\n",
       " 'him',\n",
       " 'his',\n",
       " 'himself',\n",
       " 'she',\n",
       " \"she's\",\n",
       " 'her',\n",
       " 'hers',\n",
       " 'herself',\n",
       " 'it',\n",
       " \"it's\",\n",
       " 'its',\n",
       " 'itself',\n",
       " 'they',\n",
       " 'them',\n",
       " 'their',\n",
       " 'theirs',\n",
       " 'themselves',\n",
       " 'what',\n",
       " 'which',\n",
       " 'who',\n",
       " 'whom',\n",
       " 'this',\n",
       " 'that',\n",
       " \"that'll\",\n",
       " 'these',\n",
       " 'those',\n",
       " 'am',\n",
       " 'is',\n",
       " 'are',\n",
       " 'was',\n",
       " 'were',\n",
       " 'be',\n",
       " 'been',\n",
       " 'being',\n",
       " 'have',\n",
       " 'has',\n",
       " 'had',\n",
       " 'having',\n",
       " 'do',\n",
       " 'does',\n",
       " 'did',\n",
       " 'doing',\n",
       " 'a',\n",
       " 'an',\n",
       " 'the',\n",
       " 'and',\n",
       " 'but',\n",
       " 'if',\n",
       " 'or',\n",
       " 'because',\n",
       " 'as',\n",
       " 'until',\n",
       " 'while',\n",
       " 'of',\n",
       " 'at',\n",
       " 'by',\n",
       " 'for',\n",
       " 'with',\n",
       " 'about',\n",
       " 'against',\n",
       " 'between',\n",
       " 'into',\n",
       " 'through',\n",
       " 'during',\n",
       " 'before',\n",
       " 'after',\n",
       " 'above',\n",
       " 'below',\n",
       " 'to',\n",
       " 'from',\n",
       " 'up',\n",
       " 'down',\n",
       " 'in',\n",
       " 'out',\n",
       " 'on',\n",
       " 'off',\n",
       " 'over',\n",
       " 'under',\n",
       " 'again',\n",
       " 'further',\n",
       " 'then',\n",
       " 'once',\n",
       " 'here',\n",
       " 'there',\n",
       " 'when',\n",
       " 'where',\n",
       " 'why',\n",
       " 'how',\n",
       " 'all',\n",
       " 'any',\n",
       " 'both',\n",
       " 'each',\n",
       " 'few',\n",
       " 'more',\n",
       " 'most',\n",
       " 'other',\n",
       " 'some',\n",
       " 'such',\n",
       " 'no',\n",
       " 'nor',\n",
       " 'not',\n",
       " 'only',\n",
       " 'own',\n",
       " 'same',\n",
       " 'so',\n",
       " 'than',\n",
       " 'too',\n",
       " 'very',\n",
       " 's',\n",
       " 't',\n",
       " 'can',\n",
       " 'will',\n",
       " 'just',\n",
       " 'don',\n",
       " \"don't\",\n",
       " 'should',\n",
       " \"should've\",\n",
       " 'now',\n",
       " 'd',\n",
       " 'll',\n",
       " 'm',\n",
       " 'o',\n",
       " 're',\n",
       " 've',\n",
       " 'y',\n",
       " 'ain',\n",
       " 'aren',\n",
       " \"aren't\",\n",
       " 'couldn',\n",
       " \"couldn't\",\n",
       " 'didn',\n",
       " \"didn't\",\n",
       " 'doesn',\n",
       " \"doesn't\",\n",
       " 'hadn',\n",
       " \"hadn't\",\n",
       " 'hasn',\n",
       " \"hasn't\",\n",
       " 'haven',\n",
       " \"haven't\",\n",
       " 'isn',\n",
       " \"isn't\",\n",
       " 'ma',\n",
       " 'mightn',\n",
       " \"mightn't\",\n",
       " 'mustn',\n",
       " \"mustn't\",\n",
       " 'needn',\n",
       " \"needn't\",\n",
       " 'shan',\n",
       " \"shan't\",\n",
       " 'shouldn',\n",
       " \"shouldn't\",\n",
       " 'wasn',\n",
       " \"wasn't\",\n",
       " 'weren',\n",
       " \"weren't\",\n",
       " 'won',\n",
       " \"won't\",\n",
       " 'wouldn',\n",
       " \"wouldn't\"]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stopwords.words('English'[0:200])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "f98c82dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import string\n",
    "test='This is my firts time in string, im really really excited '"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "a85eac78",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['T',\n",
       " 'h',\n",
       " 'i',\n",
       " 's',\n",
       " ' ',\n",
       " 'i',\n",
       " 's',\n",
       " ' ',\n",
       " 'm',\n",
       " 'y',\n",
       " ' ',\n",
       " 'f',\n",
       " 'i',\n",
       " 'r',\n",
       " 't',\n",
       " 's',\n",
       " ' ',\n",
       " 't',\n",
       " 'i',\n",
       " 'm',\n",
       " 'e',\n",
       " ' ',\n",
       " 'i',\n",
       " 'n',\n",
       " ' ',\n",
       " 's',\n",
       " 't',\n",
       " 'r',\n",
       " 'i',\n",
       " 'n',\n",
       " 'g',\n",
       " ' ',\n",
       " 'i',\n",
       " 'm',\n",
       " ' ',\n",
       " 'r',\n",
       " 'e',\n",
       " 'a',\n",
       " 'l',\n",
       " 'l',\n",
       " 'y',\n",
       " ' ',\n",
       " 'r',\n",
       " 'e',\n",
       " 'a',\n",
       " 'l',\n",
       " 'l',\n",
       " 'y',\n",
       " ' ',\n",
       " 'e',\n",
       " 'x',\n",
       " 'c',\n",
       " 'i',\n",
       " 't',\n",
       " 'e',\n",
       " 'd',\n",
       " ' ']"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "no_punctuation=[char for char in test\n",
    "               if char not in string.punctuation]\n",
    "no_punctuation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "98a2a850",
   "metadata": {},
   "outputs": [],
   "source": [
    "no_punctuation=''.join(no_punctuation)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "908a9bd8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'This is my firts time in string im really really excited '"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "no_punctuation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "8a4df88c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['This',\n",
       " 'is',\n",
       " 'my',\n",
       " 'firts',\n",
       " 'time',\n",
       " 'in',\n",
       " 'string',\n",
       " 'im',\n",
       " 'really',\n",
       " 'really',\n",
       " 'excited']"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "no_punctuation.split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "7ca1902f",
   "metadata": {},
   "outputs": [],
   "source": [
    "clear=[word for word in no_punctuation.split()\n",
    "      if word.lower()not in stopwords.words('english')]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "0ce9108d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['firts', 'time', 'string', 'im', 'really', 'really', 'excited']\n"
     ]
    }
   ],
   "source": [
    "print(clear)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "8bf0b1f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from sklearn.datasets import fetch_20newsgroups"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "71fe63fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "data=fetch_20newsgroups()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "0de5a18d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['alt.atheism',\n",
       " 'comp.graphics',\n",
       " 'comp.os.ms-windows.misc',\n",
       " 'comp.sys.ibm.pc.hardware',\n",
       " 'comp.sys.mac.hardware',\n",
       " 'comp.windows.x',\n",
       " 'misc.forsale',\n",
       " 'rec.autos',\n",
       " 'rec.motorcycles',\n",
       " 'rec.sport.baseball',\n",
       " 'rec.sport.hockey',\n",
       " 'sci.crypt',\n",
       " 'sci.electronics',\n",
       " 'sci.med',\n",
       " 'sci.space',\n",
       " 'soc.religion.christian',\n",
       " 'talk.politics.guns',\n",
       " 'talk.politics.mideast',\n",
       " 'talk.politics.misc',\n",
       " 'talk.religion.misc']"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.target_names"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "cf969947",
   "metadata": {},
   "outputs": [],
   "source": [
    "categories = ['alt.atheism',\n",
    " 'comp.graphics',\n",
    " 'comp.os.ms-windows.misc',\n",
    " 'comp.sys.ibm.pc.hardware',\n",
    " 'comp.sys.mac.hardware',\n",
    " 'comp.windows.x',\n",
    " 'misc.forsale',\n",
    " 'rec.autos',\n",
    " 'rec.motorcycles',\n",
    " 'rec.sport.baseball',\n",
    " 'rec.sport.hockey',\n",
    " 'sci.crypt',\n",
    " 'sci.electronics',\n",
    " 'sci.med',\n",
    " 'sci.space',\n",
    " 'soc.religion.christian',\n",
    " 'talk.politics.guns',\n",
    " 'talk.politics.mideast',\n",
    " 'talk.politics.misc',\n",
    " 'talk.religion.misc']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "a8639d27",
   "metadata": {},
   "outputs": [],
   "source": [
    "train = fetch_20newsgroups(subset=\"train\",categories= categories)\n",
    "test = fetch_20newsgroups(subset=\"test\",categories= categories)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "000a9254",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "From: dfo@vttoulu.tko.vtt.fi (Foxvog Douglas)\n",
      "Subject: Re: Rewording the Second Amendment (ideas)\n",
      "Organization: VTT\n",
      "Lines: 58\n",
      "\n",
      "In article <1r1eu1$4t@transfer.stratus.com> cdt@sw.stratus.com (C. D. Tavares) writes:\n",
      ">In article <1993Apr20.083057.16899@ousrvr.oulu.fi>, dfo@vttoulu.tko.vtt.fi (Foxvog Douglas) writes:\n",
      ">> In article <1qv87v$4j3@transfer.stratus.com> cdt@sw.stratus.com (C. D. Tavares) writes:\n",
      ">> >In article <C5n3GI.F8F@ulowell.ulowell.edu>, jrutledg@cs.ulowell.edu (John Lawrence Rutledge) writes:\n",
      ">\n",
      ">> >> The massive destructive power of many modern weapons, makes the\n",
      ">> >> cost of an accidental or crimial usage of these weapons to great.\n",
      ">> >> The weapons of mass destruction need to be in the control of\n",
      ">> >> the government only.  Individual access would result in the\n",
      ">> >> needless deaths of millions.  This makes the right of the people\n",
      ">> >> to keep and bear many modern weapons non-existant.\n",
      "\n",
      ">> >Thanks for stating where you're coming from.  Needless to say, I\n",
      ">> >disagree on every count.\n",
      "\n",
      ">> You believe that individuals should have the right to own weapons of\n",
      ">> mass destruction?  I find it hard to believe that you would support a \n",
      ">> neighbor's right to keep nuclear weapons, biological weapons, and nerve\n",
      ">> gas on his/her property.  \n",
      "\n",
      ">> If we cannot even agree on keeping weapons of mass destruction out of\n",
      ">> the hands of individuals, can there be any hope for us?\n",
      "\n",
      ">I don't sign any blank checks.\n",
      "\n",
      "Of course.  The term must be rigidly defined in any bill.\n",
      "\n",
      ">When Doug Foxvog says \"weapons of mass destruction,\" he means CBW and\n",
      ">nukes.  When Sarah Brady says \"weapons of mass destruction\" she means\n",
      ">Street Sweeper shotguns and semi-automatic SKS rifles.  \n",
      "\n",
      "I doubt she uses this term for that.  You are using a quote allegedly\n",
      "from her, can you back it up?\n",
      "\n",
      ">When John\n",
      ">Lawrence Rutledge says \"weapons of mass destruction,\" and then immediately\n",
      ">follows it with:\n",
      "\n",
      ">>> The US has thousands of people killed each year by handguns,\n",
      ">>> this number can easily be reduced by putting reasonable restrictions\n",
      ">>> on them.\n",
      "\n",
      ">...what does Rutledge mean by the term?\n",
      "\n",
      "I read the article as presenting first an argument about weapons of mass\n",
      "destruction (as commonly understood) and then switching to other topics.\n",
      "The first point evidently was to show that not all weapons should be\n",
      "allowed, and then the later analysis was, given this understanding, to\n",
      "consider another class.\n",
      "\n",
      ">cdt@rocket.sw.stratus.com   --If you believe that I speak for my company,\n",
      ">OR cdt@vos.stratus.com        write today for my special Investors' Packet...\n",
      "\n",
      "\n",
      "\n",
      "-- \n",
      "doug foxvog\n",
      "douglas.foxvog@vtt.fi\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(train.data[5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "09f20356",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11314\n"
     ]
    }
   ],
   "source": [
    "print(len(train.data))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "90402e8a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7532\n"
     ]
    }
   ],
   "source": [
    "print(len(test.data))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "2e840155",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.pipeline import make_pipeline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "2a2c0f28",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.naive_bayes import MultinomialNB\n",
    "model = make_pipeline(TfidfVectorizer(),MultinomialNB())\n",
    "model.fit(train.data,train.target)\n",
    "labels =model.predict(test.data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "948c0418",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
