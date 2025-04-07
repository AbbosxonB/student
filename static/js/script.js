document.querySelectorAll('button').forEach(btn => {
    btn.addEventListener('click', () => {
      alert(`${btn.textContent.trim()} tugmasi bosildi`);
    });
  });
  