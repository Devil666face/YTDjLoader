function setTheme(event) {
	var element = event.target;
	var navbar = document.getElementById('navbar');
	navbar.setAttribute('data-bs-theme',element.getAttribute('data-bs-theme-value'))
}
for (id in ['light', 'dark', 'auto']) {
	document.getElementById('bd-theme-'+id).addEventListener('click', setTheme)
}
