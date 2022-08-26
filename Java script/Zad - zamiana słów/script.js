let result = document.querySelector('.result');
let submit = document.querySelector('#submit');

submit.addEventListener('click', () => {
  let first = document.querySelector('#first').value;
  let secound = document.querySelector('#secound').value;
  let holder = first[0];
  first[0] = holder;
  first = first.replace(first[0], secound[0]);
  secound = secound.replace(secound[0], holder);
  result.textContent = `${first} ${secound}`;
});
