var DomainModule = (function(){

    var loadDomains = function(){

        return $.ajax({
            type: 'GET',
            url: '/api/domain',
            success: function (data) {
                var result = data.result;
                renderDomains(result);

                $("#domain-parentId").append($("<option>",{value:"", text:""}));
                for (var i = 0, len = result.length; i < len; i++) {
                    $("#domain-parentId").append($("<option>",{value:result[i].id, text:result[i].name}));
                }
                $("#domain-parentId").trigger("chosen:updated");
            },
            error: function (jqXHR, textStatus, errorThrown) {
                Utils.alertShow('Error loading domains.');
            },
            complete: function (jqXHR, textStatus) {

            }
        });

    }

    var renderDomains = function(domains) {

        var domainsData = readDomains(domains);

        var createSubtree = function(index) {
            var subtree = new Array();

            for (var i = 0; i < domainsData[index].length; i++) {
                if(domainsData[index]) {
                    var nodes = new Array();

                    if(domainsData[domainsData[index][i].id]) {
                        nodes = createSubtree(domainsData[index][i].id);
                    }

                    if(nodes.length==0) {
                        subtree.push(
                            {
                                text: domainsData[index][i].name,
                                id: domainsData[index][i].id,
                                folderParentId: domainsData[index][i].parentId,
                            }
                        );
                    }
                    else {
                        subtree.push(
                            {
                                text: domainsData[index][i].name,
                                id: domainsData[index][i].id,
                                folderParentId: domainsData[index][i].parentId,
                                nodes: nodes
                            }
                        );
                    }
                }
            }
            return subtree;
        };


        var data = createSubtree(null);

        $('#treeview1').treeview({
            data: data,
            levels: 2,
            onNodeSelected: function(event, domain) {
                selectedDomain = domain;
                $('#btn-edit').prop('disabled', false);
                loadEntities(domain.id);
            },
            onNodeUnselected: function(event, domain) {
                $('#btn-edit').prop('disabled', true);
            }
        });
    };

    var readDomains = function(domains) {
        var domainsData = {};

        for (var i = 0; i < domains.length; i++) {
            var f = domains[i];

            if(f.parent_id==undefined) {
                f.parent_Id = null;
            }

            if(!domainsData[f.parent_id]) {
                domainsData[f.parent_id] = new Array();
            }

            domainsData[f.parent_id].push(
                {
                    name: f.name,
                    id: f.id,
                    parentId: f.parent_id
                });
        }

        return domainsData;
    };

    var loadEntities = function(domainId){

        var dt = $('#table-entities').DataTable();
        dt.clear();

        return $.ajax({
            type: 'GET',
            url: '/api/domain/'+ domainId,
            success: function (data) {
                dt.rows.add(data.result.entities).order(1, 'asc').draw();
                $('[data-toggle="popover"]').popover({
                    delay: { show: 500, hide: 5000 }
                });
                rebindHandlers();
            },
            error: function (jqXHR, textStatus, errorThrown) {
                Utils.alertShow('Error loading entities.');
            },
            complete: function (jqXHR, textStatus) {
            }
        });
    };

    var btnNewClick = function (e) {
        e.preventDefault();
        clearModal();

        $('#edit-modal').modal();
    }

    var clearModal = function() {

        $('#domain-id').val("");
        $('#domain-name').val("");
        $('#domain-parentId').val("").trigger('chosen:updated');
    }
    var btnEditClick = function(e) {
        e.preventDefault();
        clearModal();

        var domain = $('#treeview1').treeview('getSelected')[0];

        $('#domain-id').val(domain.id);
        $('#domain-name').val(domain.text);
        $('#domain-parentId').val(domain.folderParentId).trigger('chosen:updated');

        $('#edit-modal').modal();
    };

    var btnEditOkConfirmed = function(e){
        e.preventDefault();

        var id = $('#domain-id').val();
        var name = $('#domain-name').val();
        var parent = $('#domain-parentId').val();

        $.ajax({
                type: 'POST',
                url: '/api/domain',
                data: JSON.stringify({
                    id: id,
                    name: name,
                    parent_id: parent
                }),
                contentType: 'application/json; charset=utf-8',
                dataType: 'json',
                success: function (data) {
                    $('#edit-modal').modal('hide');
                    Utils.successShow('Domain updated.');
                    loadDomains();

                },
                error: function () {
                    Utils.alertEditModalShow('Error updating domain.');
                },
                complete: function () {
                }
            });
    }

    var rebindHandlers = function(){
        $('#table-entities tbody tr').on('click','tr', function () {
                $(this).toggleClass( 'row_selected' );
            });

        $('#table-entities tbody tr').draggable({
            containment: ".row",
            scroll: false,
            revert : function(event, ui) {
            $(this).data("ui-draggable").originalPosition = {
                top : 0,
                left : 0
            };
            return !event;
            }

        });

        $( ".node-treeview1" ).droppable({
                drop: function(event, ui){


                    var draggable = ui.draggable;
                    var node_id = $(this).data('nodeid');

                    var node = $('#treeview1').treeview('getNode', node_id);

                    var domain_id = node.id;
                    var entity_id = draggable.find('span.id-info-tag').data('content');
                    var old_id = draggable.find('span.id-info-tag').data('parent');

                    $.ajax({
                        type: 'POST',
                        url: '/api/domain',
                        data: JSON.stringify({
                            method: "change_entity_domain",
                            entity_id: entity_id,
                            domain_id: domain_id
                        }),
                        contentType: 'application/json; charset=utf-8',
                        dataType: 'json',
                        success: function (data) {
                            Utils.successShow('Entity domain changed.');
                            loadEntities(old_id);
                        },
                        error: function () {
                            Utils.alertShow('Error changing entity domain.');
                        },
                        complete: function () {
                        }
                    });

                },
                hoverClass: 'dropdown-hover',
                greedy: true,
                tolerance: "pointer"
        });
    }

    var columns = [
        {
            'title': '',
            'data': 'id',
            'orderable': false,
            'width': '1%',
            'defaultContent': '',
            'render' : function (data, type, row, meta) {
                return '<span class="glyphicon glyphicon-transfer id-info-tag" title="Virtual Entity ID" data-toggle="popover" data-parent="'+row.domain_id+'" data-content="' + row.id + '" data-trigger="click"></span>';
            }
        },
        {
           'title': 'Name',
            'data': 'name',
            'width': '39%',
            'defaultContent': ''
        },
        {
            'title': 'Description',
            'data': 'description',
            'width': '60%',
            'defaultContent': ''
        }
    ]

    return {

        /**
         * Initializes module.
         */
        initialize: function() {

            var table = $('#table-entities').DataTable({
                'columns': columns,
                'dom': '<"row"<"col-md-8"i><"col-md-4"f>>rt<"row"<"col-md-9"l><"col-md-3"p>>',
                 'tableTools': {
                    'aButtons' : []
                },
                'bLengthChange': false
            });


            loadDomains();

            $('select').chosen();

            $('#btn-edit').prop('disabled', true);

            $('#btn-new').on('click', btnNewClick);
            $('#btn-edit').on('click', btnEditClick);
            $('#btn-edit-ok').on('click',btnEditOkConfirmed);

        }
    };
})();



require(['jquery', 'bootstrap','jqueryui','treeview','datatables','datatablesBootstrap','datatablesTableTools','chosen','utils'], DomainModule.initialize);