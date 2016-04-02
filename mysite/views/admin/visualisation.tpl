%rebase('./base.tpl',title='Admin Page | Visualisation')

%include  partial/admin/nav user=user


%include partial/admin/sidebar
<!-- Page Content -->
<div id="page-content-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1>Visualisation</h1>
                <div class="row">
                    <div class="col-lg-5">
                        <div class="input-group">
                            <div class="input-group-btn">
                                <button type = "button" class = "btn btn-default" id="subscribe"><span class="glyphicon glyphicon-play"></span> Subscribe</button>
                                <button type = "button" class = "btn btn-default" id="unsubscribe"><span class="glyphicon glyphicon-pause"></span> Unsubscribe</button>
                            </div>
                            <input type="text" id="topic" class="form-control">
                        </div>
                    </div>
                </div>
                <div class="spacer-40"></div>
                <div>
				    <canvas id="canvas" height="450" width="600"></canvas>
			    </div>
            </div>
        </div>
    </div>
</div>


%include partial/admin/footer

<script type="text/javascript" language="JavaScript">
    requirejs(['admin/visualisation']);
</script>