from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime
from sqlalchemy.orm import relationship

from blog.models.database import db
from blog.models.tag import article_tag_associations_table


class Article(db.Model):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    title = Column(String(255))
    text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship("Author", back_populates="article")
    tags = relationship("Tag", secondary=article_tag_associations_table, back_populates="article")

    def __str__(self):
        return self.tags.name
