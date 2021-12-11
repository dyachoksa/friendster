from app import app, welcome_message


@app.route("/")
def index():
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Friendster</title>
</head>
<body>
    <h1>{welcome_message}</h1>
</body>
</html>
"""


@app.route("/about")
def about():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Friendster</title>
</head>
<body>
    <h1>About page</h1>
</body>
</html>
"""
