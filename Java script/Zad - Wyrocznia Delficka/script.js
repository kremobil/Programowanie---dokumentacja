let button = document.querySelector('.btn');
let ans = document.querySelector('.ans');
let done = true;
let img = document.querySelector('img');

const chceck = () => {
  if (done) {
    button.classList.add('btn-animated');
    button.style.transform = 'scale(1.3)';
    document.querySelector('body').style.cursor = 'none';
    let procent = Math.floor(Math.random() * 100);
    ans.textContent = `Prawdopodobieństwo, że tak będzie wynosi: ${procent}%`;
    if (procent < 34) {
      ans.style.setProperty('--color', 'red');
    } else if (procent < 67) {
      ans.style.setProperty('--color', 'blue');
    } else {
      ans.style.setProperty('--color', 'green');
    }
    ans.classList.add('ans-animated');
    img.classList.add('bye');
    done = false;
  }
};

button.addEventListener('click', chceck);
