%rebase('./base.tpl',title='Admin Page | Proxy')

%include  partial/admin/nav user=user

%include partial/admin/sidebar

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
                                    <h3 class="panel-title">Proxies</h3>
                                </div>
                                <div class="panel-body" style="padding:0">
                                    <div id="proxy-list" class="list-group" style="margin-bottom:0">
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-9">
                            <div class = "proxy-detail">
                                <div class="panel panel-default">
                                    <div class="panel-heading">Proxy detail</div>
                                    <div class="panel-body" style="min-height:500px">
                                        <div id="proxy-detail">
                                            <ul class="nav nav-tabs" id="tabContent">
                                                <li class="active"><a  href="#general" id="general-tab" data-toggle="tab" onfocus="this.style.outline = 0">General</a></li>
                                                <li><a href="#devices" id="devices-tab" data-toggle="tab" onfocus="this.style.outline = 0">Devices</a></li>
                                            </ul>
                                            <div class="tab-content">
                                                <div class="tab-pane active" id="general">
                                                    <input id="proxy-id" hidden>
                                                    <div class="form-group">
                                                        <label for="usr">Name:</label>
                                                        <input type="text" class="form-control" id="proxy-name">
                                                    </div>
                                                    <div class="form-group">
                                                        <label for="description">Description:</label>
                                                        <input type="text" class="form-control" id="proxy-description">
                                                    </div>
                                                    <div class="form-group">
                                                        <label for="last-connected">Last connected:</label>
                                                        <input type="text" class="form-control" id="proxy-last-connected" readonly="readonly">
                                                    </div>
                                                    <div class="form-group">
                                                        <label for="ip-address">IP Address:</label>
                                                        <input type="text" class="form-control" id="proxy-ip-address" readonly="readonly">
                                                    </div>
                                                    <div class="form-group">
                                                        <label for="mac-address">MAC Address:</label>
                                                        <input type="text" class="form-control" id="proxy-mac-address" readonly="readonly">
                                                    </div>
                                                    <div class="form-group">
                                                        <label for="model">Model:</label>
                                                        <input type="text" class="form-control" id="proxy-model" readonly="readonly">
                                                    </div>
                                                    <div class="form-group">
                                                        <label for="os">OS:</label>
                                                        <input type="text" class="form-control" id="proxy-os" readonly="readonly">
                                                    </div>
                                                </div>
                                                <div class="tab-pane" id="devices" style="min-height: 500px;">
                                                    <table class="table table-striped" id="devices-table">
                                                        <thead>
                                                          <tr>
                                                                <th style="width:20px">  </th>
                                                                <th> Device name </th>
                                                                <th> Last connected </th>
                                                                <th> Action </th>
                                                            </tr>
                                                        </thead>
                                                        <tbody>
                                                        </tbody>
                                                    </table>
                                                </div>
                                            </div>
                                             <div class="modal-footer">
                                            <button type="button" class="btn btn-danger pull-right" id="delete-proxy" style="margin:5px">Delete</button>
                                            <button type="button" class="btn btn-primary pull-right" id="save-proxy" style="margin:5px">Save</button>
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

%include partial/admin/footer

<script type="text/javascript" language="JavaScript">
  requirejs(['admin/proxy']);
</script>