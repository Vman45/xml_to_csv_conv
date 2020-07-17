let picker = document.getElementById('picker');
let listing = document.getElementById('listing');

picker.addEventListener('change', e => {
  for (let file of Array.from(e.target.files)) {
    let item = document.createElement('li');
    item.textContent = file.webkitRelativePath;
    listing.appendChild(item);
  };
});

// Array.from() needed for Edge