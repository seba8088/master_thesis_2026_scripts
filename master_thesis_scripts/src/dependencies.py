# libraries
import csv
import logging
import os
import re
import string
import warnings
from collections import Counter, defaultdict
from datetime import date, datetime

import emoji
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.ticker import FuncFormatter
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import praw
import prawcore
import seaborn as sns
import spacy
import time
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, CountVectorizer
from corextopic import corextopic as ct
from pyabsa import AspectPolarityClassification as APC
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
from bertopic import BERTopic
from bertopic.representation import KeyBERTInspired
from sentence_transformers import SentenceTransformer
from scipy.stats import permutation_test
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.proportion import proportion_effectsize

from transformers import DebertaV2Config

# patching DebertaV2Config to avoid error when loading the model
if not hasattr(DebertaV2Config, 'is_decoder'):
    DebertaV2Config.is_decoder = False

# load spaCy English model for lemmatization, disabling NER to speed up processing since it is not needed
nlp = spacy.load("en_core_web_md", disable=["ner"])

# variables
data_folder = os.path.join('..', 'data')
raw_csv_filename = 'reddit_lego_smart_brick_data_raw.csv'
raw_tsv_filename = 'reddit_lego_smart_brick_data_raw.tsv'
preprocessed_csv_filename = 'reddit_lego_smart_brick_data_preprocessed.csv'
preprocessed_tsv_filename = 'reddit_lego_smart_brick_data_preprocessed.tsv'
aspect_based_sentiment_csv_filename = 'aspect_based_sentiments.csv'
aspect_based_sentiment_tsv_filename = 'aspect_based_sentiments.tsv'
absa_checkpoint_filename = 'absa_checkpoint.csv'
raw_csv_filepath = os.path.join(data_folder, raw_csv_filename)
raw_tsv_filepath = os.path.join(data_folder, raw_tsv_filename)
preprocessed_csv_filepath = os.path.join(data_folder, preprocessed_csv_filename)
preprocessed_tsv_filepath = os.path.join(data_folder, preprocessed_tsv_filename)
aspect_based_sentiment_csv_filepath = os.path.join(data_folder, aspect_based_sentiment_csv_filename)
aspect_based_sentiment_tsv_filepath = os.path.join(data_folder, aspect_based_sentiment_tsv_filename)
absa_checkpoint_filepath = os.path.join(data_folder, absa_checkpoint_filename)

# defining subreddit groupings
legostarwars_subs = ['legostarwars', 'legostarwarsleaks']
lego_subs = ['lego', 'legoleak', 'legonewsandrumors', 'legosmartbrick']

# defining time periods
time_periods = ('t₁','t₂')
