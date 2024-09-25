import tweepy

# Postavi svoj Bearer Token koji si dobio sa Twitter Developer Portala
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAMUjvwEAAAAAX9biAspmf8axgvZgnL2mniFgEV0%3DgWnx0ev4Hf21RzrVc5hJddZesvgGsq7dTlpr2RIKkTomhY03cC'

# Autentifikacija na Twitter API v2 pomoću Bearer Token-a
client = tweepy.Client(bearer_token=bearer_token)

# ID tweeta za koji želiš uzeti komentare (replike)
tweet_id = '1833384155708854429'  # Samo ID tweeta, bez URL-a

# Funkcija za dohvat odgovora na određeni tweet
def get_replies(tweet_id, count=10):
    # Pretraga odgovora (replika) na tweet koristeći v2 API
    query = f'conversation_id:{tweet_id}'
    
    # Tražimo odgovore koristeći tweepy.Client i v2 API
    replies = client.search_recent_tweets(query=query, max_results=count, tweet_fields=['author_id', 'conversation_id', 'text'])
    
    return [reply.text for reply in replies.data] if replies.data else []

# Prikaz komentara
komentari = get_replies(tweet_id, 10)
for i, komentar in enumerate(komentari):
    print(f'{i + 1}: {komentar}')
