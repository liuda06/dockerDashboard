/**
 * Created by king-aric on 16-10-16.
 */

$(function () {
    bind_docker(0);
    $('#sys_nav li').click(function () {
        $('.active').removeClass('active');
        localStorage.setItem('nav', this.getAttribute('index'))
    });
    var index = localStorage.getItem('nav')
    if (index == undefined || index == 'null' || index <= 0 || index > 3) {
        $("#sys_nav").children("li").first().addClass("active");
    } else {
        $("#sys_nav li").each(function () {
            if (this.getAttribute('index') == index) {
                $(this).addClass('active')
                return
            }
        })
    }

    $(".create_container").click(function () {
        $("#image_id").val(this.id)
        $('#create_image').modal({
            keyboard: true
        })
    })
});


//common
function bind_docker(e) {
    if ($("#docker_seleted").val()) {
        writeCookie('docker_server', $("#docker_seleted").val())
        if (e == undefined) {
            window.location.reload()
        }
    }
}

function writeCookie(k, v) {
    var exp = new Date();
    exp.setTime(exp.getTime() + 365 * 24 * 60 * 60 * 1000); //3天过期
    document.cookie = k + "=" + v + ";expires=" + exp.toGMTString() + ";path=/";
}


//images
function create_container(e) {
    $('#create_image').modal('hide')
    if (e && e.getAttribute("create_mode") == 0) {
        $.ajax({
            url: '/containers/create/',
            data: $("#container_form").serialize(),
            type: 'get',
            dataType: 'json',
            success: function (data) {
                if (data.status == 200) {
                    alert(data.msg);
                    window.location.href = data.request
                } else {
                    alert(data.msg)
                }
            },
            error: function (e) {
                console.log(e)
                alert('server error...')
            }
        })
    }
    return create_container_shell()
}

function create_container_shell() {
    $.ajax({
        url: '/containers/shell/',
        data: {
            shell: $("#create_shell").val()
        },
        type: 'post',
        dataType: 'json',
        success: function (data) {
            if (data.status == 200) {
                alert(data.msg);
                window.location.href = data.request
            } else {
                alert(data.msg)
            }
        },
        error: function (e) {
            console.log(e)
            alert('server error...')
        }
    })
}


//docker host
function test_host(url, reload) {
    $.ajax({
        url: url,
        data: $("#docker_host").serialize(),
        type: 'post',
        dataType: 'json',
        success: function (data) {
            if (data.status == 200) {
                alert(data.msg);
                if (reload) {
                    window.location.reload();
                }
            } else {
                alert(data.msg);
            }
        },
        error: function (e) {
            alert("add error...");
            console.log(e);
        }
    })
}
