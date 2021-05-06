from flask import Blueprint, render_template, url_for, request, redirect, make_response

from .utils import get_video, get_streams

views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        if url:
            data = get_video(url)
            streams = get_streams(url)
            context = {
                'title': data['title'],
                'author': data['author'],
                'thumbnail_url': data['thumbnail_url'],
                'streams': streams,
                'url': url,
            }
        else:
            return redirect('/')
    else:
        context = {}
    return render_template('index.html', **context)