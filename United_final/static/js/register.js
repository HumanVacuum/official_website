// 关联上验证码登录按钮
function bindCaptchaBtnClick() {
    // 获取一个按钮,jquery自动寻找
    $("#captcha-btn").on("click", function (event) {//鼠标点击触发
        var $this = $(this);
        // 获取邮箱文本
        // 获取邮箱输入框
        var email = $("input[name='email']").val();
        if (!email) {
            alert("请先输入邮箱！");
        }
        // 通过js发送网络请求： ajax。 Async JavaScript And XML(JSON)
        $.ajax({
            url: "/user/captcha",
            method: "POST",
            data: {
                "email": email
            },
            success: function (res) {
                var code = res['code'];
                if (code === 200) {
                    // 取消点击事件
                    $this.off("click");
                    // 开始倒计时
                    var countDown = 60;
                    var timer = setInterval(function () {
                        if (countDown > 0) {
                            $this.text(countDown + "秒后重新发送");
                        } else {
                            $this.text("get captcha");
                            // 重新绑定点击事件
                            bindCaptchaBtnClick();
                            // 清除定时器
                            clearInterval(timer);
                        }
                        countDown -= 1;
                    }, 1000);

                    alert("验证码发送成功！");

                } else {
                    alert(res['message']);
                }
            }
        })
    });
}

// 等网页文档所有元素都加载完成后再执行
$(function () {
    bindCaptchaBtnClick();
});
