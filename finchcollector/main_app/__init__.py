<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Finch Collector</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
</head>
<body>
  <header class="navbar-fixed">
    <nav>
      <div class="nav-wrapper">
        <ul>
          <li><a href="/" class="left brand-logo">&nbsp;&nbsp;FinchCollector</a></li>
        </ul>
        <ul class="right">
          <li><a href="/about">About</a></li>
        </ul>
      </div>
    </nav>
  </header>
  <main class="container">
    {% block content %}
    {% endblock %}
  </main>
  <footer class="page-footer">
    <div class="right">No Rights Reserved, &copy; 2022 Finch Collector &nbsp;</div>
  </footer>
</body>
</html>