# A Tesla Stock Prediction Model

A machine learning model that predicts Tesla (TSLA) stock price movements based on sentiment analysis from Reddit posts. The model combines Reddit sentiment data with current stock prices using a PyTorch LSTM network to predict whether Tesla stock will rise ("steigt") or fall ("fällt").

Since the Reddit API (PRAW) doesen't let you access historical data, we used historical data provided by a very helpful person on reddit, who extracted all historical data from the top 40.000 subreddits. (https://www.reddit.com/r/pushshift/comments/1itme1k/separate_dump_files_for_the_top_40k_subreddits/)
In this project, we only focused on r/wallstreetbets, because it it the biggest financial subreddit.

This project leverages natural language processing and deep learning to forecast Tesla stock movements by:
- Reddit Data Collection: Preprocessing Tesla-related posts from Reddit communities
- Sentiment Analysis: Processing text data using two different models finetuned for financial texts (finBERT) and social media texts (VADER)
- Embedding: Vectorizing the preprocessed texts with the help of HTW's "KI Werkstatt" and the provided API
- Stock Price Integration: Combining sentiment with historical Tesla stock data
- Multiple ML Models: LSTM, RNN, and TF-IDF based prediction models
- Performance Comparison: Comprehensive evaluation of different approaches

## Data Pipeline

Reddit Posts → Text Preprocessing (different for sentiment and embedding) → Sentiment, Embeddings → Combined sentiment scores, normalized upvotes with embeddings/vectors → Weekly Aggregation 
→ Model Training in combination with the stock data

## Model Variants
- LSTM with Embeddings: Deep learning model using word embeddings, sentiments and upvotes
- LSTM with TF-IDF: Traditional NLP approach with LSTM architecture  
- skforecast Integration: Simple time series forecasting framework

## Description of files to help you navigate:

- Root directory: All used notebooks for every single step of data filtering, preprocessing, analyzing and for every neccessary step to get to the model.
- Models: All trained models. "best_model" ist the main model outcome from the LSTM model trained with every available information.
The other model files are coming from different models with small differences, or completely different models (as their names suggest)
- Data: This folder ist almost empty. The only file on this GitHub Repository is the scraped file with the Tesla stock prices. 
The original Reddit data, as well as several other files including the preprocessed and embedded files are in this Google Drive folder: https://drive.google.com/drive/folders/1QtpAQiFK9998gK8mbqNLh-O0zf8ZVEI5
We kept the files there to prevent exeeding the limit of Github storage and problems with pushing.


## Setup

To run the project:

1. Create a venv by running `python -m venv venv`

2. Activate (`source venv/bin/activate` on WSL/Linux) the virtual environment.
	
	On Windows activate the environment with PowerShell:
	```powershell
	.\venv\Scripts\Activate.ps1
	```
	or on Windows with Command Prompt:
	```cmd
	.\venv\Scripts\activate.bat
	```

3. Install all requirements (`pip install -r requirements.txt`).

4. Create a `.env` file in the root directory with your Reddit API credentials:
	```
	REDDIT_CLIENT_ID=your_client_id
	REDDIT_CLIENT_SECRET=your_client_secret
	REDDIT_USER_AGENT=your_user_agent
	```

## Running the Prediction
 
 Within the venv run:

```bash
python output/run_prediction.py
```
This will:
- Execute the prediction notebook (`predict_tesla.ipynb`)
- Generate predictions based on current Tesla Reddit posts
- Save results to `data/latest_prediction.json`
- Start a local HTTP server on port 8000
- Automatically open the dashboard in your browser at `http://localhost:8000/output/tesla_dashboard.html`