let button = document.querySelector('.btn');
let total = document.querySelector('.wynik');

const calcTriangle = (a, b, c) => {
  total.textContent = `Pole trójkąta wynosi: ${a + b + c}`;
  // console.log(`Pole trójkąta wynosi: ${a + b + c}`);
  // console.log(total);
};

const startProgran = () => {
  let a = parseInt(document.querySelector('.in1').value);
  let b = parseInt(document.querySelector('.in2').value);
  let c = parseInt(document.querySelector('.in3').value);

  if (a + b > c && a + c > b && b + c > a) {
    calcTriangle(a, b, c);
  } else {
    total.textContent = `Z tych boków nie da się utworzyć trójkąta`;
  }
};

button.addEventListener('click', startProgran);
