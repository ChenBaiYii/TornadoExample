$(document).ready(function () {
    document.session = $('#session').val();
    console.log("loading jquery success!");
    setTimeout(requestInventory, 100);

    $('#add-button').click(function (event) {
        console.log("发送点击请求");
        jQuery.ajax({
            url: '//localhost:8080/cart',
            type: 'POST',
            data: {
                session: document.session,
                action: 'add'
            },
            dataType: 'json',
            beforeSend: function (xhr, settings) {
                $(event.target).attr('disabled', 'disabled');
                console.log("before over!");
            },
            success: function (data, status, xhr) {
                console.log("hide start");
                $('#add-to-cart').hide();
                $('#remove-from-cart').show();
                $(event.target).removeAttr('disabled');
                console.log("hide function over!")
            }
        });
    });

    $('#remove-button').click(function (event) {
        jQuery.ajax({
            url: '//localhost:8080/cart',
            type: 'POST',
            data: {
                session: document.session,
                action: 'remove'
            },
            dataType: 'json',
            beforeSend: function (xhr, settings) {
                $(event.target).attr('disabled', 'disabled');
            },
            success: function (data, status, xhr) {
                $('#remove-from-cart').hide();
                $('#add-to-cart').show();
                $(event.target).removeAttr('disabled');
            }
        });
    });
});

function requestInventory() {
    console.log("default request ok!");
    jQuery.getJSON('//localhost:8080/cart/status', {session: document.session},
        // jQuery.getJSON('//localhost:8000/cart/status',
        function (data, status, xhr) {
            $('#count').html(data['inventoryCount']);
            setTimeout(requestInventory, 0);
        }
    );
}