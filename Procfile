web: sh -c 'MAX_RETRIES=5 RETRY_DELAY=10; for i in $(seq 1 $MAX_RETRIES); do playwright install chromium && break || sleep $RETRY_DELAY; done; streamlit run scraper.py'
