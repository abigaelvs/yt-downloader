from pytube import YouTube


def get_video(url: str) -> str:
    """ Get youtube video from the url that user input
        :param url: youtube url that user input in the form

        :return title: title of the youtube video
        :return author: author or channel of the youtube video
        :return thumbnail_url: thumbnail picture of the video
    """
    yt = YouTube(url)
    return {
        'title': yt.title,
        'author': yt.author,
        'thumbnail_url': yt.thumbnail_url
    }


def get_streams(url: str) -> str:
    """ Get all of the video resolution and give it to user so they can choose resolution to download
        :param url: url that user input on the form
    """
    yt = YouTube(url)
    return [stream for stream in yt.streams if stream.resolution]
    