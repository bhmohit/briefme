from generator import news_controller

def get_video():
    #get news
    news = news_controller.get_news()
    #summarize news
    summarized = news_controller.summarize_news(news)
    #text-to-speech and text-to-video and captions (multithreaded)
    
    #edit videos
    #store videos
    #return link to stored video
    return