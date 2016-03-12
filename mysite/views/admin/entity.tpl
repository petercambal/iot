%rebase('./base.tpl',title='Admin Page | Entities')

%include  partial/admin/nav user=user


%include partial/admin/sidebar
<!-- Page Content -->

<div class="alert alert-danger collapse" role="alert" id="alert-msg">
    <button type="button" class="close" aria-label="Close" onclick="$('#alert-msg').hide()"><span aria-hidden="true">&times;</span></button>
    <div id="alert-msg-text"></div>
</div>

<div class="alert alert-success collapse" role="alert" id="success-msg">
    <button type="button" class="close" aria-label="Close" onclick="$('#success-msg').hide()"><span aria-hidden="true">&times;</span></button>
    <div id="success-msg-text"></div>
</div>

<div id="page-content-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1>Proxies</h1>
                <div class="container-fluid">
                    <div class="row">
                        <div class="col-lg-3">
                            <div class="panel panel-default">
                                <div class="panel-heading">
                                    <h3 class="panel-title">Virtual Entities</h3>
                                </div>
                                <div class="panel-body" style="padding:0">
                                    <div id="entity-list" class="list-group" style="margin-bottom:0">
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-9">
                            <div class = "entity-detail">
                                <div class="panel panel-default">
                                    <div class="panel-heading">Entity detail</div>
                                    <div class="panel-body" style="min-height:500px">
                                        <div id="entity-detail">
                                            <table class="table" id="entities-table">
                                                <thead>
                                                    <th> Id </th>
                                                    <th> Name </th>
                                                    <th> Description </th>
                                                    <th> Sensors count </th>
                                                </thead>
                                                <tbody >

                                                </tbody>
                                              </table>
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
</div>

<div class="modal fade" id="confirm-delete" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">

                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                    <h4 class="modal-title" id="myModalLabel">Confirm Delete</h4>
                </div>

                <div class="alert alert-danger collapse" role="alert" id="alert-delete-modal">
                    <button type="button" class="close" aria-label="Close" onclick="$('#alert-delete-modal').hide()"><span aria-hidden="true">&times;</span></button>
                    <div id="alert-delete-modal-text"></div>
                </div>

                <div class="modal-body">
                    <p>You are about to delete one track, this procedure is irreversible.</p>
                    <p>Do you want to proceed?</p>
                    <input id="delete-proxy-id" hidden>
                    <div class="form-group">
                        <label for="usr">Name:</label>
                        <input type="text" class="form-control" id="delete-proxy-name" readonly="readonly">
                    </div>
                </div>

                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>
                    <a class="btn btn-danger btn-ok" id="btn-delete-confirm">Delete</a>
                </div>
            </div>
        </div>
    </div>


<!-- /#page-content-wrapper -->

%include partial/admin/footer

<script type="text/javascript" language="JavaScript">
  requirejs(['admin/virtualEntity']);
</script>