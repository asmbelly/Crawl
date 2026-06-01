// Animate sections on scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('section').forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(24px)';
  el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
  observer.observe(el);
});

// Download button click feedback
const dlBtn = document.getElementById('dlBtn');
if (dlBtn) {
  dlBtn.addEventListener('click', () => {
    const original = dlBtn.innerHTML;
    dlBtn.innerHTML = '<span class="btn-icon">✓</span> Downloading...';
    dlBtn.style.background = '#2a6e2a';
    setTimeout(() => {
      dlBtn.innerHTML = original;
      dlBtn.style.background = '';
    }, 3000);
  });
}

// Typewriter effect on ascii art load
const ascii = document.querySelector('.ascii');
if (ascii) {
  const text = ascii.textContent;
  ascii.textContent = '';
  let i = 0;
  const type = () => {
    if (i < text.length) {
      ascii.textContent += text[i++];
      setTimeout(type, 2);
    }
  };
  setTimeout(type, 200);
}
