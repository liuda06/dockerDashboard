/**
 * Created by king-aric on 16-10-16.
 */

//images
$(function () {
    $(".create_container").click(function () {
        $("#image_id").val(this.id)
        $('#create_image').modal({
            keyboard: true
        })
    })
});
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
                    window.location.href = data.request
                }
            }
        },
        error: function (e) {
            alert(e)
        }
    })
}