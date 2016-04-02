var VirtualEntityModule = (function () {

    var entityResult = {};
    var devices = {};

    var loadEntities = function () {



        $('#entity-list').children().remove();

        return $.ajax({
            type: 'GET',
            url: '/api/entity',
            success: function (data) {
                if (data.result.length == 0) {
                    $('#entity-list').append('Entity list is empty');
                    return False;
                }
                else {
                    data.result.forEach(function (entity) {
                        $('#entity-list').append('<a href="#" class="list-group-item entity-name" data-id="' + entity.id + '">' + entity.name + '</a>');
                        entityResult = data.result;
                    });
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                Utils.alertShow('Error loading resources.');
            },
            complete: function (jqXHR, textStatus) {
            }
        });
    };

    var loadDevices = function () {
        $.ajax({
            type: 'GET',
            url: '/api/device',
            success: function (data) {
                if (data.result.length == 0) {
                    $('#device-list').append('Device list is empty');
                    return False;
                } else {
                    data.result.forEach(function (device) {
                        $('#devices-list').append('<a href="#" class="ui-widget-content list-group-item device-name" data-id="' + device.id + '">' + device.name + '</a>');
                    });
                    $('#devices-list').selectable();
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                Utils.alertShow('Error loading resources.');
                $('#device-list').append('Device list is empty')
            }
        });
    };

    var loadEntityDetail = function (e) {

        var id = null;

        if (e != null) {
            id = $(this).data('id');
        } else {
            id = $('#entity-id').val();
        }


        $('#properties-table tbody').children().remove();

        // find right entity in entityResult
        var entity = null
        entityResult.forEach(function (entity_tmp) {
            if (entity_tmp.id == id) {
                entity = entity_tmp;
            }
        });

        if (entity) {
            $('#entity-id').val(entity.id);
            $('#entity-name').text(entity.name);
            $('#entity-name').data('pk', entity.id);
            $('#entity-description').text(entity.description);
            $('#entity-description').data('pk', entity.id);
            $('#entity-domain').text(entity.domain_id);

            if ((entity.properties.length) == 0) {

                $('#properties-table  > tbody').append('<tr><td colspan="5">This entity has no properties click <a class="new-property" href = "#" style="border-bottom:dashed 1px #0088cc"> here </a> to add some.</td></tr>');
            }
            else {
                entity.properties.forEach(function (property) {
                    $('#properties-table  > tbody').append('<tr>' +
                        '<td></td>' +
                        '<td><a href = "#" class="editable property-name" id="property-name" data-device ="' + property.device.id + '" data-type="text" data-pk="' + property.id + '" data-url="/api/property" data-title = "Enter property name">' + property.name + '</a></td>' +
                        '<td class="topic">'+property.device.topic+'</td>' +
                        '<td><a href="#" class="subscribe">Subscribe</a></td>' +
                        '<td class="action-result"></td>' +
                        '</tr>');
                });
                $('#properties-table  > tbody').append('<tr><td colspan="5">Click <a class="new-property" href = "#" style="border-bottom:dashed 1px #0088cc"> here </a> to manage properties.</td></tr>');

            }

            $('#btn-edit').attr('disabled', false);
            $('#btn-delete').attr('disabled', false);
            bindEditable();


            $('.detail-content').hide();
            $('#entity-detail').show();
        } else {
            $('.detail-content').hide();
            $('#entity-placeholder').show();
        }
    };

    var bindEditable = function () {
        $('#btn-edit').text("Enable editing entity");

        $('.editable').editable({
            ajaxOptions: {contentType: 'application/json', dataType: 'json', type: 'PUT'},
            params: function (params) {
                params.source = "inline";
                return JSON.stringify(params);
            },
            success: function (response, newValue) {
                loadEntities();
            },
            error: function (response) {
                return "Error occured"
            }
        });

        $('.editable').editable('option', 'disabled', true);
        $('.new-property').on('click', btnAddPropertiesClick);
        $('.subscribe').on('click',btnSubscribeClick);
    };

    var btnAddPropertiesClick = function (e) {
        e.preventDefault();

        var $devices = $('.device-name');
        $devices.removeClass('ui-selected');

        var ids = [];

        $('.property-name').each(function () {
            var deviceId = $(this).data('device');
            var propertyId = $(this).data('pk');
            ids.push({
            deviceId : deviceId,
            propertyId : propertyId});
        });

        $devices.each(function () {
            var $device = $(this);

            ids.forEach(function(d){
                if ($device.data('id') == d.deviceId) {
                    $device.attr('data-property', d.propertyId);
                    $device.addClass('ui-selected');

                }
            });
        });

        $('#edit-modal').modal();
    };

    var btnEditOkClick = function (e) {
        e.preventDefault();


        properties = [];
        var deviceIds = [];
        var entityId = $('#entity-id').val();

        $('.device-name.ui-selected').each(function () {
            var name = $(this).text();
            var deviceId = $(this).data('id');
            var propertyId = $(this).data('property');
            properties.push({
                id: propertyId,
                name : name,
                device_id : deviceId
            });
            deviceIds.push($(this).data('id'));
        });

        $.ajax({
            type: 'POST',
            url: '/api/property',
            data: JSON.stringify({
                entity_id : entityId,
                properties: properties,
            }),
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            success: function (data) {
                Utils.successShow('Properties edited.');
                $.when(
                    loadEntities()
                ).then(function(){
                    loadEntityDetail()
                });

            },
            error: function () {
                Utils.alertShow('Error editing properties.');
            },
            complete: function () {
            }
        });


        $('#edit-modal').modal('hide');
    };

    var toggleEditClick = function (e) {
        e.preventDefault();
        e.stopPropagation();


        var text = $('#btn-edit').text();
        $('#btn-edit').text(
            text == "Disable editing entity" ? "Enable editing entity" : "Disable editing entity");

        $('.editable').editable('toggleDisabled');
    };

    var btnDeleteClick = function (e) {
        e.preventDefault();

        $('#delete-entity-id').val($('#entity-id').val());
        $('#delete-entity-name').val($('#entity-name').text());

        $('#confirm-delete').modal();

    };

    var btnDeleteConfirmClick = function (e) {

        var id = $('#delete-entity-id').val();

        return $.ajax({
            type: 'DELETE',
            url: '/api/entity/' + id,
            success: function (data) {
                $('#confirm-delete').modal('hide');
                Utils.successShow('Entity deleted.');
                loadEntities();
                $('.detail-content').hide();
                $('#entity-placeholder').show();
                $('#btn-edit').attr('disabled', true);
                $('#btn-delete').attr('disabled', true);


            },
            error: function (jqXHR, textStatus, errorThrown) {
                Utils.alertDeleteModalShow('Error deleting entity.');
            },
            complete: function (jqXHR, textStatus) {
            }
        });
    };
    var clearNewEntity = function () {
        $('#new-entity-name').val('');
        $('#new-entity-description').val('');
    };

    var btnNewClick = function (e) {
        e.preventDefault();

        clearNewEntity();
        $('.detail-content').hide();
        $('#btn-edit').attr('disabled', true);
        $('#btn-delete').attr('disabled', true);
        $('#new-entity').show();
    };

    var btnSaveClick = function (e) {
        e.preventDefault();

        var name = $('#new-entity-name').val();
        var description = $('#new-entity-description').val();


        $.ajax({
            type: 'POST',
            url: '/api/entity',
            data: JSON.stringify({
                name: name,
                domain_id: "46760446-cd02-11e5-89ba-22000b79ceab",
                description: description
            }),
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            success: function (data) {
                Utils.successShow('Entity created.');
                loadEntities();
            },
            error: function () {
                Utils.alertShow('Error creating entity.');
            },
            complete: function () {
                // clearEditModal();
            }
        });

    };

    var toggleDetail = function (element) {

        var $detail = element.parent('.detail-content');

        $detail.show();

        $('div.action').not($detail).each(function () {
            var $other = $(this);
            $other.hide();
        })
    };

    var btnSubscribeClick = function(){
        // Create a client instance
	    client = new Paho.MQTT.Client("iot.eclipse.org", 80, "wadaw");

	    // set callback handlers
        client.onConnectionLost = onConnectionLost;
        client.onMessageArrived = onMessageArrived;

        // connect the client
        client.connect({onSuccess:onConnect});
    }

    // called when the client connects
    function onConnect() {
        // Once a connection has been made, make a subscription and send a message.
         console.log("onConnect");
        client.subscribe("iot/raspberry/temperature");

    }

    // called when the client loses its connection
    function onConnectionLost(responseObject) {
      if (responseObject.errorCode !== 0) {
        console.log("onConnectionLost:"+responseObject.errorMessage);
      }

    }

    // called when a message arrives
    function onMessageArrived(message) {
        $rows = $('#properties-table tbody > tr');


        $rows.each(function(){
            $row = $(this)
            if ($row.children('td.topic').text() == message.destinationName){
                $row.children('td.action-result').html(message.payloadString)
            }
        })
    }

    return {

        /**
         * Initializes module.
         */
        initialize: function () {
            $('#btn-edit').attr('disabled', true);
            $('#btn-delete').attr('disabled', true);
            $('.detail-content').hide();
            $('#entity-placeholder').show();
            loadEntities();
            loadDevices();

            $('#entity-list').on('click', '.entity-name', loadEntityDetail);
            $('#btn-edit').on('click', toggleEditClick);
            $('#btn-delete').on('click', btnDeleteClick);
            $('#btn-delete-confirm').on('click', btnDeleteConfirmClick);
            $('#btn-new').on('click', btnNewClick);
            $('#save-entity').on('click', btnSaveClick);
            $('#btn-edit-ok').on('click', btnEditOkClick);


        }
    };

})();


require(['jquery', 'bootstrap', 'editable', 'jqueryui','mqtt', 'utils'], VirtualEntityModule.initialize);