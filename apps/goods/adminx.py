#_author:John
#date:2018/8/16 21:17
#softwave: PyCharm
import xadmin
from .models import Goods, GoodsCategory, GoodsImage, GoodsCategoryBrand, Banner


class GoodsAdmin(object):
    list_display = ["name", "click_count", "sold_count", "goods_num", "market_price",
                    "goods_price", "goods_desc", "is_new", "is_hot", "add_time"]
    search_fields = ['name', ]
    list_editable = ["is_hot", ]
    list_filter = ["name", "click_count", "sold_count", "goods_num", "market_price",
                   "goods_price", "is_new", "is_hot", "add_time", "category__name"]
    style_fields = {"goods_desc": "ueditor"}

    class GoodsImagesInline(object):
        model = GoodsImage
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [GoodsImagesInline]


class GoodsCategoryAdmin(object):
    list_display = ["name", "category_type", "parent_category", "add_time"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ['name', ]


class GoodsBrandAdmin(object):
    list_display = ["category", "image", "name", "desc"]




class BannerGoodsAdmin(object):
    list_display = ["goods", "image", "index"]



xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(Banner, BannerGoodsAdmin)
xadmin.site.register(GoodsCategoryBrand, GoodsBrandAdmin)