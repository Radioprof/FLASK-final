from blog.app import app
from blog.models.database import db


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
    )


@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    flask create-tags
    > done! created tags: <flask> <django> <python> <gb> <sqlite>
    """
    from blog.models import Tag

    tags = ('flask', 'django', 'python', 'gb', 'sqlite')
    for item in tags:
        db.session.add(Tag(name=item))
    db.session.commit()
    print(f"done! created tags: {', '.join(tags)}")
