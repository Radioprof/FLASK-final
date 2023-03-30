from flask import Blueprint, redirect, url_for
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from blog.models import tag, article, user, author
from blog.models.database import db

admin_app = Blueprint('admin_app', __name__, url_prefix='/admin')


class CustomAdminView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth_app.login'))


class CustomAdminIndexView(AdminIndexView):
    """
    ограничивает доступ к
    странице администрирования пользователей,
    не имеющих атрибута staff
    """

    @expose()
    def index(self):
        if not (current_user.is_authenticated and current_user.is_staff):
            return redirect(url_for('auth_app.login'))
        return super().index()


class ArticleAdminView(CustomAdminView):
    # column_list = ('title', 'author', 'text', 'tags')
    column_searchable_list = ('title', )
    ignore_hidden = False


admin = Admin(
    name='Blog Admin Panel',
    index_view=CustomAdminIndexView(),
    template_mode='bootstrap4',
)
admin.add_view(CustomAdminView(tag.Tag, db.session, category='Models'))
admin.add_view(ArticleAdminView(article.Article, db.session, category='Models'))
admin.add_view(CustomAdminView(user.User, db.session, category='Models'))
admin.add_view(CustomAdminView(author.Author, db.session, category='Models'))
