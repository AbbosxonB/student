document.getElementById('registrationForm').addEventListener('submit', function (e) {
    e.preventDefault();
    
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const country = document.getElementById('country').value;
  
    if (name && email && country) {
      alert(`Thank you, ${name}! Your registration is complete.`);
      // Formani tozalash
      this.reset();
    } else {
      alert('Please fill in all the fields.');
    }
  });
  