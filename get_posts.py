import fb_posts
import fb_pages

def submit_request(group_id):
    with open('app.txt', 'r') as f:
        first_line = f.readline().strip("/n")
        second_line = f.readline()
    app_id = "238791666290359"
    app_secret = second_line  # Get from file
    page_id = "319872211700098"
    access_token = app_id + "|" + app_secret
