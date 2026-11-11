from flask import Flask, Response, render_template

app = Flask(__name__)

SITE_URL = "https://independencesharedliving.com"


@app.get("/")
def home():
    return render_template("blue.html")


@app.get("/robots.txt")
def robots():
    return Response(
        f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n",
        mimetype="text/plain",
    )


@app.get("/sitemap.xml")
def sitemap():
    pages = ("", "/about", "/housing", "/meals")
    urls = "".join(
        f"<url><loc>{SITE_URL}{page}</loc></url>" for page in pages
    )
    return Response(
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{urls}</urlset>",
        mimetype="application/xml",
    )


@app.get("/about")
def about():
    return render_template("about.html")


@app.get("/housing")
def housing():
    return render_template("housing.html")


@app.get("/meals")
def meals():
    return render_template("meals.html")


@app.get("/alternate")
def alternate():
    return render_template("alternate.html")


@app.get("/blue")
def blue():
    return home()


if __name__ == "__main__":
    app.run(debug=True)
