document.querySelector('#ulu').oninput = function () {
	let val = this.value.trim().toLowerCase();
	let elasticItems = document.querySelectorAll('.ulu li');
	if (val != '') {
		elasticItems.forEach(function (elem) {
			if(elem.innerText.toLowerCase().search(val) == -1) {
				elem.classList.add('hide');
			}
			else {
				elem.classList.remove('hide');
			}
		});
	}
	else {
		elasticItems.forEach(function (elem) {
			elem.classList.remove('hide');
		});
	}
}