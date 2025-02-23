from flask import Blueprint, render_template, send_from_directory, make_response
import os
import re

main = Blueprint('main', __name__)

def extract_number(filename):
    match = re.search(r'(\d+)', filename)  # Extract number from filename
    return int(match.group(1)) if match else float('inf')  # Ensure correct sorting


@main.route('/')
def home():
    return render_template('index.html')

@main.route('/team')
def team():
    return render_template('players.html')

@main.route('/matches')
def matches():
    return render_template('matches.html')


import os
from flask import render_template, send_from_directory, make_response

@main.route('/gallery')
def gallery():
    gallery_path = os.path.join("app", "static", "images", "gallery")

    # Ensure the gallery folder exists
    if not os.path.exists(gallery_path):
        os.makedirs(gallery_path)

    # Fetch all images in gallery folder dynamically
    image_files = [
        f"images/gallery/{img}"
        for img in sorted(os.listdir(gallery_path), key=extract_number)  # Ensure consistent order
        if img.endswith(('.jpg', '.png', '.jpeg'))
    ]
    print(image_files)

    return render_template('gallery.html', image_files=image_files)

# Serve images without caching
@main.route('/static/images/gallery/<filename>')
def get_gallery_image(filename):
    response = make_response(send_from_directory("static/images/gallery", filename))
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Expires"] = "0"
    response.headers["Pragma"] = "no-cache"
    return response

@main.route('/static/css/<path:filename>')
def static_css(filename):
    response = make_response(send_from_directory(os.path.join("static", "css"), filename))
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Expires"] = "0"
    response.headers["Pragma"] = "no-cache"
    return response


@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/about')
def about():
    return render_template('about.html')
