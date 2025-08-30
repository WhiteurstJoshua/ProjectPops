function toggleRate(value) {
  document.getElementById('hourly_rate').style.display = value === 'Hourly' ? 'block' : 'none';
}

document.getElementById('agreementForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const formData = new FormData(this);
  let output = '<h2>Agreement Summary</h2><ul>';
  for (let [key, value] of formData.entries()) {
    output += `<li><strong>${key}:</strong> ${value}</li>`;
  }
  output += '</ul>';
  document.getElementById('output').innerHTML = output;
});
