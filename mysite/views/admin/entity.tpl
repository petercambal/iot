%rebase('./base.tpl',title='Admin Page')

%include  partial/admin/nav user=user


%include partial/admin/sidebar
<!-- Page Content -->
<div class="alert alert-danger collapse" role="alert" id="alert-msg">
    <button type="button" class="close" aria-label="Close" onclick="$('#alert-msg').hide()"><span aria-hidden="true">&times;</span></button>
    <div id="alert-msg-text"></div>
</div>

<div id="page-content-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1>Entities</h1>

                <div class="panel panel-default">

                      <div class="panel-heading">Entities table</div>
                      <div class="panel-body">
                        <p>wadwmkadpawndpawndpawodnwpodan</p>
                      </div>

                      <!-- Table -->
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

<!-- /#page-content-wrapper -->

%include partial/admin/footer

<script type="text/javascript" language="JavaScript">
  requirejs(['admin/virtualEntity']);
</script>