function setTheme(event) {
	var element = event.target;
	var navbar = document.getElementById('navbar');
	navbar.setAttribute('data-bs-theme',element.getAttribute('data-bs-theme-value'))
}
var buttonsId = ['light','dark', 'auto']
for (id in buttonsId) {
	document.getElementById('bd-theme-'+id).addEventListener('click', setTheme)
}
