# Sentiment Analysis from Reddit, X, and YouTube Posts

## Project Overview

This is a console-based Python project that allows users to input multiple links from Reddit, X, or YouTube. The program then analyzes the emotions expressed by users towards the specified posts and displays the results graphically using sentiment analysis.

## Features

- **Multiple Link Input:** Users can provide multiple URLs of posts from Reddit, X, or YouTube.
- **Sentiment Analysis:** Using pre-trained models, the program analyzes the emotions (such as happiness, anger, sadness, etc.) expressed in the comments or reactions to the posts.
- **Language Translation:** Comments or text in different languages are automatically translated before sentiment analysis (using Google Translator).
- **Graphical Representation:** The sentiment results are displayed in a visual format, such as a pie chart or bar graph, using Matplotlib.
  
## Technology Stack

The project uses the following Python libraries and tools:

- `selenium`: For web scraping and automation to extract data from Reddit, X, and YouTube posts.
- `webdriver_manager`: For managing ChromeDriver to run the Selenium browser automation.
- `transformers`: For sentiment analysis using pre-trained models.
- `matplotlib`: For creating graphical representations of the sentiment analysis results.
- `googletrans` & `deep_translator`: For translating text to a standard language (English) for sentiment analysis.

## How It Works

1. **User Input**: The user provides multiple URLs of posts from Reddit, X, or YouTube.
2. **Web Scraping**: The program uses Selenium to access each post and retrieve the relevant data (comments, reactions, etc.).
3. **Translation**: If the content is in a non-English language, it is translated using Google Translator.
4. **Sentiment Analysis**: The content is processed using a pre-trained sentiment analysis model (provided by the `transformers` library).
5. **Graphical Output**: The results of the sentiment analysis are displayed in a chart (e.g., pie chart) using Matplotlib.

## Dependencies

All dependencies required for this project are listed in the `requirements.txt` file. You can install them by running:

```bash
pip install -r requirements.txt
