#_author:John
#date:2018/8/16 21:15
#softwave: PyCharm
import xadmin
from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    """
    引入更换主题功能
    """
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    """
    页头和页脚
    """
    site_title = "YAO商城后台"
    site_footer = "shopping mall"
    # menu_style = "accordion"如果加上，后台的菜单会变成下拉式


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)