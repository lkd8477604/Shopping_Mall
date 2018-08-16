#_author:John
#date:2018/8/16 21:18
#softwave: PyCharm
import xadmin
from .models import ShoppingCar, OrderInfo, OrederGoods


class ShoppingCarAdmin(object):
    list_display = ["user", "goods", "goods_num", ]


class OrderInfoAdmin(object):
    list_display = ["user", "order_sn",  "trade_no", "pay_status", "post_script", "order_mount",
                    "order_mount", "pay_time", "add_time"]

    class OrderGoodsInline(object):
        model = OrederGoods
        exclude = ['add_time', ]
        extra = 1
        style = 'tab'

    inlines = [OrderGoodsInline, ]


xadmin.site.register(ShoppingCar, ShoppingCarAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)