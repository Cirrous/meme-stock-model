# A Tesla Stock Prediction Model

A machine learning model that predicts Tesla (TSLA) stock price movements based on sentiment analysis from Reddit posts. The model combines Reddit sentiment data with current stock prices using a PyTorch LSTM network to predict whether Tesla stock will rise ("steigt") or fall ("fällt").

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