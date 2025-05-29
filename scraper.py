import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
import io

# Default usernames
default_usernames = [
    "elusive001", "botragelad", "holiness2100", "uprightness100", "truthU87",
    "biodun556", "coronaVirusPro", "NigerianXXX", "Kingsnairaland", "Betscoreodds",
    "Nancy2020", "Nancy1986", "Writernig", "WritterNg", "WriiterNg", "WrriterNg",
    "WriteerNig", "WriterrNig", "WritterNig", "WriiterNig", "WrriterNig", "WriterNigg",
    "WriterNiiig", "WriterNiig", "Ken6488", "Dalil8", "Slavaukraini", "Redscorpion", "Nigeriazoo"
]

# Function to scrape posts
def scrape_nairaland(usernames, pages=1):
    headers = {
        'User -Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    results = []
    
    for username in usernames:
        for page in range(1, pages + 1):
            url = f"https://www.nairaland.com/{username}/posts/{page}"
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                posts = soup.find_all('div', class_='post')  # Adjust the class based on actual HTML structure
                
                for post in posts:
                    topic = post.find('a', class_='topic-title').text.strip()
                    topic_url = post.find('a', class_='topic-title')['href']
                    post_content = post.find('div', class_='post-content').text.strip()
                    likes = post.find('span', class_='likes-count').text.strip()  # Adjust based on actual HTML structure
                    shares = post.find('span', class_='shares-count').text.strip()  # Adjust based on actual HTML structure
                    
                    results.append({
                        'username': username,
                        'topic': topic,
                        'topic_url': topic_url,
                        'post_content': post_content,
                        'likes': likes,
                        'shares': shares
                    })
            else:
                st.warning(f"Failed to retrieve posts for {username} on page {page}")

    return results

# Streamlit app layout
st.title("Nairaland Post Scraper")

# User input for usernames
usernames_input = st.text_input("Enter up to 10 usernames separated by commas (or leave blank to use default):")
if usernames_input:
    usernames = [name.strip() for name in usernames_input.split(',')][:10]
else:
    usernames = default_usernames

# User input for number of pages
pages = st.number_input("Number of pages to scrape:", min_value=1, max_value=10, value=1)

# Button to trigger scraping
if st.button("Scrape Posts"):
    with st.spinner("Scraping posts..."):
        posts_data = scrape_nairaland(usernames, pages)
    
    # Display results
    if posts_data:
        df = pd.DataFrame(posts_data)
        for post in posts_data:
            st.subheader(f"Post by {post['username']}")
            st.markdown(f"**Topic:** [{post['topic']}]({post['topic_url']})")
            st.markdown(f"**Content:** {post['post_content']}")
            st.markdown(f"**Likes:** {post['likes']} | **Shares:** {post['shares']}")
            st.markdown("---")
        
        # CSV download
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='nairaland_posts.csv',
            mime='text/csv',
        )
    else:
        st.info("No posts found for the given usernames.")
