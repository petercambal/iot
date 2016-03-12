var ProxyModule = (function(){

    var proxyResult = {}

    var loadProxies = function() {



        return $.ajax({
            type: 'GET',
            url: '/api/proxy',
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            success: function (data) {
                //  <a href="#" class="list-group-item">First item <span class="badge">12</span></a>
                $('#proxy-list').children().remove();
                if (data.result.length == 0 ){
                    $('#proxy-list').append('Proxy list is empty')
                    return False
                }
                data.result.forEach(function(proxy){
                    $('#proxy-list').append('<a href="#" class="list-group-item proxy-name" data-id="'+proxy.id+'">'+proxy.name+' <span class="badge">'+proxy.devices.length+'</span></a>');
                });

                proxyResult = data.result


            },
            error: function (jqXHR, textStatus, errorThrown) {
                Utils.alertShow('Error loading resources.');
            },
            complete: function (jqXHR, textStatus) {
            }
        });


    };

    var loadProxyDetail = function() {
        id = $(this).data('id');
        $('#devices-table tbody').children().remove();

        // load devices for proxy
        var proxy;
        proxyResult.forEach(function(proxy_tmp){
            if (proxy_tmp.id == id) {
                proxy = proxy_tmp;
            }
        });

        if (proxy){
            $('#proxy-id').val(proxy.id);
            $('#proxy-name').val(proxy.name);
            $('#proxy-description').val(proxy.description);
            $('#proxy-ip-address').val(proxy.ip_address);
            $('#proxy-mac-address').val(proxy.mac_address);
            $('#proxy-last-connected').val(proxy.last_connected);
            $('#proxy-model').val(proxy.model);
            $('#proxy-os').val(proxy.os);

            proxy.devices.forEach(function(device){
                var timedeltaMinutes = createDatetime(device.last_connected);
                var statusText = "";
                var fillColor = "";
                if (timedeltaMinutes > 10) {
                    statusText = "Disconnected";
                    fillColor = "red";
                } else if(timedeltaMinutes > 5) {
                    statusText = "Idle";
                    fillColor = "orange";
                } else {
                    statusText = "Connected";
                    fillColor = "green";
                }

                var statusMarker = ' <span class="id-info-tag" title="Status: '+statusText+' " data-toggle="popover" data-trigger="click" data-content="Last connected: ' + device.last_connected + '"> \
                                        <svg height="20" width="20" style="cursor:pointer"> \
                                            <circle cx="10" cy="10" r="9" stroke-width="0" fill="'+fillColor+'" /> \
                                        </svg> \
                                    </span>';

               $('#devices-table').append('<tr> \
                                                <td>'+statusMarker+'</td>\
                                                <td data-id="'+device.id+'"><a class="editable" id="name" data-type="text" data-pk="'+device.id+'" data-url="/api/device" data-title = "Enter device name">'+device.name+'</a></td>\
                                                <td>'+device.last_connected+'</td>\
                                                <td>Action</td>\
                                            </tr>');

                $('[data-toggle="popover"]').popover({
                    delay: { show: 100, hide: 100 }
                });
            });

            bindEditable();
            $('#proxy-detail').show();
        }
        else return False

    }

    var bindEditable = function(){
        $('.editable').editable({
            ajaxOptions: {contentType: 'application/json', dataType: 'json' },
            params: function(params) { return JSON.stringify(params); }
        });
    };

    var createDatetime = function(datetime_string) {
        var now = new Date();
        var last_connected = new Date(datetime_string.substring(0,4)+"-"+datetime_string.substring(5,7)+"-"+datetime_string.substring(8,10)+"T"+datetime_string.substring(11,16)+":00Z")

        var delta_time = now - last_connected;
        timedeltaMinutes = delta_time/1000/60;
        return timedeltaMinutes
    }

    var btnSaveProxyClick = function(e){
        e.preventDefault();

        var proxy_id = $('#proxy-id').val();
        var name = $('#proxy-name').val();
        var description = $('#proxy-description').val();
        var ipAddress = $("#proxy-ip-address").val();
        var macAddress = $('#proxy-mac-address').val();
        var model = $('#proxy-model').val();
        var os = $('#proxy-os').val();

        devices = [];
        $('#devices-table > tbody > tr').each(function(row){

            td = $(this).find('td#name')
            var name =  td.html()
            var device_id = td.data('id')
            device = {
                'id' : device_id,
                'name' : name,
                'proxy_id' : proxy_id
            }

            devices.push(device);
        });

        $.ajax({
                type: 'PUT',
                url: '/api/proxy',
                data: JSON.stringify({
                    id: proxy_id,
                    name: name,
                    description: description,
                    ip_address: ipAddress,
                    mac_address : macAddress,
                    model : model,
                    os : os,
                    devices : devices
                }),
                contentType: 'application/json; charset=utf-8',
                dataType: 'json',
                success: function (data) {
                    Utils.successShow('Proxy edited.');
                    loadProxies();
                },
                error: function () {
                    Utils.alertShow('Error updating proxy.');
                },
                complete: function () {
                   // clearEditModal();
                }
            });
    }


    var btnDeleteProxyClick = function(e){
         e.preventDefault();

         $('#delete-proxy-id').val($('#proxy-id').val());
         $('#delete-proxy-name').val($('#proxy-name').val());

        $('#confirm-delete').modal();
    }

    var btnDeleteProxyConfirmClick = function(e){
        e.preventDefault();
        proxyId = $('#delete-proxy-id').val();

        return $.ajax({
            type: 'DELETE',
            url: '/api/proxy/' + proxyId,
            success: function (data) {
                $('#confirm-delete').modal('hide');
                Utils.successShow('Proxy deleted.');
                loadProxies();

            },
            error: function (jqXHR, textStatus, errorThrown) {
                Utils.alertDeleteModalShow('Error deleting proxy.');
            },
            complete: function (jqXHR, textStatus) {
            }
        });


    }

    return {

        /**
         * Initializes module.
         */
        initialize: function() {

            $.fn.editable.defaults.ajaxOptions = {contentType: 'application/json', dataType: 'json'};

            $('#proxy-detail').hide();
            loadProxies();

            $('#proxy-list').on('click','.proxy-name',loadProxyDetail);
            $('#proxy-detail').on('click','#save-proxy',btnSaveProxyClick);
            $('#proxy-detail').on('click','#delete-proxy',btnDeleteProxyClick);
            $('#btn-delete-confirm').on('click',btnDeleteProxyConfirmClick);



        }
    };

})();


require(['jquery', 'bootstrap','editable','utils'], ProxyModule.initialize);