def verify_reddit_auth(reddit):
    try:
        me = reddit.user.me()
        print(f"✅ Reddit authentication successful (logged in as: {me or 'Anonymous (read-only)'})")
    except Exception as e:
        print("❌ Reddit authentication failed.")
        raise e
