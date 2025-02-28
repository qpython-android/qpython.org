jQuery(function($) {
    submenu_init();
});

// 二级目录的点击功能
function submenu_init() {
    // 判断当前屏幕
    jQuery('#example-navbar-collapse li.li-sub').click(function (event) {
        event.stopPropagation(); // 阻止事件冒泡
        let ele = jQuery(this).find('.submenu');

        // 第一次点击需要显示(因为存在兼容性BUG)
        if(!ele.data('click_first')){
            ele.show();
            ele.data('click_first',true)
            return true;
        }

        // 判断显示隐藏
        if (ele.is(':visible')) {
            ele.hide();
        } else {
            ele.show();
        }
    })
}