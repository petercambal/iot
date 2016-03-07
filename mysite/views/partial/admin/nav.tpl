<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand menu-toggle" href="#">Internet of Things admin page</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav navbar-right">
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"><span class="glyphicon glyphicon-user"></span> Hi <b>{{user.get_name()}}</b> <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li class="menu-toggle"><a href="#"><span class="glyphicon glyphicon-resize-horizontal"></span> Toggle sidebar</a></li>
             <li><a href="/"><span class="glyphicon glyphicon-home"></span> Homepage</a></li>
            <li role="separator" class="divider"></li>
            <li id="btn-logout"><a href="#"><span class="glyphicon glyphicon-off"></span> Log out</a></li>
          </ul>
        </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>

