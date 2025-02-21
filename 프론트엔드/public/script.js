fetch('http://localhost:5000/api/data')
    .then(response => response.json())
    .then(data => {
        document.getElementById('api-data').textContent = data.message;
    })
    .catch(error => console.error(error));