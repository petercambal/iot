%rebase('./base.tpl',title='Admin Page | Domain')

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
                <h1>Domains</h1>
                <div class="container-fluid">
                    <div class="row">
                        <div class="col-lg-3">
                            <div class="panel panel-default">
                                <div class="panel-heading">
                                    Domains
                                    <div class="pull-right">
                                            <button type="button" class="btn btn-primary btn-xs" id="btn-edit" disabled="disabled">Edit domain</button>
                                    </div>
                                </div>
                                <div class="panel-body" style="padding:0">
                                    <div id="treeview1" style="min-height: 500px;overflow-y: scroll;"></div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-9">
                            <div class = "domain-detail">
                                <div class="panel panel-default">
                                    <div class="panel-heading">Domain detail
                                         <div class="pull-right">
                                            <button type="button" class="btn btn-default btn-xs" id="btn-new">New Domain</button>
                                        </div>
                                    </div>
                                    <div class="panel-body" style="min-height:500px">
                                        <div id="domain-detail">
                                            <div style="padding: 5px;">
                                                <table class="table table-striped" id="table-entities" cellspacing="0" width="100%"></table>
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

<div class="modal fade" id="edit-modal" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title">Edit domain</h4>
      </div>
      <div class="modal-body">
        <form class="form-horizontal">
          <input type="hidden" id="domain-id">

          <div class="form-group" id="grp-domain-name">
            <label for="domain-name" class="col-sm-2 control-label">Name</label>
            <div class="col-sm-10"><input type="text" class="form-control" id="domain-name" placeholder="Name" /></div>
          </div>

          <div class="form-group">
            <label for="parent-domain" class="col-sm-2 control-label">Parent domain</label>
            <div class="col-sm-10">
              <select id="domain-parentId" data-placeholder="Choose parent domain" class="chosen-select"></select>
            </div>
          </div>

        </form>

      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal"><span class="glyphicon glyphicon-remove" aria-hidden="true"></span> Close</button>
        <button type="button" class="btn btn-primary" id="btn-edit-ok"><span class="glyphicon glyphicon-ok" aria-hidden="true"></span> OK</button>
      </div>
    </div>
  </div>
</div>



%include partial/admin/footer

<script type="text/javascript" language="JavaScript">
  requirejs(['admin/domain']);
</script>