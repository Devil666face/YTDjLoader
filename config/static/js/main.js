function setTheme(event) {
	var element = event.target;
	var navbar = document.getElementById('navbar');
	navbar.setAttribute('data-bs-theme',element.getAttribute('data-bs-theme-value'));
}

themeIdList = ['light', 'dark', 'auto'];
for (id in themeIdList) {
	document.getElementById('bd-theme-'+themeIdList[id]).addEventListener('click', setTheme);
}
