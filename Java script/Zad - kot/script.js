const form = document.querySelector('.form');
const answear = document.querySelector('.answear');
// alert('Storna bezpieczna dla epileptyków :)');
form.addEventListener('submit', (event) => {
  const inputValue = event.srcElement[0].value;
  let napis = [];
  for (let i = 3; i >= 1; i--) {
    napis.push(inputValue[inputValue.length - i]);
  }
  const end = napis.toString('').replace(/,/g, '');
  event.preventDefault();
  if (inputValue.length >= 6 && end === 'kot') {
    answear.textContent =
      'Wyraz składa się z conajmniej 6 liter i na końcu pisze kot';
  }
  if (inputValue.length >= 6 && end !== 'kot') {
    answear.textContent =
      'Wyraz składa się z conajmniej 6 liter ale na końcu nie pisze kot';
  }
  if (inputValue.length < 6 && end === 'kot') {
    answear.textContent =
      'Wyraz nie składa się z conajmniej 6 liter ale na końcu pisze kot';
  }
  if (inputValue.length < 6 && end !== 'kot') {
    answear.textContent =
      'Wyraz nie składa się z conajmniej 6 liter i na końcu nie pisze kot';
  }
});
