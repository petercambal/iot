%rebase('./base.tpl',title="Register")

%include  partial/public/nav user=None

<div id="signupbox" style="margin-top:50px" class="mainbox col-md-6 col-md-offset-3 col-sm-8 col-sm-offset-2">
    <div class="panel panel-info">
        <div class="panel-heading">
            <div class="panel-title">Sign Up</div>
            <div style="float:right; font-size: 85%; position: relative; top:-10px"><a id="signinlink" href="/login">Sign In</a></div>
        </div>
        <div class="panel-body" >
            <form id="signupform" class="form-horizontal" role="form">

                <div id="signupalert" style="display:none" class="alert alert-danger">
                    <p>Error:</p>
                    <span></span>
                </div>

                <div class="form-group">
                    <label for="username" class="col-md-3 control-label">Username</label>
                    <div class="col-md-9">
                        <input type="text" class="form-control" id="username" name="username" placeholder="Username">
                    </div>
                </div>

                <div class="form-group">
                    <label for="password" class="col-md-3 control-label">Password</label>
                    <div class="col-md-9">
                        <input type="password" class="form-control" id="password" name="password" placeholder="Password">
                    </div>
                </div>

                <div class="form-group">
                    <label for="re-password" class="col-md-3 control-label">Confirm Password</label>
                    <div class="col-md-9">
                        <input type="password" class="form-control" id="re-password" name="re-password" placeholder="Password">
                    </div>
                </div>

                <div class="form-group">
                    <!-- Button -->
                    <div class="col-md-offset-3 col-md-9">
                        <button id="btn-signup" type="button" class="btn btn-info"><i class="icon-hand-right"></i> &nbsp Sign Up</button>
                    </div>
                </div>

            </form>
         </div>
        </div>
    </div>
</div>