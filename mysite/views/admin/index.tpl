%rebase('./base.tpl',title='Admin Page')

%include  partial/admin/nav user=user

%include partial/admin/sidebar
<!-- Page Content -->
<div id="page-content-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1>Internet of things</h1>
                <p>This is admin page of internet of things name server.</p>
            </div>
        </div>
    </div>
</div>
<!-- /#page-content-wrapper -->

%include partial/admin/footer
