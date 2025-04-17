# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lCoYXGoVKbR6vqxCGnbk9kYUA7CmZzRL
"""
import streamlit as st
import pandas as pd
from backend_scraper import scrape_urls
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import base64
import io
import plotly.express as px

# Set custom theme
st.set_page_config(
    page_title="Large-Scale Data Scraper",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for background image and text color
background_image_url = "https://images.pexels.com/photos/1103970/pexels-photo-1103970.jpeg?auto=compress&cs=tinysrgb&w=1920&h=1080&dpr=1"

st.markdown(
    """
    <style>
    body {
        background-color: #f9f9f9; /* Light background */
        background-image: none !important; /* Explicitly remove background image */
    }
    .stApp {
        font-family: Arial, sans-serif;
        color: #333333; /* Dark text color */
    }
    table {
        color: inherit; /* Ensure tables inherit the text color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.title("Large-Scale Data Scraper")
st.write("Enter up to 30 URLs to scrape their content and analyze coordination patterns.")

# Input field for URLs
urls_input = st.text_area("Enter URLs (one per line):", height=200)
urls_list = [url.strip() for url in urls_input.split("\n") if url.strip()]

# Button to trigger scraping
if st.button("Scrape URLs"):
    if not urls_list:
        st.error("Please enter at least one URL.")
    elif len(urls_list) > 30:
        st.error("You can only scrape up to 30 URLs at once.")
    else:
        # Display progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Scrape URLs
        scraped_data = scrape_urls(urls_list, progress_bar, status_text)
        
        # Update progress bar
        progress_bar.progress(100)
        status_text.text("Scraping completed!")
        
        # Display results
        if scraped_data:
            df = pd.DataFrame(scraped_data)
            
            # Filter by similarity
            similarity_filter = st.selectbox("Filter by Similarity", ["All", "Similar", "Partially Similar", "Not Similar"])
            if similarity_filter != "All":
                filtered_df = df[df["Similarity"] == similarity_filter]
            else:
                filtered_df = df
            
            st.write("Preview of Scraped Data:")
            st.dataframe(filtered_df)
            
            # Generate interactive word cloud
            def generate_interactive_wordcloud(text):
                from collections import Counter
                wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
                word_freq = wordcloud.words_
                word_freq_df = pd.DataFrame(list(word_freq.items()), columns=["Word", "Frequency"])
                word_freq_df = word_freq_df.sort_values(by="Frequency", ascending=False)
                fig = px.bar(word_freq_df, x="Word", y="Frequency", title="Interactive Word Cloud",
                             labels={"Word": "Words", "Frequency": "Frequency"}, color="Frequency")
                fig.update_traces(marker_color='blue')
                fig.update_layout(xaxis_title="Words", yaxis_title="Frequency")
                return fig
            
            all_content = " ".join([item["Content"] for item in scraped_data])
            wordcloud_fig = generate_interactive_wordcloud(all_content)
            st.plotly_chart(wordcloud_fig)
            
            # Display entities
            # Display entities
            st.write("Extracted Entities (Up to 10 Unique Samples):")
            for item in scraped_data:
                st.write(f"Title: {item['Title']}")  # Use Title instead of URL
                st.table(pd.DataFrame(item["Entities"], columns=["Entity", "Type"]))
            
            
            # Download button for CSV
            csv_buffer = io.StringIO()
            df.to_csv(csv_buffer, index=False)
            csv_buffer.seek(0)
            b64 = base64.b64encode(csv_buffer.getvalue().encode()).decode()
            href = f'<a href="data:text/csv;base64,{b64}" download="scraped_data.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)
        else:
            st.warning("No data was scraped. Possible reasons:")
            st.write("- The URLs may be invalid or inaccessible.")
            st.write("- The pages may use anti-scraping mechanisms.")
            st.write("- Network issues may have occurred during scraping.")
