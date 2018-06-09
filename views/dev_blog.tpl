% rebase('layout.tpl', title=title, year=year)

<nav class="navbar navbar-inverse">
	<div class="container-fluid">
		<div class="navbar-header">
			<a class="navbar-brand" href="">Filter</a>
		</div>
		<ul class="nav navbar-nav" id="filter">
			<li><a href="#" onclick="showElement('features','1');">Features</a></li>
			<li><a href="#" onclick="showElement('changelog','2');">Changelog</a></li>
			<li><a href="#" onclick="showElement('other','3');">Other</a></li>
		</ul>
	</div>
</nav>

<div class="container" id="features">
	<div class="panel panel-default">
		<div class="panel-heading"><b>Features</b></div>
			<div class="panel-body">
				<div class="table-responsive">
					<table class="table">
					- Fully open source.<br>
					- Powered by a python back-end.<br>
					- Using the latest libraries.<br>
					- Can be easily deployed in the cloud.<br>
					- Personal custom blog.<br>
					- Secure, admin only set of writing/reading database managment script the frontend will fetch only.<br>
					- An integrated python mailer, just set your email in the config file<br>
					- MIT License.<br>
					</table>
				</div>

		</div>
	</div>
</div>

<div class="container" id="changelog">
	<div class="panel panel-default">
		<div class="panel-heading"><b>Changelog</b></div>
			<div class="panel-body">
				<div class="table-responsive">
					<table class="table">
					<b>Ver.01</b> - Initial version is out please note that the whole project is WIP.<br>
					</table>
				</div>
			</div>
		
	</div>
</div>

<div class="container" id="other">
	<div class="panel panel-default">
		<div class="panel-heading"><b>Other</b></div>
			<div class="panel-body">
				No news for now.<br>
			</div>

	</div>
</div>