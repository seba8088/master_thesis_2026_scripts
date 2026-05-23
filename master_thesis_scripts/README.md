# Repository for Master thesis in Social Data Science

## Description
This repository contains the scripts used to collect, processs, and analyse data in connection with my Master thesis in Social Data Science, 2026.

## Scripts
The repository contains the following scripts; all have been made using Python version 3.13.13.
- ### reddit_data_retrieval_script.ipynb
-- This script retrieves raw data using the Reddit API
- ### data_preprocessing_script.ipynb
-- This script pre-processes the raw data
- ### keyword_expansion_script.ipynb
-- This script uses FastText, Anchored CorEx and BERTopic for keyword- and topic expansion
- ### aspect_based_sentiment_analysis.ipynb
-- This script quantifies the pre-processed data using aspect based sentiment analysis (ABSA)
- ### descriptive_analytics_and_visuals.ipynb
-- This script provides descriptive stats and visuals of the pre-processed and ABSA data
- ### permutation_test_script.ipynb
-- This scripts runs permutation tests on the ABSA data

## Dependencies
The scripts depend on depedencies.py, which contains import of libraries and definition of key variables and paths, as well as keywords.py which contains the dictionaries of keyword sets for the product quality features. 
Additionally, they depend on credentials.py, which is not included as it contains the personal reddit credentials of the author. Instead, credentials_template.py is included as an example. 