%rebase('./base.tpl',title='Admin Page | Entities')

%include  partial/admin/nav user=user


%include partial/admin/sidebar
<!-- Page Content -->

<div class="alert alert-danger collapse" role="alert" id="alert-msg">
    <button type="button" class="close" aria-label="Close" onclick="$('#alert-msg').hide()"><span
            aria-hidden="true">&times;</span></button>
    <div id="alert-msg-text"></div>
</div>

<div class="alert alert-success collapse" role="alert" id="success-msg">
    <button type="button" class="close" aria-label="Close" onclick="$('#success-msg').hide()"><span
            aria-hidden="true">&times;</span></button>
    <div id="success-msg-text"></div>
</div>

<div id="page-content-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1>Virtual Entities</h1>
                <div class="container-fluid">
                    <div class="row">
                        <div class="col-lg-3">
                            <div class="panel panel-default">
                                <div class="panel-heading">
                                    Virtual Entities
                                    <div class="pull-right">
                                        <button type="button" class="btn btn-default btn-xs" id="btn-new">New entity
                                        </button>
                                    </div>
                                </div>
                                <div class="panel-body" style="padding:0">
                                    <div id="entity-list" class="list-group" style="margin-bottom:0">
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-9">
                            <div class="entity-detail">
                                <div class="panel panel-default">
                                    <div class="panel-heading">Entity detail
                                        <div class="pull-right">
                                            <button type="button" class="btn btn-primary btn-xs" id="btn-edit"
                                                    disabled="disabled">Enable editing entity
                                            </button>
                                            <button type="button" class="btn btn-danger btn-xs" id="btn-delete"
                                                    disabled="disabled">Delete entity
                                            </button>
                                        </div>
                                    </div>
                                    <div class="panel-body" style="min-height:500px">
                                        <div class="detail-content" id="entity-detail">
                                            <input id="entity-id" hidden>
                                            <div class="form-group">
                                                <label for="entity-name">Name:</label>
                                                <a href="#" class="editable" id="entity-name" data-type="text"
                                                   data-pk="" data-url="/api/entity" data-title="Enter entity name"></a>
                                            </div>
                                            <div class="form-group">
                                                <label for="entity-domain">Domain:</label>
                                                <span class="disabled" id="entity-domain" readonly="readonly"></span>
                                            </div>
                                            <div class="form-group">
                                                <label for="entity-description">Description:</label>
                                                <a href="#" class="editable" id="entity-description"
                                                   data-type="textarea" data-pk="" data-url="/api/entity"
                                                   data-title="Enter entity description"></a>
                                            </div>
                                            <hr>
                                            <h3> Properties </h3>
                                            <div class="tab-pane" id="properties" style="min-height: 500px;">
                                                <table class="table table-striped" id="properties-table">
                                                    <thead>
                                                    <tr>
                                                        <th style="width:20px"></th>
                                                        <th> Property name</th>
                                                        <th> Action</th>
                                                    </tr>
                                                    </thead>
                                                    <tbody>
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                        <div class="detail-content" id = "new-entity">
                                            <div class="form-group">
                                                <label for="new-entity-name">Name:</label>
                                                <input type="text" class="form-control" id="new-entity-name">
                                            </div>
                                            <div class="form-group">
                                                <label for="new-entity-description">Description:</label>
                                                <input type="text" class="form-control" id="new-entity-description">
                                            </div>
                                            <div class="modal-footer">
                                                <button type="button" class="btn btn-primary pull-right" id="save-entity" style="margin:5px">Save</button>
                                            </div>
                                        </div>
                                        <div class="detail-content" id="entity-placeholder"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="modal fade" id="confirm-delete" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
     aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">

            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                <h4 class="modal-title" id="myModalLabel">Confirm Delete</h4>
            </div>

            <div class="alert alert-danger collapse" role="alert" id="alert-delete-modal">
                <button type="button" class="close" aria-label="Close" onclick="$('#alert-delete-modal').hide()"><span
                        aria-hidden="true">&times;</span></button>
                <div id="alert-delete-modal-text"></div>
            </div>

            <div class="modal-body">
                <p>You are about to delete one track, this procedure is irreversible.</p>
                <p>Do you want to proceed?</p>
                <input id="delete-entity-id" hidden>
                <div class="form-group">
                    <label for="delete-entity-name">Name:</label>
                    <input type="text" class="form-control" id="delete-entity-name" readonly="readonly">
                </div>
            </div>

            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>
                <a class="btn btn-danger btn-ok" id="btn-delete-confirm">Delete</a>
            </div>
        </div>
    </div>
</div>

<div class="modal fade" id="edit-modal" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title">Add properties</h4>
      </div>
      <div class="modal-body">
            <div id="devices-list" class="list-group" style="margin-bottom:0"></div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal"><span class="glyphicon glyphicon-remove" aria-hidden="true"></span> Close</button>
        <button type="button" class="btn btn-primary" id="btn-edit-ok"><span class="glyphicon glyphicon-ok" aria-hidden="true"></span> OK</button>
      </div>
    </div>
  </div>
</div>


<!-- /#page-content-wrapper -->

%include partial/admin/footer

<script type="text/javascript" language="JavaScript">
    requirejs(['admin/virtualEntity']);
</script>